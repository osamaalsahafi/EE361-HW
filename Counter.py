from myhdl import block, always_seq

@block
def inc(count, enable, clk, reset):
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
