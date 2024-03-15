import src.main.WriteCoordinates as wc
import src.main.Initialize as init
import src.main.Calculations as calc
import src.main.Value as val
import src.main.Aspiration as asp
import numpy as np


def ez_4tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, insert="EZ-Seed"):
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
    path0 = vol_array[:, [-2, -1]]
    path1 = vol_array[:, [2, 3]]
    snake0 = calc.build_snake(path0)
    snake1 = calc.build_snake(path1)
    snake = [snake0, snake1]

    # Move to dispensing start point
    wc.rapid_xy_pos(name, val.plate_96)

    # Dispense volumes for each well
    for i in range(len(snake0)):

        # Proceed to next non-zero well
        if snake[0][i] == 0 and snake[1][i] == 0:
            continue

        # Move to dispense height
        wc.rapid_z_pos(name, val.dispense_height_EZ)
        init.set_relative(name)

        # Dispense Reagent for both tools
        for j in range(2):
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[j][i]))
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
        if snake[min(k, m)] > t_vol[0]:
            if min(k, m) < 12:
                pos = [val.plate_96[val.x], val.plate_96[val.y] + (min(k, m) * 9)]
            else:
                pos = [val.plate_96[val.x] + 9, val.plate_96[val.y] + ((-min(k, m) + 23) * 9)]
            asp.aspirate(name, r_vol, insert, tip, t_vol, disp_pos=pos)
            init.set_disp(name)

        # Move to next unfilled non-zero well
        elif min(k, m) < 12:
            wc.rapid_z_pos(name, val.plate96_movement_height)
            wc.rapid_xy_pos(name, [val.plate_96[val.x], val.plate_96[val.y] + (min(k, m) * 9)])
        else:
            wc.rapid_z_pos(name, val.plate96_movement_height)
            wc.rapid_xy_pos(name, [val.plate_96[val.x] + 9, val.plate_96[val.y] + ((-min(k, m) + 23) * 9)])

def n_ez_4tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, insert="EZ-Seed"):
    return None

# *** FROM LINE 222 - UPDATE TO SNAKE 4 COLUMNS ****
# *** NOT YET COMPATIBLE WITH ASPIRATE FUNCTION (Aspirate acts like there are 4 tips) ***
def ez_2tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, insert="EZ-Seed"):
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
    path0 = vol_array[:, [4, 5, 6, 7]]
    path1 = vol_array[:, [0, 1, 2, 3]]
    snake0 = calc.build_snake(path0)
    snake1 = calc.build_snake(path1)
    snake = [snake0, snake1]

    # Move to dispensing start point
    wc.rapid_xy_pos(name, val.plate_96)

    # Dispense volumes for each well
    for i in range(len(snake0)):

        # Proceed to next non-zero well
        if snake[0][i] == 0 and snake[1][i] == 0:
            continue

        # Move to dispense height
        wc.rapid_z_pos(name, val.dispense_height_EZ)
        init.set_relative(name)

        # Dispense Reagent for both tools
        for j in range(2):
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[j][i]))
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
        if snake[min(k, m)] > t_vol[0]:
            if min(k, m) < 12:
                pos = [val.plate_96[val.x], val.plate_96[val.y] + (min(k, m) * 9)]
            else:
                pos = [val.plate_96[val.x] + 9, val.plate_96[val.y] + ((-min(k, m) + 23) * 9)]
            asp.aspirate(name, r_vol, insert, tip, t_vol, disp_pos=pos)
            init.set_disp(name)

        # Move to next unfilled non-zero well
        elif min(k, m) < 12:
            wc.rapid_z_pos(name, val.plate96_movement_height)
            wc.rapid_xy_pos(name, [val.plate_96[val.x], val.plate_96[val.y] + (min(k, m) * 9)])
        else:
            wc.rapid_z_pos(name, val.plate96_movement_height)
            wc.rapid_xy_pos(name, [val.plate_96[val.x] + 9, val.plate_96[val.y] + ((-min(k, m) + 23) * 9)])

def n_ez_2tip_dispense(name: str, r_vol: list, tip: int, vol_array: np.array, t_vol, insert="EZ-Seed"):
    return None
