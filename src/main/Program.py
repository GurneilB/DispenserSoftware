import UserInput as inp
import Initialize as init
import Calculations as calc
import BuildProcedure as bp
import MiscOperations as mo
import Value as val
import WriteCoordinates as wc
import numpy as np


def commandline():
    name = inp.get_procedure_name()
    plate = inp.get_plate_type()
    insert = inp.get_insert_type(plate)
    res_type = inp.get_reservoir_type()
    tip_size = inp.get_tip_type()
    design = inp.get_design()

    # UPDATE THIS FUNCTION
    rnum = calc.num_reservoir(design, res_type)

    tnum = calc.num_tip(design)

    init.initialization(name, res_type, rnum, tip_size, tnum, plate, insert)
    r_vol = calc.vol_per_res(design, res_type)
    # mo.equip(name)
    bp.build_procedure(name, r_vol, insert, tip_size, design, res_type)

    for i in range(2):
        mo.eject(name, i)

    mo.present(name)

    print("File successfully generated!")


def gui(name: str, plate_inp, insert, restype_inp, tip_size, design, equip, eject):

    # Convert inputs to recognized variables

    plate = None
    res_type = None

    # Initialize Plate Size
    if plate_inp == "6 well plate":
        plate = val.zone_6
    elif plate_inp == "96 well plate":
        plate = val.zone_96

    # Initialize Reservoir type
    if restype_inp == "1.5":
        res_type = val.tube_1500uL
    elif plate_inp == "5":
        res_type = val.tube_5mL
    elif restype_inp == "25":
        res_type = val.res_25mL

    rnum = calc.num_reservoir(design, res_type)
    tnum = calc.num_tip(design)
    r_vol = calc.vol_per_res(design, res_type)

    init.initialization(name, res_type, rnum, tip_size, tnum, plate, insert)
    mo.present(name)
    wc.dwell(name,60)

    if equip:
        mo.equip(name)

    bp.build_procedure(name, r_vol, insert, tip_size, design, res_type)

    if eject:
        for i in range(2):
            mo.eject(name, i)

    mo.present(name)

    return r_vol


