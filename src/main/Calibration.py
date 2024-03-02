import WriteCoordinates as wc
import BuildProcedure as bp
import Value as val
import Initialize as init

displacement = float(input("Enter the displacement: "))
file_name = "Calibration"

with open("%s.gcode" % file_name, "w") as file:
    file.write(";Calibration")

# Absolute positioning, Pick tool 0
init.set_absolute(file_name)
init.pick_tool(file_name, "EZ-Seed")
wc.rapid_e_pos(file_name, val.zero_height)

for i in range(4):
    init.set_absolute(file_name)

    # Move to beaker
    wc.rapid_z_pos(file_name, val.cal_movement_height)
    wc.rapid_xy_pos(file_name, val.beaker)

    # Aspirate
    wc.rapid_z_pos(file_name, val.beaker_asp_height)
    init.set_relative(file_name)
    wc.rapid_e_pos(file_name, displacement)

    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.cal_movement_height)
    wc.rapid_xy_pos(file_name, val.tubes[i])

    # Dispense
    wc.rapid_z_pos(file_name, val.tubes_disp_height)
    init.set_relative(file_name)
    wc.rapid_e_pos(file_name, -displacement)


init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height)
bp.present(file_name)
