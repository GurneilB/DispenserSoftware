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

    if np.all(np.all(arr == arr[0], axis=1)):
        return True
    return False


def calculate_tip(vol_array):
    """
    Calculates the greatest number for tips for user's procedure

    :param vol_array: Array corresponding to volumes in each
            well of culture plate
    :return: Number of tips required for dispensing
    """

    num_wells = vol_array.size

    if num_wells != 96 or rows_identical(vol_array):
        return 4
    else:
        return 1