from myhdl import block, always_comb, Signal, intbv, delay, \
    instance, instances, bin
import random

random.seed(2)
randrange = random.randrange


@block
def mux_2to1(i0, i1, sel, out):
    @always_comb
    def mux2to1():
        if sel == 0:
            out.next = i0
        else:
            out.next = i1

    return mux2to1


i0 = Signal(bool(0))
i1 = Signal(bool(0))
sel = Signal(bool(0))
out = Signal(bool(0))


@block
def tbb():
    i0, i1, sel0, out = [Signal(intbv(0)) for i in range(4)]
    mux1 = mux_2to1(i0, i1, sel0, out)

    @instance
    def stimulus():
        print("i0     i1      sel    output")
        print()
        for i in range(20):
            i0.next, i1.next, sel0.next = randrange(2), randrange(2), randrange(2)
            yield delay(10)
            print(" %s      %s       %s       %s" % (bin(i0), bin(i1), bin(sel0), bin(out)))

    return instances()


def convert():
    tst = mux_2to1(i0, i1, sel, out)
    tst.convert(hdl='Verilog')


convert()
tb = tbb()
tb.run_sim()
