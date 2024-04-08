import WriteCoordinates as wc
import MiscOperations as mo
import Value as val
import Initialize as init

"""  Generate wet validation commands """

# v_range = (input("Low Medium or High Volume Validation? (L or M or H): ")).upper()
# min_ = None
# max_ = None
#
# while True:
#     try:
#         if v_range == "L":
#             volume = float(input("Enter the volume you want to dispense in uL (up to 50uL): "))
#             min_ = 0
#             max_ = 50
#         if min_ <= volume <= max_:
#             raise exp.OutOfRangeError(volume, min_, max_)
#     except exp.OutOfRangeError as e:
#         print(e)


# Get dispensing model factor, and desired volume to be dispensed
factor = float(input("Enter the model factor: "))
volume = float(input("Enter the dispensing volume (20ul - 50ul): "))
file_name = "Validation"

# Generate Validation file
with open("%s.gcode" % file_name, "w") as file:
    file.write(";Validation")

# Build procedure

# Absolute positioning,
init.set_absolute(file_name)

# Move to reservoir
wc.rapid_e_pos(file_name, val.zero_height)
wc.rapid_z_pos(file_name, val.cal_movement_height)
wc.rapid_xy_pos(file_name, val.beaker)

# Aspirate
wc.rapid_z_pos(file_name, val.beaker_asp_height)
init.set_relative(file_name)
init.pick_tool(file_name, val.ez_seed)
wc.rapid_e_pos(file_name, volume * factor * 4)

init.set_absolute(file_name)
wc.rapid_z_pos(file_name, val.cal_movement_height)
wc.rapid_xy_pos(file_name, val.cal_tubes4[0])

for i in range(4):
    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.dispense_move_height)
    wc.rapid_xy_pos(file_name, val.cal_tubes4[i])

    wc.rapid_z_pos(file_name, val.tubes_disp_height)
    init.set_relative(file_name)
    wc.rapid_e_pos(file_name, -volume * factor)

# End procedure
init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height)
mo.present(file_name)
