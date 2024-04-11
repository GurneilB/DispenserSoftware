import numpy as np
import Value as val

""" Functions relating to prompting user input via terminal/command-line """


def get_procedure_name():
    """
    Prompts user for procedure name

    :return: (String) procedure name
    """
    while True:
        try:
            name = input("Please type in your procedure name: \n")
            if name == "":
                raise TypeError("The procedure name cannot be empty. Please try again")
            return name
        except TypeError as e:
            print(e)


def get_reservoir_type(default=True):
    """
    Prompts user for reservoir type

    :return: (Float) size of reservoir in uL
    """
    if default:
        return val._25mL
    while True:
        try:
            tube = input("Which reservoir are you using? (Type A for 25mL reservoir, "
                         "B for 1.5mL tube): ")
            if tube not in {"A", "B"}:
                raise ValueError("Invalid Input\n Please select A or B.")
            elif tube == "A":
                return val._25mL
            else:
                return val._5mL
        except ValueError as e:
            print(e)


def get_tip_type(default=True):
    """
    Prompts user for nozzle tip type
    :return: (Int) size of tip in uL
    """
    if default:
        return val._250uL_tip
    else:
        while True:
            try:
                tip = int(input("Which size nozzle tip are you using? (Type volume in uL): "))
                return tip
            except ValueError:
                print("Volume should be an integer. Please enter a number.")


def get_plate_type():
    """
    Prompts user for culture plate type
    :return: (Int) size of culture plate
    """
    while True:
        try:
            plate = int(input("What size culture plate are you using? (Type # of wells): "))
            if plate not in {6, 96}:
                raise ValueError("Plate type must be either 6 or 96. Please try again")
            return plate
        except ValueError as e:
            print(e)


def get_insert_type(plate: int):
    """
    Prompts user for culture plate insert type
    :return: (String) name of culture plate insert
    """
    if plate == val.zone_96:
        return val.ez_seed
    else:
        return val.three_in_one


def get_design():
    """
    Prompts user for CSV file of experimental design
    :return: array of volumes per well
    """
    file = input("Enter the name of the CSV file: ")

    while True:

        try:
            vol_array = np.loadtxt(file, delimiter=',', dtype=float)

        except FileNotFoundError:
            print("Error: File not found.")
            file = input("Enter the name of the CSV file: ")

        except ValueError:
            print("Error: The file contains non-numeric values.")
            continue

        # ***This does not work****
        # if vol_array.shape != (8, 12):
        # print("Incorrect size. Include all volumes for culture plate.")
        else:
            return vol_array


def get_equip():
    """
    Prompts user to specify if automatic tip equip is desired

    :return: (bool) True for equip, False otherwise
    """
    while True:
        try:
            equip = input("Please indicate if you want to auto-equip tips? (T or F): \n")
            equip.upper()
            if equip not in {"T", "F"}:
                raise ValueError("Invalid Input\n Please select T or F.")
            elif equip == "T":
                return True
            else:
                return False
        except ValueError as e:
            print(e)


def get_eject():
    """
    Prompts user to specify if automatic tip equip is desired

    :return: (bool) True for equip, False otherwise
    """
    while True:
        try:
            eject = input("Please indicate if you want to auto-eject tips? (T or F): \n")
            eject.upper()
            if eject not in {"T", "F"}:
                raise ValueError("Invalid Input\n Please select T or F.")
            elif eject == "T":
                return True
            else:
                return False
        except ValueError as e:
            print(e)
