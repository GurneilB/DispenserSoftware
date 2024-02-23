import WriteCoordinates as wc
import Initialize as init
import Calculations as calc

# Coordinate Bank
tip_tray_8 = [0, 0]
reservoir_5ml_4 = [0,0]
plate_96 = [0,0]
eject_bowl = [0,0]
equip_height = 0
dispense_height_EZ = 0
dispense_height_3in1 = 0
eject_height = 0
aspirate_height = 0
movement_height = 0


def aspirate(name: str, r_vol: list, insert: str, tip: int):
    """
    Writes Aspiration-related commands to G-code file

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    """

    # Write aspiration comment to file
    init.set_asp(name)
    # Run aspiration for both motors
    for i in range (2):
        # Set to absolute positioning
        init.set_absolute(name)
        # Write XYZ pos of reservoirs
        wc.rapid_z_pos(name, movement_height)
        wc.rapid_xy_pos(name, reservoir_5ml_4)
        wc.rapid_z_pos(name, aspirate_height)
        # Set to relative positioning
        init.set_relative(name)
        # Pick active tool
        init.pick_tool(name,insert, i)
        # Write aspiration command, change remaining reservoir volume
        # Aspiration command when reservoir volume is greater than total tip volume
        if r_vol[i] >= tip:
            wc.rapid_e_pos(name, wc.rapid_e_pos(name, calc.convert_vol(tip)) )
            r_vol[i] =  r_vol[i] - tip
        # Aspiration command when reservoir volume is less than total tip volume
        else:
            wc.rapid_e_pos(name, wc.rapid_e_pos(name, calc.convert_vol(r_vol[i])))
            r_vol[i] = 0

    # Set to absolute positioning
    init.set_absolute(name)
    # Move to dispensing position
    wc.rapid_z_pos(name, movement_height)
    wc.rapid_xy_pos(name, plate_96)

def build_procedure(name: str, r_vol: list, insert: str, tip: int, vol_array):
    row = 1
    # Write dispensing comment to file
    init.set_disp(name)
    # Run protocol 0 (1x4 dispensing)
    if calc.get_protocol(vol_array) == 0:
        # Write dispensing comment to file
        path = vol_array[:, [-2, -1]]
        snake = buildSnake(path)
        init.set_absolute(name)
        wc.rapid_xy_pos(name, plate_96)

        for i in range (len(snake)):
            init.set_absolute(name)
            wc.rapid_z_pos(name, dispense_height_EZ)
            init.set_relative(name)
            for j in range (2):
                init.pick_tool(name, insert, j)
                wc.rapid_e_pos(name, calc.convert_vol(-snake[i]))
            #if calc.convert_vol(-snake[i+1]) > t_vol[j]:


    elif calc.get_protocol(vol_array) == 1:
        path_1 = vol_array[:, [-2, -1]]
        path_2 = vol_array[:, [0, 1]]
        wc.rapid_xy_pos(name, plate_96)
    else:
        path = vol_array


def buildSnake(array):
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