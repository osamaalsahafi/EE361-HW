import random
from myhdl import block, always_comb, instance, intbv, instances, Signal, delay

random.seed()
randrange = random.randrange


@block
def decoder(i0, i1, i2, i3, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15):
    @always_comb
    def decoder_4to16():
        d0.next = ~i3 & ~i2 & ~i1 & ~i0
        d1.next = ~i3 & ~i2 & ~i1 & i0
        d2.next = ~i3 & ~i2 & i1 & ~i0
        d3.next = ~i3 & ~i2 & i1 & i0
        d4.next = ~i3 & i2 & ~i1 & ~i0
        d5.next = ~i3 & i2 & ~i1 & i0
        d6.next = ~i3 & i2 & i1 & ~i0
        d7.next = ~i3 & i2 & i1 & i0
        d8.next = i3 & ~i2 & ~i1 & ~i0
        d9.next = i3 & ~i2 & ~i1 & i0
        d10.next = i3 & ~i2 & i1 & ~i0
        d11.next = i3 & ~i2 & i1 & i0
        d12.next = i3 & i2 & ~i1 & ~i0
        d13.next = i3 & i2 & ~i1 & i0
        d14.next = i3 & i2 & i1 & ~i0
        d15.next = i3 & i2 & i1 & i0

    return decoder_4to16


@block
def testbench():
    i0, i1, i2, i3, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, \
    d12, d13, d14, d15 = [Signal(intbv(0)[1:]) for i in range(20)]
    dec = decoder(i0, i1, i2, i3, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15)

    @instance
    def stimulus():
        print("i3,i2,i1,i0   d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 d11 d12 d13 d14 d15")
        for i in range(20):
            i0.next, i1.next, i2.next, i3.next = randrange(2), randrange(2), randrange(2), randrange(2)
            yield delay(10)
            print(" %s  %s  %s  %s |  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s   %s   %s   %s   %s   %s" \
                  % (i3, i2, i1, i0, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15))

    return instances()


tb = testbench()
tb.run_sim()