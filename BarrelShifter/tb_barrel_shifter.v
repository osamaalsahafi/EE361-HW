module tb_barrel_shifter;

wire [11:0] load_value;
reg [11:0] load_input;
reg [2:0] shift_reg;

initial begin
    $from_myhdl(
        load_input,
        shift_reg
    );
    $to_myhdl(
        load_value
    );
end

barrel_shifter dut(
    load_value,
    load_input,
    shift_reg
);

endmodule
