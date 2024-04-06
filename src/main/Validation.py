import WriteCoordinates as wc
import MiscOperations as  mo
import Value as val
import Initialize as init

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


factor = float(input("Enter the model factor: "))
volume = float(input("Enter the dispensing volume (20ul - 100ul): "))
file_name = "Validation"

with open("%s.gcode" % file_name, "w") as file:
    file.write(";Validation")

# Absolute positioning,
init.set_absolute(file_name)

# Move to reservoir
wc.rapid_e_pos(file_name, val.zero_height)
wc.rapid_z_pos(file_name, val.movement_height_25mL)
wc.rapid_xy_pos(file_name, val.cal_25_pos_new)

# Aspirate
wc.rapid_z_pos(file_name, val.aspirate_height_25ml)
init.set_relative(file_name)
for j in range(2):
    init.pick_tool(file_name, val.ez_seed, j)
    wc.rapid_e_pos(file_name, volume * factor * 2)

wc.rapid_z_pos(file_name, val.movement_height_25mL)
wc.rapid_xy_pos(file_name, val.cal_tubes_new[0])

for i in range(2):
    # Move to tubes
    init.set_absolute(file_name)
    wc.rapid_z_pos(file_name, val.dispense_move_height)
    wc.rapid_xy_pos(file_name, val.cal_tubes_new[i])

    # Dispense
    for j in range(2):
        wc.rapid_z_pos(file_name, val.tubes_disp_height)
        init.set_relative(file_name)
        wc.rapid_e_pos(file_name, -volume * factor)

init.set_absolute(file_name)
wc.rapid_e_pos(file_name, val.zero_height)
mo.present(file_name)
