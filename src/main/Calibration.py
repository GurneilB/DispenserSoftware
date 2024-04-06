import WriteCoordinates as wc
import Value as val
import Initialize as init
import MiscOperations as mc

displacement = float(input("Enter the displacement in mm: "))
file_name = "Calibration"

with open("%s.gcode" % file_name, "w") as file:
    file.write(";Calibration")

# Absolute positioning
init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height)

for i in range(2):
    init.set_absolute(file_name)

    # Move to reservoir
    wc.rapid_e_pos(file_name, val.zero_height)
    wc.rapid_z_pos(file_name, val.movement_height_25mL)
    wc.rapid_xy_pos(file_name, val.pos_reservoir_25ml)

    # Aspirate
    wc.rapid_z_pos(file_name, val.aspirate_height_25ml)
    init.set_relative(file_name)
    for j in range(2):
        init.pick_tool(file_name, val.ez_seed, j)
        wc.rapid_e_pos(file_name, displacement)

    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.movement_height_25mL)
    wc.rapid_xy_pos(file_name, val.cal_tubes2[i])

    # Dispense
    wc.rapid_z_pos(file_name, val.tubes_disp_height)
    init.set_relative(file_name)
    for j in range(2):
        init.pick_tool(file_name, val.ez_seed, j)
        wc.rapid_e_pos(file_name, -displacement)


init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height)
mc.present(file_name)
