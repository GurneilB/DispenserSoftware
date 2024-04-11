import xml.etree.ElementTree as ET
""" Values related to the program's operation. Includes calibrated positions"""

# Coordinate Types
plate_96 = "96 Well Plate"
plate_6 = "6 Well Plate"
reservoir_25ml = "25 mL Reservoir"
_1_5_tubes = "1.5 mL Reservoirs"
tip_tray = "Tip Tray"
pos_eject_bowl = "Ejection Bowl"
cal_1_5_tubes = "1.5 mL Reservoirs (Testing)"

# Insert Types
ez_seed = "EZ-SEED"
three_in_one = "3-IN-1"

# Protocol Identifiers
_4_tip_96well_protocol = 0
_2_tip_96well_protocol = 1
_1_tip_6well_protocol = 2
_2_tip_6well_protocol = 3

# Tip and Reservoir volumes
_5mL = 5000.000
_1_5mL = 1500.000
_25mL = 25000.000
_250uL_tip = 250

# tree = ET.parse("calibration_values.xml")
# root = tree.getroot()

# 96 Well Plate Coordinates
_96_well_coordinates =[125,21] # [int(root.find(plate_96).attrib['x']), int(root.find(plate_96).attrib['y'])]
_96_well_movement_height = 30 #int(root.find(plate_96).attrib['z_movement'])
ez_dispense_height = 40 #int(root.find(plate_96).attrib['z']) - 3
_96_well_dispense_height = 40 #int(root.find(plate_96).attrib['z'])

# 6 Well Plate Coordinates
_6_well_coordinates = [101, 0]  # Not Calibrated
_6_well_movement_height = 0  # Not Calibrated
dispense_height_3in1 = 0  # Not Calibrated
dispense_height_6 = 0  # Not Calibrated

# 25 mL Reservoir Coordinates
pos_reservoir_25ml = [6, 49]
aspirate_height_25ml = 45
movement_height_25mL = 18

# 1.5 mL Reservoir Coordinates
tubes4tips = [[11, 104], [47, 104]]  # Not calibrated
tubes2tips = [[11, 104], [47, 104], [2, 117], [38, 117]]  # Not Calibrated
aspirate_height_1_5ml = 51  # Not Calibrated
movement_height_1_5ml = 43  # Not Calibrated

# Ejection Coordinates
eject_bowl = [5, 108]
eject_height = 66

# Presenting Coordinates
present = [65, 0]
present_height = 0

# Equipping Coordinates
tip_tray_8 = [65, 0]  # Not Calibrated
equip_height = 0  # Not Calibrated

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
beaker = [23.5, 61]
beaker_asp_height = 55
cal_tubes8 = [[9, 104], [27, 104], [45, 104], [72, 104],
              [0, 117], [18, 117], [36, 117], [54, 117]]  # Coordinates for 1-Tip dispensing
cal_tubes4 = [[10, 104], [46, 104], [37, 117],[1, 117]]  # Coordinates for 2-Tip dispensing
cal_tubes2 = [[11, 101], [2,114]]  # Coordinates for 4-Tip dispensing
tubes_disp_height = 78
cal_movement_height = 17
dispense_move_height = 41
zero_height = 0  # Find height, set manually with G92 E

# Calibration model dispensing factor
model_factor = 0.163

# New Calibration Coordinates
cal_25_pos_new = [0, 116]
cal_tubes_new = [[11, 101], [2,114]]

