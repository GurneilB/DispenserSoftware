import numpy as np
import Value as val

""" 
    Calculations required for generating aspiration/dispensing procedures:

    all_identical: Checks if all elements in an array are identical
    
    rows_identical: Checks if all elements in a row are identical
    
    num_tip: Calculates the max number for tips for user's procedure
    
    required_vol_per_tip: Calculates total volume needed per tip for entire procedure
    
    total_vol: Calculates total volume needed for plate design (w/out error)
    
    vol_per_res: Calculates total volume per reservoir for entire procedure
    
    num_reservoir: Calculates number of reservoirs needed for entire procedure
    
    convert_vol: Converts volume to relative extrusion (dispensing) distance
    
    get_protocol: Finds relevant dispensing protocol for culture plate design
    
    build_snake: Creates list of values in snake order, starting from top right of array
    moving column-wise towards the left.
"""


def all_identical(arr):
    """
    Checks if all elements in an array are identical

    :param arr: array to be checked
    :return: TRUE if all elements are identical, FALSE otherwise
    """
    # Checks if all elements in an array are the same
    return np.all(arr == arr[0, 0])


def rows_identical(arr):
    """
    Checks if all elements in a row are identical

    :param arr: array to be checked
    :return: TRUE if all elements are identical, FALSE otherwise
    """
    # Loops through each row
    for i in range(val.dims_96[1]):

        # Loops through each element in a row
        for j in range(val.dims_96[0]):

            # Checks if element is not identical to first element in the row
            if arr[i, j] != arr[i, 0]:
                return False

    return True


def num_tip(vol_array: np.array):
    """
    Calculates the max number for tips for user's procedure

    :param vol_array: Array corresponding to volumes in each
            well of culture plate
    :return: Number of tips required for dispensing
    """
    # Checks for appropriate protocol
    if get_protocol(vol_array) == val.tip4_96:
        # Returns "4" for 4-tip dispensing
        return val.tip4
    elif get_protocol(vol_array) in {val.tip2_96, val.tip2_6}:
        # Returns "2" for 2-tip dispensing
        return val.tip2
    elif get_protocol(vol_array) == val.tip1_6:
        # Returns "1" for 1-tip dispensing
        return val.tip1


def required_vol_per_tip(vol_array):
    """
    Calculates total volume needed per tip for entire procedure

    :param vol_array: array with well volumes
    :return: (List) Total volume needed per tip
    """

    # 96 Well Plate Protocols
    if np.shape(vol_array) == (12, 8):
        section_1 = vol_array[:, [0, 1]]
        section_2 = vol_array[:, [2, 3]]
        section_3 = vol_array[:, [4, 5]]
        section_4 = vol_array[:, [6, 7]]

        if get_protocol(vol_array) == val.tip4_96:

            # Return set of tip volumes for 96-well 4-tip Dispensing
            return [total_vol(section_4), total_vol(section_3), total_vol(section_2), total_vol(section_1)]

        elif get_protocol(vol_array) == val.tip2_96:

            # Return set of tip volumes for 96-well 2-tip Dispensing
            return [total_vol(section_4) + total_vol(section_3), total_vol(section_2) + total_vol(section_1)]

    # 6-well plate volumes
    else:
        section_1 = vol_array[:, [0]]
        section_2 = vol_array[:, [1]]

        if get_protocol(vol_array) == val.tip2_96:

            # Return set of tip volumes for 6-well 2-tip Dispensing
            return [total_vol(section_2) * 4, total_vol(section_1) * 4]

        elif get_protocol(vol_array) == val.tip1_6:

            # Return set of tip volumes for 6-well 1-tip Dispensing
            return [total_vol(vol_array)]


def total_vol(vol_array):
    """
    Calculates total volume needed for plate design (w/out error)

    :param vol_array: array with well volumes
    :return: total volume needed for entire procedure
    """

    # Return total for 96 well plate
    if np.shape(vol_array) == (12, 8):
        return np.sum(vol_array)

    # Return total for 6-well plate
    elif np.shape(vol_array) == (3, 2):
        return np.sum(vol_array) * 4

    else:
        return np.sum(vol_array)


def vol_per_res(vol_array, reservoir: float):
    """
    Calculates total volume per reservoir for entire procedure

    :param vol_array: array with well volumes
    :param reservoir: size of reagent reservoir used
    :return: (List) volume per reservoir needed
    """

    double_tubes = False

    # Get total tip volumes
    total_vols = required_vol_per_tip(vol_array)

    # For 25ml Reservoir
    if reservoir == val.res_25mL:

        # For 4 tips
        if num_tip(vol_array) == val.tip4:

            # Return reservoir volume needed for both motors, 4-tip dispensing
            return [total_vols[0] + total_vols[1], total_vols[2] + total_vols[3]]

        # For 2 tips
        elif num_tip(vol_array) == val.tip2:

            # Return reservoir volume needed for both motors, 2-tip dispensing
            return [total_vols[0], total_vols[1]]

        else:

            # Return reservoir volume needed for one motor, 1-tip dispensing
            return [total_vols[0]]

    # For 1.5mL Reservoir
    elif reservoir == val.tube_1500uL:

        # For 4 tips
        if num_tip(vol_array) == val.tip4:

            # Check if any tip needs more than 1500uL
            for i in range(4):
                if total_vols[i] > val.tube_1500uL:
                    double_tubes = True

            if double_tubes:

                # Return reservoir volume needed for both motors, 4-tip dispensing, 8 tubes
                return [total_vols[0] / 2, total_vols[1] / 2, total_vols[2] / 2, total_vols[3] / 2,
                        total_vols[0] / 2, total_vols[1] / 2, total_vols[2] / 2, total_vols[3] / 2]
            else:

                # Return reservoir volume needed for both motors, 4-tip dispensing, 4 tubes
                return [total_vols[0], total_vols[1], total_vols[2], total_vols[3],
                        0, 0, 0, 0]

        # For 2 tips
        elif num_tip(vol_array) == val.tip2:

            # Check if any tip needs more than 1500uL
            for i in range(2):
                if total_vols[i] > val.tube_1500uL:
                    double_tubes = True

            if double_tubes:

                # Return reservoir volume needed for both motors, 2-tip dispensing, 4 tubes
                return [0, total_vols[0] / 2, 0, total_vols[1] / 2,
                        0, total_vols[0] / 2, 0, total_vols[1] / 2]

            else:

                # Return reservoir volume needed for both motors, 2-tip dispensing, 2 tubes
                return [0, total_vols[0] / 2, 0, total_vols[1] / 2,
                        0, 0, 0, 0]

        # For 1 tip
        else:

            # 4 Tubes
            if val.tube_1500uL * 3 < total_vols[0] < val.tube_1500uL * 4:
                return [total_vols[0] / 4, total_vols[0] / 4, total_vols[0] / 4, total_vols[0] / 4]

            # 3 Tubes
            elif val.tube_1500uL * 2 < total_vols[0] < val.tube_1500uL * 3:
                return [total_vols[0] / 3, total_vols[0] / 3, total_vols[0] / 3, 0]
            # 2 Tubes
            elif val.tube_1500uL < total_vols[0] < val.tube_1500uL * 2:
                return [total_vols[0] / 2, total_vols[0] / 2, 0, 0]

            # 1 Tube
            else:
                return [total_vols[0], 0, 0, 0]


def num_reservoir(vol_array: np.array, reservoir: float):
    """
    Calculates number of reservoirs needed for entire procedure

    :param vol_array: array with well volumes
    :param reservoir: size of reagent reservoir used
    :return: # of reservoirs needed
    """
    if reservoir == val.res_25mL:

        # Returns "1" for 25mL reservoir
        return val.rnum1

    else:

        # Return # of non-zero elements in reservoir volume list
        non_zero_count = sum(1 for x in vol_per_res(vol_array, reservoir) if x != 0)
        return non_zero_count


def convert_vol(vol: float):
    """
    Converts volume to relative extrusion (dispensing) distance

    :param vol:
    :return: (float) relative extrusion distance
    """
    return vol * val.model_factor


def get_protocol(vol_array: np.array):
    """
    Finds relevant dispensing protocol for culture plate design

    :param vol_array: array with well volumes
    :return: Relevant protocol number
    """
    # Convert vol_array to a NumPy array if it's not already one
    vol_array = np.array(vol_array)

    # 96 Well Plate Protocols
    if np.shape(vol_array) == (12, 8):
        section_1 = vol_array[:, [0, 1]]
        section_2 = vol_array[:, [2, 3]]
        section_3 = vol_array[:, [4, 5]]
        section_4 = vol_array[:, [6, 7]]

        # Checks equality of 2x12 sections of array, returns appropriate protocol
        if np.array_equal(section_1, section_2) & np.array_equal(section_3, section_4):

            # protocol 0 is 4 Tip dispensing
            return val.tip4_96
        else:

            # protocol 1 is 2 Tip dispensing
            return val.tip2_96

    # 6 Well Plate Protocols
    elif np.shape(vol_array) == (3, 2):
        if rows_identical(vol_array):

            # Protocol 2 is 2 Tip Dispensing
            return val.tip2_6
        else:

            # Protocol 3 is 1 Tip Dispensing
            return val.tip1_6


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
