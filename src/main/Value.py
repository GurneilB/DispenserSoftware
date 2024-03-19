# Protocol Identifiers
tip4_96 = 0
tip2_96 = 1
tip1_6 = 2
tip2_6 = 3

# Insert Types
ez_seed = "EZ-SEED"
three_in_one = "3-IN-1"

# Tip and Reservoir volumes
tube_5mL = 5000.000
tube_1500uL = 1500.000
res_25mL = 25000.000
tip_250 = 250

# 96 Well Plate Coordinates
plate_96 = [125, 20]
plate96_movement_height = 49
dispense_height_EZ = 53
dispense_height_96 = None

# 6 Well Plate Coordinates
plate_6 = []
plate6_movement_height = None
dispense_height_3in1 = None
dispense_height_6 = None

# 25 mL Reservoir Coordinates
pos_reservoir_25ml = [3, 58]
aspirate_height_25ml = 56
movement_height_25mL = 36

# 1.5 mL Reservoir Coordinates
tubes4tips = [[]]
tubes2tips = []
aspirate_height_1_5ml = None
movement_height_1_5ml = None

# Ejection Coordinates
eject_bowl = [5, 108]
eject_height = 66

# Presenting Coordinates
present = [65, 0]
present_height = 0

# Equipping Coordinates
tip_tray_8 = []
equip_height = None

# 96-well plate dimensions
dims_96 = (8, 12)

# Size of 96-well plate
zone_96 = 96

# Size of 6-well plate
zone_6 = 6

# No. of tips for dispensing
tip1 = 1
tip2 = 2
tip4 = 4

# No. of reservoirs
rnum1 = 1
rnum4 = 4
rnum8 = 8

# XY Indices
x = 0
y = 1

# Calibration and Testing Coordinates
beaker = [27.5, 61]
beaker_asp_height = 50
cal_tubes8 = [[9, 104], [27, 104], [45, 104], [72, 104],
              [0, 117], [18, 117], [36, 117], [54, 117]]  # Coordinates for 1-Tip dispensing
cal_tubes4 = [[11, 104], [47, 104], [2, 117], [38, 117]]  # Coordinates for 2-Tip dispensing
cal_tubes2 = [[]]  # Coordinates for 4-Tip dispensing
tubes_disp_height = 81
cal_movement_height = 17
dispense_move_height = 41
zero_height = 0  # Find height, set manually with G92 E

# Calibration model dispensing factor
model_factor = 1
