import WriteCoordinates as wc
import BuildProcedure as bp
import Value as val
import Initialize as init
import Exceptions as exp

v_range = (input("Low Medium or High Volume Validation? (L or M or H): ")).upper()
min_ = None
max_ = None

while True:
    try:
        if v_range == "L":
            volume = float(input("Enter the volume you want to dispense in uL (up to 50uL): "))
            min_ = 0
            max_ = 50
        if min_ <= volume <= max_:
            raise exp.OutOfRangeError(volume, min_, max_)
    except exp.OutOfRangeError as e:
        print(e)


factor = float(input("Enter the model factor: "))
file_name = "Validation"

with open("%s.gcode" % file_name, "w") as file:
    file.write(";Validation")

# Absolute positioning, Pick tool 0
init.set_absolute(file_name)
init.pick_tool(file_name, "EZ-Seed")

# Move to beaker
wc.rapid_e_pos(file_name, val.zero_height)
wc.rapid_z_pos(file_name, val.cal_movement_height)
wc.rapid_xy_pos(file_name, val.beaker)

# Aspirate
wc.rapid_z_pos(file_name, val.beaker_asp_height)
init.set_relative(file_name)
wc.rapid_e_pos(file_name, volume * factor * 4)

for i in range(4):
    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.dispense_move_height)
    wc.rapid_xy_pos(file_name, val.cal_tubes4[i])

    # Dispense
    wc.rapid_z_pos(file_name, val.tubes_disp_height)
    init.set_relative(file_name)
    wc.rapid_e_pos(file_name, -volume * factor)

init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height)
bp.present(file_name)
