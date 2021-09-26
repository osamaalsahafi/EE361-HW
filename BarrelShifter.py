from myhdl import block, always, bin, \
    Signal, delay, modbv, always_comb
from random import randrange


@block
def barrel_shifter(load_value, load_input, shift_reg):

    @always_comb
    def shift_bit():
        load_value.next = load_input >> shift_reg

    return shift_bit


load_value = Signal(modbv(0)[12:])
load_input = Signal(modbv(0)[12:])
shift_reg = Signal(modbv(0)[3:])


@block
def test_bench():
    test_bench_shifter = barrel_shifter(load_value, load_input, shift_reg)

    @always(delay(10))
    def generator():
        shift_reg.next = randrange(8)
        load_input.next = randrange(2**12)

    @always(delay(10))
    def monitor():
        print("%s    :   %s  :    %s" % (bin(load_input, 12), bin(shift_reg, 3), bin(load_value, 12)))

    return test_bench_shifter, generator, monitor

def simulate():
    tb = test_bench()
    print("  load_value    |  shift |      load_shift ")
    tb.run_sim(200)


def convert():
    conv = barrel_shifter(load_value, load_input, shift_reg)
    conv.convert(hdl='Verilog')


convert()
simulate()




