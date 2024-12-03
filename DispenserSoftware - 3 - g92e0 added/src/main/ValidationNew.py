import WriteCoordinates as wc
import Value as val
import Initialize as init
import MiscOperations as mc

""" Generate new wet validation commands """

# Get dispensing model factor, and desired volume to be dispensed
factor = float(input("Enter the model factor: "))
volume = int(input("Enter the dispensing volume (20ul - 200ul): "))
file_name = "Validation %d uL" % volume

# Generate Validation file
with open("%s.gcode" % file_name, "w") as file:
    file.write(";Validation")
    file.write(";FACTOR: %.3f" % factor)

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
    wc.rapid_z_pos(file_name, val.aspirate_height_25ml, "Aspirate height")
    init.set_relative(file_name)
    for j in range(2):
        init.pick_tool(file_name, val.ez_seed, j)
        wc.rapid_e_pos(file_name, volume * factor, "Aspirate %.1f uL" % (volume*factor))

    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.cal_movement_height, "Move height")
    wc.rapid_xy_pos(file_name, val.cal_tubes_new[i], "Move to tubes")

    # Dispense according to displacement
    wc.rapid_z_pos(file_name, val.tubes_disp_height, "Dispense height")
    init.set_relative(file_name)
    for j in range(2):
        init.pick_tool(file_name, val.ez_seed, j)
        wc.rapid_e_pos(file_name, -volume * factor, "Dispense %.1f uL" % (volume*factor))

# Present
init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height, "Set Extruder to 0")
mc.present(file_name)
