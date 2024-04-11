import WriteCoordinates as wc
import Initialize as init
import Calculations as calc
import Value as val

""" Functions related to generating G-Code aspiration commands for 4 tips and 2 tips using 
25mL and 1.5mL reservoirs. (5mL Reservoir unsupported)."""


def asp_4tip_25ml(name: str, r_vol, insert: str, tip: int, t_vol=None, disp_pos=val._96_well_coordinates):
    """
    Writes 4-tip 25 mL reservoir aspiration-related commands to G-code file

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    :param t_vol: Current volume of reagent in tip
    :param disp_pos: Next XY dispensing position
    :return t_vol: Updated volume of reagent in tip
    """

    # Write aspiration comment to file, initialize t_vol if None
    if t_vol is None:
        t_vol = [0.0, 0.0]
    init.set_asp(name)

    # Set to absolute positioning
    init.set_absolute(name)

    # Travel to XYZ pos of reservoirs
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, val.pos_reservoir_25ml)
    wc.rapid_z_pos(name, val.aspirate_height_25ml)

    # Run aspiration for both motors
    for i in range(2):

        # Pick active tool
        init.pick_tool(name, insert, i)

        # Write aspiration command, change remaining reservoir volume

        # When reservoir volume is greater than remaining tip volume, fill tip to max
        if r_vol[i] >= (tip - t_vol[i]) * val.tip2:
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update r_vol
            r_vol[i] = r_vol[i] - ((tip - t_vol[i]) * val.tip2)

            # Update t_vol
            t_vol[i] = tip

        # When reservoir volume is less than remaining tip volume, aspirate remaining reagent
        else:
            # Set to relative positioning
            init.set_relative(name)

            # Aspirate Remaining Reagent
            wc.rapid_e_pos(name, calc.convert_vol(r_vol[i]) / 2)

            # Update t_vol
            t_vol[i] = t_vol[i] + r_vol[i] / 2

            # Update r_vol
            r_vol[i] = r_vol[i] - r_vol[i]

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_2tip_25ml(name: str, r_vol, insert: str, tip: int, t_vol=None, disp_pos=val._96_well_coordinates):
    """
    Writes 2-tip, 25mL reservoir aspiration-related commands to G-code file

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    :param t_vol: Current volume of reagent in tip
    :param disp_pos: Next XY dispensing position
    :return t_vol: Updated volume of reagent in tip
    """

    # Write aspiration comment to file, initialize t_vol if None
    if t_vol is None:
        t_vol = [0.0, 0.0]
    init.set_asp(name)

    # Set to absolute positioning
    init.set_absolute(name)

    # Travel to XYZ pos of reservoirs
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, val.pos_reservoir_25ml)
    wc.rapid_z_pos(name, val.aspirate_height_25ml)

    # Run aspiration for both motors
    for i in range(2):

        # Pick active tool
        init.pick_tool(name, insert, i)

        # Write aspiration command, change remaining reservoir volume

        # When reservoir volume is greater than remaining tip volume, fill tip to max
        if r_vol[i] >= (tip - t_vol[i]):
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update r_vol
            r_vol[i] = r_vol[i] - (tip - t_vol[i])

            # Update t_vol
            t_vol[i] = tip

        # When reservoir volume is less than remaining tip volume, aspirate remaining reagent
        else:
            # Set to relative positioning
            init.set_relative(name)

            # Aspirate Remaining Reagent
            wc.rapid_e_pos(name, calc.convert_vol(r_vol[i]))

            # Update t_vol
            t_vol[i] = t_vol[i] + r_vol[i]

            # Update r_vol
            r_vol[i] = r_vol[i] - r_vol[i]

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_4tip_1_5ml(name: str, r_vol, insert: str, tip: int, t_vol=None, disp_pos=val._96_well_coordinates):
    """
    Writes 4 tip, 1.5mL reservoir Aspiration-related commands to G-code file

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    :param t_vol: Current volume of reagent in tip
    :param disp_pos: Next XY dispensing position
    :return t_vol: Updated volume of reagent in tip
    """

    # Write aspiration comment to file, initialize t_vol if None
    if t_vol is None:
        t_vol = [0.0, 0.0]
    init.set_asp(name)

    # Set to absolute positioning
    init.set_absolute(name)

    # Travel to XYZ pos of reservoirs
    if r_vol[0] != 0:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes4tips[0])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 0

    else:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes4tips[1])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 4

    # Run aspiration for both motors
    for i in range(2):

        # Pick active tool
        init.pick_tool(name, insert, i)

        # Write aspiration command, change remaining reservoir volume

        # When reservoir volume is greater than remaining tip volume, fill tip to max
        if r_vol[k + (i * 2)] >= (tip - t_vol[i]):
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - (tip - t_vol[i])
            r_vol[k + 1 + (i * 2)] = r_vol[k + 1 + (i * 2)] - (tip - t_vol[i])

            # Update t_vol
            t_vol[i] = tip

        # When reservoir volume is less than remaining tip volume, aspirate remaining reagent
        else:
            init.set_relative(name)
            wc.rapid_e_pos(name, calc.convert_vol(r_vol[k + (i * 2)]))

            # Update t_vol
            t_vol[i] = t_vol[i] + r_vol[k + (i * 2)]

            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - r_vol[k + (i * 2)]
            r_vol[k + 1 + (i * 2)] = r_vol[k + 1 + (i * 2)] - r_vol[k + 1 + (i * 2)]

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_1_5ml)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_2tip_1_5ml(name: str, r_vol, insert: str, tip: int, t_vol=None, disp_pos=val._96_well_coordinates):
    """
    Writes 2 tip, 1.5mL reservoir Aspiration-related commands to G-code file

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    :param t_vol: Current volume of reagent in tip
    :param disp_pos: Next XY dispensing position
    :return t_vol: Updated volume of reagent in tip
    """

    # Write aspiration comment to file, initialize t_vol if None
    if t_vol is None:
        t_vol = [0.0, 0.0]
    init.set_asp(name)

    # Set to absolute positioning
    init.set_absolute(name)

    # Travel to XYZ pos of reservoirs
    if r_vol[1] != 0:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes4tips[0])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 1

    else:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes4tips[1])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 5

    # Run aspiration for both motors
    for i in range(2):

        # Pick active tool
        init.pick_tool(name, insert, i)

        # Write aspiration command, change remaining reservoir volume

        # When reservoir volume is greater than remaining tip volume, fill tip to max
        if r_vol[k + (i * 2)] >= tip - t_vol[i]:
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - tip - t_vol[i]

            # Update t_vol
            t_vol[i] = tip

        # When reservoir volume is less than remaining tip volume, aspirate remaining reagent
        else:
            init.set_relative(name)
            wc.rapid_e_pos(name, calc.convert_vol(r_vol[k + (i * 2)]))

            # Update t_vol
            t_vol[i] = t_vol[i] + r_vol[k + (i * 2)]

            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - r_vol[k + (i * 2)]

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_1_5ml)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_4tip(name: str, r_vol, insert: str, tip: int, restype, t_vol=None, disp_pos=val._96_well_coordinates):
    """
    Finds 4-Tip Aspiration function for appropriate reservoir in use

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    :param restype: Maximum volume of reservoir
    :param t_vol: Current volume of reagent in tip
    :param disp_pos: Next XY dispensing position
    :return t_vol: Updated volume of reagent in tip
    """

    if restype == val._25mL:
        return asp_4tip_25ml(name, r_vol, insert, tip, t_vol, disp_pos)
    else:
        return asp_4tip_1_5ml(name, r_vol, insert, tip, t_vol, disp_pos)


def asp_2tip(name: str, r_vol, insert: str, tip: int, restype, t_vol=None, disp_pos=val._96_well_coordinates):
    """
    Finds 2-Tip Aspiration function for appropriate reservoir in use

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    :param restype: Maximum volume of reservoir
    :param t_vol: Current volume of reagent in tip
    :param disp_pos: Next XY dispensing position
    :return t_vol: Updated volume of reagent in tip
    """

    if restype == val._25mL:
        return asp_2tip_25ml(name, r_vol, insert, tip, t_vol, disp_pos)
    else:
        return asp_2tip_1_5ml(name, r_vol, insert, tip, t_vol, disp_pos)
