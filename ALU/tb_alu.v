module tb_alu;

reg [2:0] a;
reg [2:0] b;
reg [2:0] sel;
wire [2:0] out;

initial begin
    $from_myhdl(
        a,
        b,
        sel
    );
    $to_myhdl(
        out
    );
end

alu dut(
    a,
    b,
    sel,
    out
);

endmodule
