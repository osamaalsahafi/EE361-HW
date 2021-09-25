from myhdl import block, always_comb, intbv, Signal,\
    delay, instance, instances
import random

random.seed(2)
randrange = random.randrange

@block
def mux_3to1(i0, i1, i2, sel0, sel1, out):
    @always_comb
    def mux3to1():
        if sel0 == 0 and sel1 == 0:
            out.next = i0
        elif sel0 == 0 and sel1 == 1:
            out.next = i1
        else:
            out.next = i2
    return mux3to1


i0 = Signal(bool(0))
i1 = Signal(bool(0))
i2 = Signal(bool(0))
sel0 = Signal(bool(0))
sel1 = Signal(bool(0))
out = Signal(bool(0))

@block
def tbmux3to1():
    i0, i1, i2, sel0, sel1, out = [Signal(intbv(0)) for i in range(6)]
    mux = mux_3to1(i0, i1, i2, sel0, sel1, out)

    @instance
    def stimulus():
        print("i0 i1 i2 sel1 sel0  out")
        for i in range(20):
            i0.next, i1.next, i2.next= randrange(2), randrange(2), randrange(2)
            sel0.next, sel1.next = randrange(2), randrange(2)
            yield delay(10)
            print("%s  %s  %s    %s    %s    %s" % (i0, i1, i2, sel1, sel0, out))
    return instances()


def convert():
    tst = mux_3to1(i0, i1, i2, sel0, sel1, out)
    tst.convert(hdl='Verilog')

convert()
tb = tbmux3to1()
tb.run_sim()

