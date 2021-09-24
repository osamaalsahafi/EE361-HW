module tb_Counter;

wire [11:0] count;
reg enable;
reg clk;
reg reset;

initial begin
    $from_myhdl(
        enable,
        clk,
        reset
    );
    $to_myhdl(
        count
    );
end

Counter dut(
    count,
    enable,
    clk,
    reset
);

endmodule
