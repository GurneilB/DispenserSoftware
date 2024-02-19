import numpy as np

dims_96 = (8, 12)
plate_96 = 96
tip1 = 1
tip4 = 4
rnum4 = 4
rnum8 = 8


def all_identical(arr):
    """
    Checks if all elements in an array are identical

    :param arr: array to be checked
    :return: TRUE if all elements are identical, FALSE otherwise
    """

    return np.all(arr == arr[0, 0])


def rows_identical(arr):
    """
    Checks if all elements in a row are identical
    :param arr: array to be checked
    :return: TRUE if all elements are identical, FALSE otherwise
    """

    for i in range(dims_96[1]):
        for j in range(dims_96[0]):
            if arr[i, j] != arr[i, 0]:
                return False

    return True


def num_tip(vol_array):
    """
    Calculates the greatest number for tips for user's procedure

    :param vol_array: Array corresponding to volumes in each
            well of culture plate
    :return: Number of tips required for dispensing
    """

    if vol_array.size != plate_96 or rows_identical(vol_array):
        return tip4
    else:
        return tip1


def required_vol_per_tip(vol_array):
    """
    Calculates total volume needed per tip for entire procedure

    :param vol_array: array with well volumes
    :return: Total volume needed per tip
    """

    if num_tip(vol_array) == tip4:

        return (np.sum(vol_array, axis=0)[0]
                + np.sum(vol_array, axis=0)[1])

    else:
        return np.sum(vol_array)


def total_required_vol_(vol_array):
    """
    Calculates total volume needed for entire procedure (w/out error)

    :param vol_array: array with well volumes
    :return: total volume needed for entire procedure
    """

    return np.sum(vol_array)


def vol_per_res(vol_array, reservoir):
    """
    Calculates total volume per reservoir for entire procedure

    :param vol_array: array with well volumes
    :param reservoir: size of reagent reservoir used
    :return: volume per reservoir needed
    """
    total = total_required_vol_(vol_array)
    rnum = num_reservoir(vol_array, reservoir)

    return total / rnum


def num_reservoir(vol_array, reservoir):
    """
    Calculates number of reservoirs needed for entire procedure

    :param vol_array: array with well volumes
    :param reservoir: size of reagent reservoir used
    :return: # of reservoirs needed
    """
    if num_tip(vol_array) == tip4:
        if total_required_vol_(vol_array) >= reservoir * tip4:
            return rnum8
        else:
            return rnum4
    else:
        rnum = total_required_vol_(vol_array) / reservoir

        return rnum


def convert_vol(vol):
    """
    Converts volume to relative extrusion (dispensing) distance

    :param vol:
    :return: (float) relative extrusion distance
    """
    return vol * vol
