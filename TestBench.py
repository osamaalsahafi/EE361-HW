import random
from myhdl import block, always, instance, Signal, \
    ResetSignal, modbv, delay, StopSimulation
from Counter import inc

random.seed(1)
randrange = random.randrange
ACTIVE_LOW, INACTIVE_HIGH = 0, 1

@block
def test_inc():
    x = 3
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
        reset.next = ACTIVE_LOW
        yield clk.negedge
        reset.next = INACTIVE_HIGH
        for i in range(16):
            enable.next = min(1, randrange(3))
            yield clk.negedge
        raise StopSimulation()

    @instance
    def monitor():

        print("enable   count")
        yield reset.posedge
        while 1:
            yield clk.posedge
            yield delay(1)
            print("   %s      %s" % (int(enable), count))

    return clkgen, stimulus, inc_1, monitor


tb = test_inc()
tb.run_sim()
