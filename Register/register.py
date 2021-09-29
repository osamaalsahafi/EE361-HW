import random
from myhdl import delay, block, always_seq, Signal, intbv, modbv, always, \
    ResetSignal, instance, StopSimulation, instances, bin

random.seed(2)
randrange = random.randrange
ACTIVE, INACTIVE = 0, 1


@block
def register(load_in, load_out, enable, clock, reset):
    @always_seq(clock.posedge, reset=reset)
    def shifter():
        if enable:
            load_out.next = load_in

    return shifter


load_in = Signal(modbv(0)[32:0])
load_out = Signal(modbv(0)[32:0])
amount = Signal(intbv(0)[3:0])
clock = Signal(bool(0))
enable = Signal(bool(0))
reset = ResetSignal(0, active=0, isasync=True)


@block
def testbench():
    ins = register(load_in, load_out, enable, clock, reset)

    @always(delay(10))
    def clockGen():
        clock.next = not clock
        return clockGen

    @instance
    def stimulus():
        reset.next = ACTIVE
        yield clock.negedge
        reset.next = INACTIVE
        for i in range(20):
            load_in.next, enable.next = randrange(2 ** 32), randrange(2)
            yield clock.posedge
        raise StopSimulation()

    @instance
    def monitor():
        print("             load in                |              load out                     | enable |")
        print("------------------------------------|-------------------------------------------|--------|")
        yield clock.posedge
        for i in range(20):
            print("%s    |     %s      |   %s    |" % (bin(load_in, 32), bin(load_out, 32), bin(enable)))
            yield clock.posedge
            yield delay(10)

    return instances()


def convert():
    a = register(load_in, load_out, enable, clock, reset)
    a.convert(hdl='Verilog')


tb = testbench()
tb.run_sim()
convert()

