import WriteCoordinates as wc
import Initialize as init
import Calculations as calc
import Value as val
import Aspiration as asp
import numpy as np

""" Functions related to generating G-Code dispensing commands for 4 tips and 2 tips within 96-well plate 
with HT-Sphere or no insert. (6-well and 3-in-1 unsupported)."""


def ez_4tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, restype, insert=val.ez_seed):
    """
    Writes EZ-Seed dispensing commands to file for 4-tip dispensing

    :param name: name of file to write to
    :param r_vol: volume of reagent in reservoirs
    :param tip: max volume of tip
    :param vol_array: Volumetric design of plate
    :param t_vol: Current volume of reagent in tip
    :param restype: Type of reservoir used in procedure
    :param insert: type of plate insert
    """

    # Build List of dispensing volumes
    path0 = vol_array[:, [-2, -1]]
    path1 = vol_array[:, [2, 3]]
    snake0 = calc.build_snake(path0)
    snake1 = calc.build_snake(path1)
    snake = [snake0, snake1]

    init.set_disp(name)

    # Move to dispensing start point
    wc.rapid_xy_pos(name, val._96_well_coordinates, "Move to 96 well plate")

    # Dispense volumes for each well
    for i in range(len(snake0)):

        # Proceed to next non-zero well
        if snake[0][i] == 0 and snake[1][i] == 0:
            continue

        # Move to dispense height
        wc.rapid_z_pos(name, val.ez_dispense_height, "Dispense Height at well %d" % i)
        init.set_relative(name)

        # Dispense Reagent for both tools
        for j in range(2):
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[j][i]), "Dispense %.1f uL" % snake[j][i])
            t_vol[j] = t_vol[j] - snake[j][i]

        init.set_absolute(name)

        # End procedure at the final well
        if i == 23:
            break

        # Find next non-zero well
        k = i + 1
        for k in range(i + 1, len(snake[0])):
            if snake[0][k] != 0:
                k = k
                break

        m = i + 1
        for m in range(i + 1, len(snake[1])):
            if snake[1][m] != 0:
                m = m
                break

        # Aspirate more reagent if current tip volume is too low for next non-zero well, move to next well
        if min(snake[0][k], snake[1][m]) > t_vol[0]:
            if min(k, m) < 12:
                pos = [val._96_well_coordinates[val.x], val._96_well_coordinates[val.y] + (min(k, m) * 9)]
            else:
                pos = [val._96_well_coordinates[val.x] + 9, val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)]
            asp.asp_4tip(name, r_vol, insert, tip, restype, t_vol, disp_pos=pos)
            init.set_disp(name)

        # Move to next unfilled non-zero well
        elif min(k, m) < 12:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x], val._96_well_coordinates[val.y] + (min(k, m) * 9)],
                            "Move to next well")
        else:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] + 9, val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)],
                            "Move to next well")


def n_ez_4tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, restype, insert=val.ez_seed):
    """
    Writes 96-well plate dispensing commands to file for 4-tip dispensing

    :param name: name of file to write to
    :param r_vol: volume of reagent in reservoirs
    :param tip: max volume of tip
    :param vol_array: Volumetric design of plate
    :param t_vol: Current volume of reagent in tip
    :param restype: Type of reservoir used in procedure
    :param insert: type of plate insert
    """

    # Build List of dispensing volumes
    path0 = vol_array[:, [-2, -1]]
    path1 = vol_array[:, [2, 3]]
    snake0 = calc.build_snake(path0)
    snake1 = calc.build_snake(path1)
    snake = [snake0, snake1]

    # Move to dispensing start point
    wc.rapid_xy_pos(name, val._96_well_coordinates, "Move to 96-well plate")

    # Dispense volumes for each well
    for i in range(len(snake0)):

        # Proceed to next non-zero well
        if snake[0][i] == 0 and snake[1][i] == 0:
            continue

        # Move to dispense height
        wc.rapid_z_pos(name, val._96_well_dispense_height, "Dispense Height at well %d" % i)
        init.set_relative(name)

        # Dispense Reagent for both tools
        for j in range(2):
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[j][i]), "Dispense %.1f uL" % snake[j][i])
            t_vol[j] = t_vol[j] - snake[j][i]

        init.set_absolute(name)

        # End procedure at the final well
        if i == 23:
            break

        # Find next non-zero well
        k = i + 1
        for k in range(i + 1, len(snake[0])):
            if snake[0][k] != 0:
                k = k
                break

        m = i + 1
        for m in range(i + 1, len(snake[1])):
            if snake[1][m] != 0:
                m = m
                break

        # Aspirate more reagent if current tip volume is too low for next non-zero well, move to next well
        if min(snake[0][k], snake[1][m]) > t_vol[0]:
            if min(k, m) < 12:
                pos = [val._96_well_coordinates[val.x], val._96_well_coordinates[val.y] + (min(k, m) * 9)]
            else:
                pos = [val._96_well_coordinates[val.x] + 9, val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)]
            asp.asp_4tip(name, r_vol, insert, tip, restype, t_vol, disp_pos=pos)
            init.set_disp(name)

        # Move to next unfilled non-zero well
        elif min(k, m) < 12:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x], val._96_well_coordinates[val.y] + (min(k, m) * 9)],
                            "Move to next well")
        else:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] + 9, val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)],
                            "Move to next well")


def ez_2tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, restype, insert=val.ez_seed):
    """
        Writes EZ-Seed dispensing commands to file for 2-tip dispensing

        :param name: name of file to write to
        :param r_vol: volume of reagent in reservoirs
        :param tip: max volume of tip
        :param vol_array: Volumetric design of plate
        :param t_vol: Current volume of reagent in tip
        :param restype: Type of reservoir used in procedure
        :param insert: type of plate insert
        """

    # Build List of dispensing volumes
    path0 = vol_array[:, [4, 5, 6, 7]]
    path1 = vol_array[:, [0, 1, 2, 3]]
    snake0 = calc.build_snake(path0)
    snake1 = calc.build_snake(path1)
    snake = [snake0, snake1]

    # Move to dispensing start point
    wc.rapid_xy_pos(name, val._96_well_coordinates, "Move to 96-well plate")

    # Write dispensing comment to file
    init.set_disp(name)

    # Dispense volumes for each well
    for i in range(len(snake0)):

        # Proceed to next non-zero well
        if snake[0][i] == 0 and snake[1][i] == 0:
            continue

        # Move to dispense height
        wc.rapid_z_pos(name, val.ez_dispense_height, "Dispense Height at well %d" % i)
        init.set_relative(name)

        # Dispense Reagent for both tools
        for j in range(2):
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[j][i]), "Dispense %.1f uL" % snake[j][i])
            t_vol[j] = t_vol[j] - snake[j][i]

        init.set_absolute(name)

        # End procedure at the final well
        if i == 47:
            break

        # Find next non-zero well
        k = i + 1
        for k in range(i + 1, len(snake[0])):
            if snake[0][k] != 0:
                k = k
                break

        m = i + 1
        for m in range(i + 1, len(snake[1])):
            if snake[1][m] != 0:
                m = m
                break

        # Aspirate more reagent if current tip volume is too low for next non-zero well, move to next well
        if min(snake[0][k], snake[1][m]) > t_vol[0]:
            if min(k, m) < 12:
                pos = [val._96_well_coordinates[val.x] - (2 * 9), val._96_well_coordinates[val.y] + (min(k, m) * 9)]
            elif 12 <= min(k, m) < 24:
                pos = [val._96_well_coordinates[val.x] - (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)]
            elif 24 <= min(k, m) < 36:
                pos = [val._96_well_coordinates[val.x] + (0 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 35) * 9)]
            else:
                pos = [val._96_well_coordinates[val.x] + (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 47) * 9)]
            asp.asp_2tip(name, r_vol, insert, tip, restype, t_vol, disp_pos=pos)
            init.set_disp(name)

        # Move to next unfilled non-zero well
        elif min(k, m) < 12:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x], val._96_well_coordinates[val.y] + (min(k, m) * 9)],
                            "Move to next well")
        elif 12 <= min(k, m) < 24:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] - (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)],
                            "Move to next well")
        elif 24 <= min(k, m) < 36:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] + (0 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 35) * 9)],
                            "Move to next well")
        else:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] + (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 47) * 9)],
                            "Move to next well")


def n_ez_2tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, restype, insert=val.ez_seed):
    """
            Writes 96-well Plate dispensing commands to file for 2-tip dispensing

            :param name: name of file to write to
            :param r_vol: volume of reagent in reservoirs
            :param tip: max volume of tip
            :param vol_array: Volumetric design of plate
            :param t_vol: Current volume of reagent in tip
            :param restype: Type of reservoir used in procedure
            :param insert: type of plate insert
            """

    # Build List of dispensing volumes
    path0 = vol_array[:, [4, 5, 6, 7]]
    path1 = vol_array[:, [0, 1, 2, 3]]
    snake0 = calc.build_snake(path0)
    snake1 = calc.build_snake(path1)
    snake = [snake0, snake1]

    # Move to dispensing start point
    wc.rapid_xy_pos(name, val._96_well_coordinates, "Move to 96-well plate")

    # Write dispensing comment to file
    init.set_disp(name)

    # Dispense volumes for each well
    for i in range(len(snake0)):

        # Proceed to next non-zero well
        if snake[0][i] == 0 and snake[1][i] == 0:
            continue

        # Move to dispense height
        wc.rapid_z_pos(name, val.ez_dispense_height, "Dispense Height at well %d" % i)
        init.set_relative(name)

        # Dispense Reagent for both tools
        for j in range(2):
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[j][i]), "Dispense %.1f uL" % snake[j][i])
            t_vol[j] = t_vol[j] - snake[j][i]

        init.set_absolute(name)

        # End procedure at the final well
        if i == 47:
            break

        # Find next non-zero well
        k = i + 1
        for k in range(i + 1, len(snake[0])):
            if snake[0][k] != 0:
                k = k
                break

        m = i + 1
        for m in range(i + 1, len(snake[1])):
            if snake[1][m] != 0:
                m = m
                break

        # Aspirate more reagent if current tip volume is too low for next non-zero well, move to next well
        if min(snake[0][k], snake[1][m]) > t_vol[0]:
            if min(k, m) < 12:
                pos = [val._96_well_coordinates[val.x] - (2 * 9), val._96_well_coordinates[val.y] + (min(k, m) * 9)]
            elif 12 <= min(k, m) < 24:
                pos = [val._96_well_coordinates[val.x] - (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)]
            elif 24 <= min(k, m) < 36:
                pos = [val._96_well_coordinates[val.x] + (0 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 35) * 9)]
            else:
                pos = [val._96_well_coordinates[val.x] + (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 47) * 9)]
            asp.asp_2tip(name, r_vol, insert, tip, restype, t_vol, disp_pos=pos)
            init.set_disp(name)

        # Move to next unfilled non-zero well
        elif min(k, m) < 12:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x], val._96_well_coordinates[val.y] + (min(k, m) * 9)],
                            "Move to next well")
        elif 12 <= min(k, m) < 24:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] - (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 23) * 9)],
                            "Move to next well")
        elif 24 <= min(k, m) < 36:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] + (0 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 35) * 9)],
                            "Move to next well")
        else:
            wc.rapid_z_pos(name, val._96_well_movement_height, "Move height")
            wc.rapid_xy_pos(name, [val._96_well_coordinates[val.x] + (1 * 9), val._96_well_coordinates[val.y] + ((-min(k, m) + 47) * 9)],
                            "Move to next well")


"""WRITE CODE HERE FOR n_three_in_one_2tip_dispense, three_in_one_2tip_dispense, n_three_in_one_1tip_dispense, 
three_in_one_1tip_dispense, (Or however it makes sense to write logarithm)"""
