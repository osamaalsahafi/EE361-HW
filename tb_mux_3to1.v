module tb_mux_3to1;

reg i0;
reg i1;
reg i2;
reg sel0;
reg sel1;
wire out;

initial begin
    $from_myhdl(
        i0,
        i1,
        i2,
        sel0,
        sel1
    );
    $to_myhdl(
        out
    );
end

mux_3to1 dut(
    i0,
    i1,
    i2,
    sel0,
    sel1,
    out
);

endmodule
