from myhdl import block, always, instance, Signal, \
    ResetSignal, modbv, delay, StopSimulation, bin, always_seq, traceSignals, Simulation

ACTIVE_LOW, INACTIVE_HIGH = 0, 1


@block
def Counter(count, enable, clk, reset):
    """
    #count -- output
    #enable -- control input, increment when 1
    #clk -- clock input
    #reset -- asynchronous reset input
    """

    @always_seq(clk.posedge, reset=reset)
    def counter():
        if enable:
            count.next = count + 1

    return counter

@block
def Test():
    count = Signal(modbv(0)[12:])
    enable = Signal(bool(0))
    clk = Signal(bool(0))
    reset = ResetSignal(0, active=0, isasync=True)
    counter_test = Counter(count, enable, clk, reset)
    inc_1 = Counter(count, enable, clk, reset)
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


def convert():
    count = Signal(modbv(0)[12:])
    enable = Signal(bool(0))
    clk = Signal(bool(0))
    reset = ResetSignal(0, active=0, isasync=True)
    tst = Counter(count, enable, clk, reset)
    tst.convert(hdl='Verilog')


convert()
tb = Test()
tb.run_sim()
