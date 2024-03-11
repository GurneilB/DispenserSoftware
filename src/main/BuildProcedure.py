import src.main.WriteCoordinates as wc
import src.main.Initialize as init
import src.main.Calculations as calc
import src.main.Value as val
import numpy as np


# NOTE: *****Only supports 25mL reservoir******
def aspirate(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None, disp_pos=val.plate_96):
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

    # Set to relative positioning
    init.set_relative(name)

    # Run aspiration for both motors
    for i in range(2):

        # Pick active tool
        init.pick_tool(name, insert, i)

        # Write aspiration command, change remaining reservoir volume

        # When reservoir volume is greater than total tip volume, aspirate total tip volume
        if r_vol[0] >= tip * 4:
            wc.rapid_e_pos(name, calc.convert_vol(tip))

            # Update t_vol
            t_vol[i] = tip
            # Update r_vol
            r_vol[0] = r_vol[0] - (t_vol[i] * 2)

        # When reservoir volume is less than total tip volume, aspirate remaining reagent
        else:

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


def protocol0_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, insert="EZ-Seed"):
    """
    Writes Protocol 0 (1x4) Dispensing commands to file

    :param name: name of file to write to
    :param r_vol: volume of reagent in reservoirs
    :param tip: max volume of tip
    :param vol_array: Volumetric design of plate
    :param t_vol: Current volume of reagent in tip
    :param insert: type of plate insert
    """

    # Build List of dispensing volumes
    path = vol_array[:, [-2, -1]]
    snake = build_snake(path)

    # Move to dispensing start point
    init.set_absolute(name)
    wc.rapid_xy_pos(name, val.plate_96)

    # Dispense volumes for each well
    for i in range(len(snake)):

        # Proceed to next non-zero well
        if snake[i] == 0:
            continue

        # Move to dispense height
        init.set_absolute(name)
        wc.rapid_z_pos(name, val.dispense_height_EZ)
        init.set_relative(name)

        # Dispense Reagent for both tools
        for j in range(2):
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[i]))

        # End procedure at the final well
        if i == 23:
            break

        # Find next non-zero well
        k = i+1
        for k in range(i+1, len(snake)):
            if snake[k] != 0:
                k = k
                break

        # Aspirate more reagent if current tip volume is too low for next non-zero well
        if snake[k] > t_vol[0]:
            aspirate(name, r_vol, insert, tip, t_vol)
            init.set_disp(name)

        # Move to next unfilled non-zero well
        init.set_absolute(name)
        wc.rapid_z_pos(name, val.plate96_movement_height)
        if k < 12:
            wc.rapid_xy_pos(name, [val.plate_96[val.x], val.plate_96[val.y] + (k * 9)])
        else:
            wc.rapid_xy_pos(name, [val.plate_96[val.x] + 9, val.plate_96[val.y] + ((-k + 23) * 9)])


def build_procedure(name: str, r_vol: list, insert: str, tip: int, vol_array, t_vol):
    """

    :param name: name of file to write to
    :param r_vol: volume of reagent in reservoirs
    :param insert:
    :param tip: max volume of tip
    :param vol_array: Volumetric design of plate
    :param t_vol: Current volume of reagent in tip
    """

    # Write dispensing comment to file
    init.set_disp(name)

    # Run protocol 0 (1x4 dispensing)
    if calc.get_protocol(vol_array) == 0:
        protocol0_dispense(name, r_vol, tip, vol_array, t_vol)

    # Run protocol 1 (2x2 dispensing)
    elif calc.get_protocol(vol_array) == 1:

        # *****NOT DONE*******
        path_1 = vol_array[:, [-2, -1]]
        path_2 = vol_array[:, [0, 1]]
        wc.rapid_xy_pos(name, val.plate_96)

    # Run protocol 2 (2x1 dispensing)
    else:

        # *****NOT DONE*******
        path = vol_array


def build_snake(array):
    """
    Creates list of values in snake order, starting from top right of array
    moving column-wise towards the left.

    :param array: numpy array of values
    :return: list of values in snake order
    """
    snake = []
    num_rows = len(array)
    num_cols = len(array[0])

    for j in range(num_cols - 1, -1, -1):

        # Iterate through columns backwards
        if j % 2 != 0:
            for i in range(num_rows):

                # If the column index is odd, iterate down the column
                snake.append(array[i][j])
        else:
            for i in range(num_rows - 1, -1, -1):

                # If the column index is even, iterate up the column
                snake.append(array[i][j])
    return snake


def equip(name):
    """
    Writes tip-equipping commands to file

    :param name: name of file to write to
    """
    init.set_equip(name)
    init.set_absolute(name)
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, val.tip_tray_8)
    wc.rapid_z_pos(name, val.equip_height)
    wc.dwell(name, 2)
    wc.rapid_z_pos(name, val.movement_height_25mL)


def eject(name):
    """
    Writes tip-ejection commands to file

    :param name: name of file to write to
    """
    init.set_eject(name)
    init.set_absolute(name)
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, val.eject_bowl)
    wc.rapid_z_pos(name, val.eject_height)
    wc.rapid_e_pos(name, 0)
    wc.rapid_z_pos(name, val.movement_height_25mL)


def present(name):
    """
    Writes plate presenting commands to file

    :param name: name of file to write to
    """
    init.set_absolute(name)
    wc.rapid_z_pos(name, val.present_height)
    wc.rapid_xy_pos(name, val.present)
