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
wc.rapid_e_pos(file_name, val.zero_height)

# For 4-tip calibration with 25mL Reservoir (Aspirate) and 1.5 mL tubes (Dispense)
for i in range(4):
    init.set_absolute(file_name)

    # Move to reservoir
    wc.rapid_e_pos(file_name, val.zero_height)
    wc.rapid_z_pos(file_name, val.cal_movement_height)
    wc.rapid_xy_pos(file_name, val.beaker)

    # Aspirate according to displacement
    wc.rapid_z_pos(file_name, val.beaker_asp_height)
    init.set_relative(file_name)
    init.pick_tool(file_name, val.ez_seed)
    wc.rapid_e_pos(file_name, volume * factor)

    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.cal_movement_height)
    wc.rapid_xy_pos(file_name, val.cal_tubes4[i])

    # Dispense according to displacement
    wc.rapid_z_pos(file_name, val.tubes_disp_height)
    init.set_relative(file_name)
    init.pick_tool(file_name, val.ez_seed)
    wc.rapid_e_pos(file_name, -volume * factor)

# Present
init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height)
mc.present(file_name)
