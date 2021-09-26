from myhdl import always_comb, block, Signal, intbv, \
    delay, instance, instances

import random

random.seed(2)
randrange = random.randrange


@block
def decoder(i0, i1, d0, d1, d2, d3):
    @always_comb
    def decoder_2to4():
        if i1 == 0 and i0 == 0:
            d0.next = 1
            d1.next = 0
            d2.next = 0
            d3.next = 0
        elif i1 == 0 and i0 == 1:
            d0.next = 0
            d1.next = 1
            d2.next = 0
            d3.next = 0
        elif i1 == 1 and i0 == 0:
            d0.next = 0
            d1.next = 0
            d2.next = 1
            d3.next = 0
        else:
            d0.next = 0
            d1.next = 0
            d2.next = 0
            d3.next = 1

    return decoder_2to4


i0 = Signal(bool(0))
i1 = Signal(bool(0))
d0 = Signal(bool(0))
d1 = Signal(bool(0))
d2 = Signal(bool(0))
d3 = Signal(bool(0))

@block
def testbench():
    i0, i1, d0, d1, d2, d3 = [Signal(intbv(0)) for i in range(6)]
    dec = decoder(i0, i1, d0, d1, d2, d3)

    @instance
    def stimulus():
        print("i0 i1   d0 d1 d2 d3")
        for i in range(20):
            i0.next, i1.next = randrange(2), randrange(2)
            print("%s  %s     %s  %s  %s  %s" % (i0, i1, d0, d1, d2, d3))
            yield delay(10)

    return instances()


def convert():
    tst = decoder(i0, i1, d0, d1, d2, d3)
    tst.convert(hdl='Verilog')


convert()
tb = testbench()
tb.run_sim()
