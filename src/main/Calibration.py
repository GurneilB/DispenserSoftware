import WriteCoordinates as wc
import Value as val
import Initialize as init
import MiscOperations as mc

""" Generate wet calibration commands """

# Get piston displacement value from user
displacement = int(input("Enter the displacement in mm: "))
file_name = "Calibration %d mm" % displacement

# Create Calibration File
with open("%s.gcode" % file_name, "w") as file:
    file.write(";Calibration")

# Build File

# Absolute positioning
init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height, "Set Extruder to 0")

# For 4-tip calibration with 25mL Reservoir (Aspirate) and 1.5 mL tubes (Dispense)
for i in range(2):
    init.set_absolute(file_name)

    # Move to reservoir
    wc.rapid_e_pos(file_name, val.zero_height, "Set Extruder to 0")
    wc.rapid_z_pos(file_name, val.movement_height_25mL, "Move height")
    wc.rapid_xy_pos(file_name, val.pos_reservoir_25ml, "Move to 25mL reservoir")

    # Aspirate according to displacement
    wc.rapid_z_pos(file_name, val.aspirate_height_25ml, "Aspiration height")
    init.set_relative(file_name)
    for j in range(2):
        init.pick_tool(file_name, val.ez_seed, j)
        wc.rapid_e_pos(file_name, displacement, "Aspirate %.1f mm" % displacement)

    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.cal_movement_height, "Move height")
    wc.rapid_xy_pos(file_name, val.cal_tubes_new[i], "Move to 1.5mL tubes")

    # Dispense according to displacement
    wc.rapid_z_pos(file_name, val.tubes_disp_height, "Dispensing height")
    init.set_relative(file_name)
    for j in range(2):
        init.pick_tool(file_name, val.ez_seed, j)
        wc.rapid_e_pos(file_name, -displacement, "Dispense %.1f mm" % displacement)

# Present
init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height, "Set extruder to 0")
mc.present(file_name)
