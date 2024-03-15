import src.main.WriteCoordinates as wc
import src.main.Initialize as init
import src.main.Calculations as calc
import src.main.Value as val
import numpy as np


# NOTE: *****Only supports 25mL reservoir******
def asp_4tip_25mL(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None, disp_pos=val.plate_96):
    """
    Writes Aspiration-related commands to G-code file

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


def asp_2tip_25mL(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None, disp_pos=val.plate_96):
    """
    Writes Aspiration-related commands to G-code file

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
