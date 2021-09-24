module tb_inc;

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

inc dut(
    count,
    enable,
    clk,
    reset
);

endmodule
