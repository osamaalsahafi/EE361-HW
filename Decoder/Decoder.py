import random
from myhdl import *

random.seed()
randrange = random.randrange


@block
def decoder(i0, i1, d0, d1, d2, d3):
    @always_comb
    def decoder_2to4():
        d0.next = ~i1 & ~i0
        d1.next = ~i1 & i0
        d2.next = i1 & ~i0
        d3.next = i1 & i0
    return decoder_2to4


@block
def testbench():
    i0, i1, d0, d1, d2, d3 = [Signal(intbv(0)[1:]) for i in range(6)]
    dec = decoder(i0, i1, d0, d1, d2, d3)

    @instance
    def stimulus():
        print("i1 i0   d3 d2 d1 d0")
        for i in range(20):
            i0.next, i1.next = randrange(2), randrange(2)
            yield delay(10)
            print("%s  %s     %s  %s  %s  %s" % (i1, i0, d3, d2, d1, d0))

    return instances()

def convert():
    i0, i1, d0, d1, d2, d3 = [Signal(intbv(0)[1:]) for i in range(6)]
    conv = decoder(i0, i1, d0, d1, d2, d3)
    conv.convert(hdl='Verilog')


convert()
tb = testbench()
tb.run_sim()