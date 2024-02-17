import numpy as np


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

    for i in range(12):
        for j in range(8):
            if arr[i,j] != arr[i,0]:
                return False

    return True


def calculate_tip(vol_array):
    """
    Calculates the greatest number for tips for user's procedure

    :param vol_array: Array corresponding to volumes in each
            well of culture plate
    :return: Number of tips required for dispensing
    """

    if vol_array.size != 96 or rows_identical(vol_array):
        return 4
    else:
        return 1


def required_vol_per_tip(vol_array):
    """
    Calculates total volume needed per tip for entire procedure

    :param vol_array: array with well volumes
    :return: Total volume needed per tip
    """

    if calculate_tip(vol_array) == 4:

        return (np.sum(vol_array, axis=0)[0]
                + np.sum(vol_array, axis=0)[1])

    else:
        return np.sum(vol_array)