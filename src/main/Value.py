import os.path
import xml.etree.ElementTree as ET
import ConfigCalibration as calval

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
ez_seed = "HT-Sphere"
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

""" COORDINATES AND CALIBRATION MODEL"""
if os.path.exists("calibration_values.xml"):
    tree = ET.parse("calibration_values.xml")
    root = tree.getroot()

    # 96 Well Plate Coordinates
    _96_well_coordinates = [float(root.find("plate_96").attrib['x']), float(root.find("plate_96").attrib['y'])]
    _96_well_movement_height = float(root.find("plate_96").attrib['z_movement'])
    ez_dispense_height = float(root.find("plate_96").attrib['z']) - 2
    _96_well_dispense_height = float(root.find("plate_96").attrib['z'])

    # 6 Well Plate Coordinates
    _6_well_coordinates = [float(root.find("plate_6").attrib['x']), float(root.find("plate_6").attrib['y'])]
    _6_well_movement_height = float(root.find("plate_6").attrib['z_movement'])
    dispense_height_3in1 = float(root.find("plate_6").attrib['z']) - 3
    dispense_height_6 = float(root.find("plate_6").attrib['z'])

    # 25 mL Reservoir Coordinates
    pos_reservoir_25ml = [float(root.find("pos_reservoir_25ml").attrib['x']),
                          float(root.find("pos_reservoir_25ml").attrib['y'])]
    aspirate_height_25ml = float(root.find("pos_reservoir_25ml").attrib['z'])
    movement_height_25mL = float(root.find("pos_reservoir_25ml").attrib['z_movement'])

    # Make sure the adjusted X value is always greater than 0
    x_value = float(root.find("tubes4tips").attrib['x'])
    adjusted_x = max(x_value - 6, 0)

    # 1.5 mL Reservoir Coordinates
    tubes4tips = [[float(root.find("tubes4tips").attrib['x']), 
                   float(root.find("tubes4tips").attrib['y'])],
                  [adjusted_x, float(root.find("tubes4tips").attrib['y']) + 13]]  # Not calibrated
    tubes2tips = [[float(root.find("tubes4tips").attrib['x']), 
                   float(root.find("tubes4tips").attrib['y'])],
                  [float(root.find("tubes4tips").attrib['x']) + 36, 
                   float(root.find("tubes4tips").attrib['y'])],
                  [float(root.find("tubes4tips").attrib['x']) - 9, 
                   float(root.find("tubes4tips").attrib['y']) + 13],
                  [float(root.find("tubes4tips").attrib['x']) + 27, 
                   float(root.find("tubes4tips").attrib['y']) + 13]]
    aspirate_height_1_5ml = float(root.find("tubes4tips").attrib['z'])
    movement_height_1_5ml = float(root.find("tubes4tips").attrib['z_movement'])

    # Ejection Coordinates
    eject_bowl = [float(root.find("eject_bowl").attrib['x']), int(root.find("eject_bowl").attrib['y'])]
    eject_height = float(root.find("eject_bowl").attrib['z'])

    # Equipping Coordinates
    tip_tray_8 = [float(root.find("tip_tray_8").attrib['x']), float(root.find("tip_tray_8").attrib['y'])]
    equip_height = float(root.find("tip_tray_8").attrib['z'])

    # Calibration Coordinates
    cal_tubes_new = calval.cal_tubes_new
    model_factor = calval.model_factor

else:
    # 96 Well Plate Coordinates
    _96_well_coordinates = calval.plate_96
    _96_well_movement_height = calval.plate96_movement_height
    ez_dispense_height = calval.dispense_height_EZ
    _96_well_dispense_height = calval.dispense_height_96

    # 6 Well Plate Coordinates
    _6_well_coordinates = calval.plate_6
    _6_well_movement_height = calval.plate6_movement_height
    dispense_height_3in1 = calval.dispense_height_3in1
    dispense_height_6 = calval.dispense_height_6

    # 25 mL Reservoir Coordinates
    pos_reservoir_25ml = calval.pos_reservoir_25ml
    aspirate_height_25ml = calval.aspirate_height_25ml
    movement_height_25mL = calval.movement_height_25mL

    # 1.5 mL Reservoir Coordinates
    tubes4tips = calval.tubes4tips
    tubes2tips = calval.tubes2tips
    aspirate_height_1_5ml = calval.aspirate_height_1_5ml
    movement_height_1_5ml = calval.movement_height_1_5ml

    # Ejection Coordinates
    eject_bowl = calval.eject_bowl
    eject_height = calval.eject_height

    # Equipping Coordinates
    tip_tray_8 = calval.tip_tray_8
    equip_height = calval.equip_height

    # Calibration Coordinates
    cal_tubes_new = calval.cal_tubes_new
    model_factor = calval.model_factor


# Presenting Coordinates
present = [65, 0]
present_height = 0

""" OLD CALIBRATION VALUES"""
# New Calibration Coordinates
cal_25_pos_new = [0, 116]

# Calibration and Testing Coordinates
beaker = [23.5, 61]
beaker_asp_height = 55
cal_tubes8 = [[9, 104], [27, 104], [45, 104], [72, 104],
              [0, 117], [18, 117], [36, 117], [54, 117]]  # Coordinates for 1-Tip dispensing
cal_tubes4 = [[10, 104], [46, 104], [37, 117], [1, 117]]  # Coordinates for 2-Tip dispensing
cal_tubes2 = [[11, 101], [2, 114]]  # Coordinates for 4-Tip dispensing
tubes_disp_height = 78
cal_movement_height = 17
dispense_move_height = 41
zero_height = 0  # Find height, set manually with G92 E
