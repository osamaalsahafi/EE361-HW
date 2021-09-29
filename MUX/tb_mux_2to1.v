module tb_mux_2to1;

reg i0;
reg i1;
reg sel;
wire out;

initial begin
    $from_myhdl(
        i0,
        i1,
        sel
    );
    $to_myhdl(
        out
    );
end

mux_2to1 dut(
    i0,
    i1,
    sel,
    out
);

endmodule
