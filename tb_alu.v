module tb_alu;

reg [2:0] a;
reg [2:0] b;
reg [2:0] sel;
wire [2:0] output;

initial begin
    $from_myhdl(
        a,
        b,
        sel
    );
    $to_myhdl(
        output
    );
end

alu dut(
    a,
    b,
    sel,
    output
);

endmodule
