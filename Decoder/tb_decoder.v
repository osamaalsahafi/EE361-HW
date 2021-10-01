module tb_decoder;

reg [0:0] i0;
reg [0:0] i1;
wire [0:0] d0;
wire [0:0] d1;
wire [0:0] d2;
wire [0:0] d3;

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
