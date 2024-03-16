import src.main.WriteCoordinates as wc
import src.main.Initialize as init
import src.main.Calculations as calc
import src.main.Value as val
import numpy as np


def asp_4tip_25ml(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None, disp_pos=val.plate_96):
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

        # When reservoir volume is greater than total tip volume, aspirate total tip volume
        if r_vol[0] >= tip * val.tip4:
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update t_vol
            t_vol[i] = tip
            # Update r_vol
            r_vol[0] = r_vol[0] - (t_vol[i] * 2)

        # When reservoir volume is less than total tip volume, aspirate remaining reagent
        else:
            # Set to relative positioning
            init.set_relative(name)

            # Aspiration for second motor
            if i == 1:
                wc.rapid_e_pos(name, calc.convert_vol(r_vol[0]) / 2)

                # Update t_vol
                t_vol[i] = r_vol[0] / 2

                # Update r_vol
                r_vol[0] = r_vol[0] - r_vol[0]

            # Aspiration for first motor
            else:
                wc.rapid_e_pos(name, calc.convert_vol(r_vol[0] / 4))

                # Update t_vol
                t_vol[i] = r_vol[0] / 4

                # Update r_vol
                r_vol[0] = r_vol[0] - t_vol[i] * 2

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_2tip_25ml(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None, disp_pos=val.plate_96):
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

        # When reservoir volume is greater than total tip volume, aspirate total tip volume
        if r_vol[0] >= tip * val.tip2:
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update t_vol
            t_vol[i] = tip
            # Update r_vol
            r_vol[0] = r_vol[0] - (t_vol[i])

        # When reservoir volume is less than total tip volume, aspirate remaining reagent
        else:
            # Set to relative positioning
            init.set_relative(name)

            # Aspiration for second motor
            if i == 1:
                wc.rapid_e_pos(name, calc.convert_vol(r_vol[0]))

                # Update t_vol
                t_vol[i] = r_vol[0] / 2

                # Update r_vol
                r_vol[0] = r_vol[0] - r_vol[0]

            # Aspiration for first motor
            else:
                wc.rapid_e_pos(name, calc.convert_vol(r_vol[0] / 2))

                # Update t_vol
                t_vol[i] = r_vol[0] / 2

                # Update r_vol
                r_vol[0] = r_vol[0] - t_vol[i]

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_4tip_1_5ml(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None, disp_pos=val.plate_96):
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

        # When reservoir volume is greater than total tip volume, aspirate total tip volume
        if r_vol[k + (i * 2)] >= tip:
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update t_vol
            t_vol[i] = tip
            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - (t_vol[i])
            r_vol[k + 1 + (i * 2)] = r_vol[k + 1 + (i * 2)] - (t_vol[i])

        # When reservoir volume is less than total tip volume, aspirate remaining reagent
        else:
            init.set_relative(name)
            wc.rapid_e_pos(name, calc.convert_vol(r_vol[k + (i * 2)]))

            # Update t_vol
            t_vol[i] = r_vol[k + (i * 2)]

            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - r_vol[k + (i * 2)]
            r_vol[k + 1 + (i * 2)] = r_vol[k + 1 + (i * 2)] - r_vol[k + 1 + (i * 2)]

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_1_5ml)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_2tip_1_5ml(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None, disp_pos=val.plate_96):
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
    if r_vol[0] != 0:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes2tips[0])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 0

    elif r_vol[1] != 0:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes4tips[1])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 1

    elif r_vol[4] != 0:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes4tips[4])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 4

    else:
        wc.rapid_z_pos(name, val.movement_height_1_5ml)
        wc.rapid_xy_pos(name, val.tubes4tips[5])
        wc.rapid_z_pos(name, val.aspirate_height_1_5ml)
        k = 6

    # Run aspiration for both motors
    for i in range(2):

        # Pick active tool
        init.pick_tool(name, insert, i)

        # Write aspiration command, change remaining reservoir volume

        # When reservoir volume is greater than total tip volume, aspirate total tip volume
        if r_vol[k + (i * 2)] >= tip:
            init.set_absolute(name)
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update t_vol
            t_vol[i] = tip
            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - (t_vol[i])

        # When reservoir volume is less than total tip volume, aspirate remaining reagent
        else:
            init.set_relative(name)
            wc.rapid_e_pos(name, calc.convert_vol(r_vol[k + (i * 2)]))

            # Update t_vol
            t_vol[i] = r_vol[k + (i * 2)]

            # Update r_vol
            r_vol[k + (i * 2)] = r_vol[k + (i * 2)] - r_vol[k + (i * 2)]

    # Set to absolute positioning
    init.set_absolute(name)

    # Move to dispensing position
    wc.rapid_z_pos(name, val.movement_height_1_5ml)
    wc.rapid_xy_pos(name, disp_pos)

    return t_vol


def asp_4tip(name: str, r_vol: list[float], insert: str, tip: int, restype, t_vol=None, disp_pos=val.plate_96):
    if restype == val.res_25mL:
        return asp_4tip_25ml(name, r_vol, insert, tip, t_vol, disp_pos)
    else:
        return asp_4tip_1_5ml(name, r_vol, insert, tip, t_vol, disp_pos)


def asp_2tip(name: str, r_vol: list[float], insert: str, tip: int, restype, t_vol=None, disp_pos=val.plate_96):
    if restype == val.res_25mL:
        return asp_2tip_25ml(name, r_vol, insert, tip, t_vol, disp_pos)
    else:
        return asp_2tip_1_5ml(name, r_vol, insert, tip, t_vol, disp_pos)
