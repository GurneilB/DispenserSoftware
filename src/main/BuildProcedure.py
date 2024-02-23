import WriteCoordinates as wc
import Initialize as init
import Calculations as calc

# Coordinate Bank
tip_tray_8 = [0, 0]
reservoir_5ml_4 = [0, 0]
plate_96 = [0, 0]
eject_bowl = [0, 0]
equip_height = 0
dispense_height_EZ = 0
dispense_height_3in1 = 0
eject_height = 0
aspirate_height = 0
movement_height = 0


def aspirate(name: str, r_vol: list[float], insert: str, tip: int, t_vol=None):
    """
    Writes Aspiration-related commands to G-code file

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    :param t_vol: Current volume of reagent in tip
    """

    # Write aspiration comment to file
    if t_vol is None:
        t_vol = [0.0, 0.0]
    init.set_asp(name)
    # Run aspiration for both motors
    for i in range(2):
        # Set to absolute positioning
        init.set_absolute(name)
        # Write XYZ pos of reservoirs
        wc.rapid_z_pos(name, movement_height)
        wc.rapid_xy_pos(name, reservoir_5ml_4)
        wc.rapid_z_pos(name, aspirate_height)
        # Set to relative positioning
        init.set_relative(name)
        # Pick active tool
        init.pick_tool(name, insert, i)
        # Write aspiration command, change remaining reservoir volume
        # Aspiration command when reservoir volume is greater than total tip volume
        if r_vol[i] >= tip:
            wc.rapid_e_pos(name, wc.rapid_e_pos(name, calc.convert_vol(tip)))
            t_vol[i] = tip
            r_vol[i] = r_vol[i] - tip
        # Aspiration command when reservoir volume is less than total tip volume
        else:
            wc.rapid_e_pos(name, wc.rapid_e_pos(name, calc.convert_vol(r_vol[i])))
            t_vol[i] = r_vol[i]
            r_vol[i] = 0

    # Set to absolute positioning
    init.set_absolute(name)
    # Move to dispensing position
    wc.rapid_z_pos(name, movement_height)
    wc.rapid_xy_pos(name, plate_96)


def protocol0_dispense(name: str, r_vol: list, insert: str, tip: int, vol_array, t_vol):
    # Build List of dispensing volumes
    path = vol_array[:, [-2, -1]]
    snake = build_snake(path)
    init.set_absolute(name)
    # Move to dispensing start point
    wc.rapid_xy_pos(name, plate_96)
    # Dispense every volume
    for i in range(len(snake)):
        init.set_absolute(name)
        # Move to dispense height
        wc.rapid_z_pos(name, dispense_height_EZ)
        init.set_relative(name)
        for j in range(2):
            # Dispense Reagent for both tools
            init.pick_tool(name, insert, j)
            wc.rapid_e_pos(name, calc.convert_vol(-snake[i]))
        if snake[i + 1] > t_vol[0]:
            aspirate(name, r_vol, insert, tip, t_vol)
            init.set_disp(name)
            init.set_absolute(name)
            if i + 1 <= 12:
                wc.rapid_xy_pos(name, [plate_96[0], plate_96[1] + (i * 9)])
            else:
                wc.rapid_xy_pos(name, [plate_96[0] - 9, plate_96[1] + ((-i + 25) * 9)])

        else:
            init.set_absolute(name)
            wc.rapid_z_pos(name, movement_height)
            init.set_relative(name)
            if i < 12:
                wc.rapid_xy_pos(name, [0, 9])
            elif i > 12:
                wc.rapid_xy_pos(name, [0, -9])
            else:
                wc.rapid_xy_pos(name, [-9, 0])


def build_procedure(name: str, r_vol: list, insert: str, tip: int, vol_array, t_vol=None):
    if t_vol is None:
        t_vol = [float(tip), float(tip)]
    # Write dispensing comment to file
    init.set_disp(name)
    # Run protocol 0 (1x4 dispensing)
    if calc.get_protocol(vol_array) == 0:
        protocol0_dispense(name, r_vol, insert, tip, vol_array, t_vol)

    elif calc.get_protocol(vol_array) == 1:
        # Not done
        path_1 = vol_array[:, [-2, -1]]
        path_2 = vol_array[:, [0, 1]]
        wc.rapid_xy_pos(name, plate_96)
    else:
        # Not done
        path = vol_array


def build_snake(array):
    snake = []
    num_rows = len(array)
    num_cols = len(array[0])
    for j in range(num_cols - 1, -1, -1):
        # Iterate through columns backwards
        if j % 2 == 0:
            for i in range(num_rows):
                # If the column index is even, iterate down the column
                snake.append(array[i][j])
        else:
            for i in range(num_rows - 1, -1, -1):
                # If the column index is odd, iterate up the column
                snake.append(array[i][j])
    return snake


def equip(name):
    init.set_equip(name)
    init.set_absolute(name)
    wc.rapid_z_pos(name, movement_height)
    wc.rapid_xy_pos(name, tip_tray_8)
    wc.rapid_z_pos(name, equip_height)
    wc.dwell(name, 2)
    wc.rapid_z_pos(name, movement_height)


def eject(name):
    init.set_eject(name)
    init.set_absolute(name)
    wc.rapid_z_pos(name, movement_height)
    wc.rapid_xy_pos(name, eject_bowl)
    wc.rapid_z_pos(name, eject_height)
    wc.rapid_e_pos(name, 0)
    wc.rapid_z_pos(name, movement_height)
