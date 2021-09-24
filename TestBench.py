from myhdl import block, always, instance, Signal, \
    ResetSignal, modbv, delay, StopSimulation , bin
from Counter import inc

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

@block
def test_inc():
    x = 12
    count = Signal(modbv(0)[x:])
    enable = Signal(bool(0))
    clk = Signal(bool(0))
    reset = ResetSignal(0, active=0, isasync=True)
    inc_1 = inc(count, enable, clk, reset)
    HALF_PERIOD = delay(10)

    @always(HALF_PERIOD)
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        for i in range(3):
            yield clk.negedge
        reset.next = INACTIVE_HIGH
        for i in range(4096):
            enable.next = 1
            yield clk.negedge
            enable.next = 0
            yield clk.negedge
        raise StopSimulation()

    @instance
    def monitor():

        print("enable   count")
        yield reset.posedge
        while 1:
            yield clk.posedge
            yield delay(1)
            print("   %s      %s" % (int(enable), bin(count, 12)))

    return clkgen, stimulus, inc_1, monitor


tb = test_inc()
tb.run_sim()
