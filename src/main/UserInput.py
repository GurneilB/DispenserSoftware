import csv
import numpy as np

tube_5mL = 5000.000
tube_1500uL = 1500.000


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


def get_reservoir_type():
    """
    Prompts user for reservoir type

    :return: (Float) size of reservoir in uL
    """
    while True:
        try:
            tube = input("Which reservoir are you using? (Type A for 5mL tube, "
                 "B for 1.5mL PCR tube): ")
            if tube not in {"A", "B"}:
                raise ValueError("Please choose either A or B.")
            return tube
        except ValueError as e:
            print(e)


def get_tip_type():
    """
    Prompts user for nozzle tip type
    :return: (Int) size of tip in uL
    """
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
    if plate == 96:
        return "EZ-Seed"
    else:
        return "3-in-1"

def get_design():
    """
    Prompts user for CSV file of experimental design
    :return: array of volumes per well
    """
    file = input("Enter the name of the CSV file: ")

    while True:

        try:
            with open(file, newline='') as csvfile:
                reader = csv.reader(csvfile)
                vol_array = np.array([row for row in reader])
                break
        except FileNotFoundError:
            print("Error: File not found.")
            file = input("Enter the name of the CSV file: ")

        except ValueError:
            print("Error: The file contains non-numeric values.")
            continue

        if vol_array.shape != (8, 12):
            print("Incorrect size. Include all volumes for culture plate.")
        else:
            return vol_array