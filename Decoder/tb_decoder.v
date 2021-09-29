module tb_decoder;

reg i0;
reg i1;
wire d0;
wire d1;
wire d2;
wire d3;

initial begin
    $from_myhdl(
        i0,
        i1
    );
    $to_myhdl(
        d0,
        d1,
        d2,
        d3
    );
end

decoder dut(
    i0,
    i1,
    d0,
    d1,
    d2,
    d3
);

endmodule
