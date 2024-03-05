import numpy as np
import Value as val


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
    if get_protocol(vol_array) in {0, 1}:
        return val.tip4
    else:
        return val.tip2


def required_vol_per_tip(vol_array):
    """
    Calculates total volume needed per tip for entire procedure

    :param vol_array: array with well volumes
    :return: (List) Total volume needed per tip
    """

    # Checks for appropriate protocol
    if get_protocol(vol_array) == 0:
        # Return set of tip volumes for protocol 0
        return [(np.sum(vol_array, axis=0)[0]
                 + np.sum(vol_array, axis=0)[1]), ] * 4
    elif get_protocol(vol_array) == 1:
        # Return set of tip volumes for protocol 1
        return [(np.sum(vol_array, axis=0)[0]
                 + np.sum(vol_array, axis=0)[1]), (np.sum(vol_array, axis=0)[0]
                                                   + np.sum(vol_array, axis=0)[1]), (np.sum(vol_array, axis=0)[-2]
                                                                                     + np.sum(vol_array, axis=0)[-1]),
                (np.sum(vol_array, axis=0)[-2]
                 + np.sum(vol_array, axis=0)[-1])]
    else:
        # Return total volume for protocol 2
        return [np.sum(vol_array)] * 4


def total_required_vol_(vol_array):
    """
    Calculates total volume needed for entire procedure (w/out error)

    :param vol_array: array with well volumes
    :return: total volume needed for entire procedure
    """

    return np.sum(vol_array)


def vol_per_res(vol_array, reservoir: float):
    """
    Calculates total volume per reservoir for entire procedure

    :param vol_array: array with well volumes
    :param reservoir: size of reagent reservoir used
    :return: (List) volume per reservoir needed
    """
    # Get total volume
    total = total_required_vol_(vol_array)
    # get number of reservoirs needed
    rnum = num_reservoir(vol_array, reservoir)

    if reservoir == val.res_25mL:
        return [total]
    # Code below has not been updated or debugged
    # Check for protocol 1
    if get_protocol(vol_array) == 1:

        # Return list of volumes per reservoir
        return [total_required_vol_(vol_array[:, [0, 1, 2, 3]]) / (rnum) / 2,
                total_required_vol_(vol_array[:, [4, 5, 6, 7]]) / (rnum) / 2]
    elif get_protocol(vol_array) == 0:
        return [total]
    else:
        return [total / rnum] * 4


def num_reservoir(vol_array: np.array, reservoir: float):
    """
    Calculates number of reservoirs needed for entire procedure

    :param vol_array: array with well volumes
    :param reservoir: size of reagent reservoir used
    :return: # of reservoirs needed
    """
    if reservoir == val.res_25mL:
        return val.rnum1
    elif reservoir == val.tube_1500uL:
        if total_required_vol_(vol_array) >= reservoir * val.rnum4:
            return val.rnum8
        else:
            return val.rnum4


def convert_vol(vol: float):
    """
    Converts volume to relative extrusion (dispensing) distance

    :param vol:
    :return: (float) relative extrusion distance
    """
    return vol*val.model_factor


def get_protocol(vol_array: np.array):
    protocol_0 = 0
    protocol_1 = 1
    protocol_2 = 2

    section_1 = vol_array[:, [0, 1]]
    section_2 = vol_array[:, [2, 3]]
    section_3 = vol_array[:, [4, 5]]
    section_4 = vol_array[:, [6, 7]]

    # Checks equality of 2x12 sections of array, returns appropriate protocol
    if np.array_equal(section_1, section_2) & (
            np.array_equal(section_1, section_3) & (np.array_equal(section_1, section_4))):
        # protocol 0 is 1x4 dispensing
        return protocol_0
    elif np.array_equal(section_1, section_2) & np.array_equal(section_3, section_4):
        # protocol 1 is 2x2 dispensing
        return protocol_1
    else:
        # protocol 2 is 2x1 dispensing
        return protocol_2
