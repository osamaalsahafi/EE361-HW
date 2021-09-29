import random
from myhdl import always_comb, block, intbv, Signal, instance, delay, instances,\
    bin

random.seed(13)
randrange = random.randrange


@block
def alu(a, b, sel, output):
    @always_comb
    def alu():

        if sel == 0:
            output.next = a + b
        elif sel == 1:
            output.next = a - b
        elif sel == 2:
            output.next = a & b
        elif sel == 3:
            output.next = a | b
        else:
            output.next = a ^ b

    return alu

@block
def testbench():
    sel = Signal(intbv(0)[3:])
    a = Signal(intbv(0)[3:])
    b = Signal(intbv(0)[3:])
    out = Signal(intbv(0).signed())
    ins = alu(a, b, sel, out)
    operation = ""

    @instance
    def stimulus():
        print("A   ,  B  = Out | selection")
        for i in range(20):
            a.next, b.next, sel.next = randrange(7), randrange(7), randrange(4)

            yield delay(1)
            operation = ""
            if sel == 0:
                operation = "Add"
            elif sel == 1:
                operation = "Sub"
            elif sel == 2:
                operation = "AND"
            elif sel == 3:
                operation = "OR"
            else:
                operation = "XOR"
            yield delay(10)
            print(("%s , %s = %s  |   " + operation) % (bin(a, 3), bin(b, 3), bin(out, 3)))
            yield delay(10)

    return instances()


def convert():
    sel = Signal(intbv(0)[3:])
    a = Signal(intbv(0)[3:])
    b = Signal(intbv(0)[3:])
    out = Signal(intbv(0)[3:0])
    ins = alu(a, b, sel, out)
    ins.convert(hdl='Verilog')


tb = testbench()
tb.run_sim()
convert()
