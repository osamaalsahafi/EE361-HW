module tb_register;

reg [31:0] load_in;
wire [31:0] load_out;
reg enable;
reg clock;
reg reset;

initial begin
    $from_myhdl(
        load_in,
        enable,
        clock,
        reset
    );
    $to_myhdl(
        load_out
    );
end

register dut(
    load_in,
    load_out,
    enable,
    clock,
    reset
);

endmodule
