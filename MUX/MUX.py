import random
from myhdl import block, instance, always_comb, Signal, intbv, delay, bin

random.seed()
randrange = random.randrange


@block
def mux_2to1(i0, i1, sel, output):
    @always_comb
    def mux2to1():
        if sel == 0:
            output.next = i0
        else:
            output.next = i1

    return mux2to1


@block
def mux_3to1(i0, i1, i2, sel, out):

    @always_comb
    def mux3to1():
        if sel == 0:
            out.next = i0
        if sel == 1:
            out.next = i1
        else:
            out.next = i2

    return mux3to1


@block
def tb1():
    i0 = Signal(intbv(0))
    i1 = Signal(intbv(0))
    sel = Signal(intbv(0))
    out = Signal(intbv(0))
    mux1 = mux_2to1(i0, i1, sel, out)

    @instance
    def stimulus():
        print("i0 | i1 | sel | output")
        for i in range(20):
            i0.next, i1.next, sel.next = randrange(2), randrange(2), randrange(2)
            yield delay(10)
            print(" %s | %s  |  %s  | %s" % (bin(i0), bin(i1), bin(sel), bin(out)))

    return stimulus, mux1


@block
def tb2():
    i0 = Signal(intbv(0))
    i1 = Signal(intbv(0))
    i2 = Signal(intbv(0))
    sel = Signal(intbv(0))
    out = Signal(intbv(0))
    mux = mux_3to1(i0, i1, i2, sel, out)

    @instance
    def stimulus():
        print("i0 | i1 | i2 | sel | out")
        for i in range(20):
            i0.next, i1.next, i2.next, sel.next = randrange(2), randrange(2), randrange(2), randrange(4)
            yield delay(10)
            print(" %s |  %s | %s  | %s  | %s" % (i0, i1, i2, bin(sel, 2), out))

    return stimulus, mux


def convert_2to1():
    i0 = Signal(intbv(0)[1:])
    i1 = Signal(intbv(0)[1:])
    sel = Signal(intbv(0)[1:])
    out = Signal(intbv(0)[1:])
    mux1 = mux_2to1(i0, i1, sel, out)
    mux1.convert(hdl='Verilog')


def convert_3to1():
    i0 = Signal(intbv(0)[1:])
    i1 = Signal(intbv(0)[1:])
    i2 = Signal(intbv(0)[1:])
    sel = Signal(intbv(0)[2:])
    out = Signal(intbv(0)[1:])
    mux = mux_3to1(i0, i1, i2, sel, out)
    mux.convert(hdl='Verilog')


tb1 = tb1()
tb1.run_sim()
print("------------------------------------------")
tb2 = tb2()
tb2.run_sim()
convert_2to1()
convert_3to1()