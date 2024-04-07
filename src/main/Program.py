import UserInput as inp
import Initialize as init
import Calculations as calc
import BuildProcedure as bp
import MiscOperations as mo
import Value as val
import WriteCoordinates as wc
import copy

""" Functions for generating g-code file for entire procedure via command line or GUI """


def commandline():
    """ builds procedure file via command line, and displays active tips and reservoir volumes"""

    # Prompt user for preferences
    name = inp.get_procedure_name()
    plate = inp.get_plate_type()
    insert = inp.get_insert_type(plate)
    res_type = inp.get_reservoir_type()
    tip_size = inp.get_tip_type()
    design = inp.get_design()
    if res_type != val.res_25mL:
        equip = inp.get_equip()
    else:
        equip = False
    eject = inp.get_eject()

    # Calculate number of reservoirs, tips and starting res volumes
    rnum = calc.num_reservoir(design, res_type)
    tnum = calc.num_tip(design)
    r_vol = calc.vol_per_res(design, res_type)
    res_vol = copy.deepcopy(r_vol)

    # Write initialization comments to file
    init.initialization(name, res_type, rnum, tip_size, tnum, plate, insert)
    mo.present(name)
    wc.dwell(name, 60)

    # Equip Tips
    if equip:
        mo.equip(name)

    # Aspirate and Dispense
    bp.build_procedure(name, r_vol, insert, tip_size, design, res_type)

    # EJect Tips
    if eject:
        for i in range(2):
            mo.eject(name, i)

    # Present Stage/End Procedure
    mo.present(name)
    print("File successfully generated!")

    # Display Tip, Reservoir, and machine loading information


def gui(name: str, plate_inp, insert, restype_inp, tip_size, design, equip, eject):
    """ builds procedure file via GUI, and returns reservoir volumes

    :param name: name of file to write to
    :param plate_inp: Type of culture plate
    :param insert: Type of insert used for procedure
    :param restype_inp: Type of reservoir used for procedure
    :param tip_size: max volume of tip
    :param design: Volumetric design of plate
    :param equip: If tips are equipped
    :param eject: If tips are ejected
    :return: Starting minimum reservoir volumes
    """

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

    # Calculate number of reservoirs, tips and starting res volumes
    rnum = calc.num_reservoir(design, res_type)
    tnum = calc.num_tip(design)
    r_vol = calc.vol_per_res(design, res_type)
    res_vol = copy.deepcopy(r_vol)

    # Write initialization comments to file
    init.initialization(name, res_type, rnum, tip_size, tnum, plate, insert)
    mo.present(name)
    wc.dwell(name, 60)

    # Equip Tips
    if equip:
        mo.equip(name)

    # Aspirate and Dispense
    bp.build_procedure(name, r_vol, insert, tip_size, design, res_type)

    # EJect Tips
    if eject:
        for i in range(2):
            mo.eject(name, i)

    # Present Stage/End Procedure
    mo.present(name)

    # Return starting reservoir volumes (without dead volumes)
    return res_vol
