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
        name = input("Please type in your procedure name: \n")
        if name != "":
            return name
        else:
            print("The procedure name cannot be empty. Please try again")

def get_reservoir_type():
    """
    Prompts user for reservoir type

    :return: (Float) size of reservoir in uL
    """
    while True:
        tube = input("Which reservoir are you using? (Type A for 5mL tube, "
                 "B for 1.5mL PCR tube): ")
        if tube not in {"A", "B"}:
            print("Please choose either A or B.")
        else:
            return tube


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
            plate = input("What size culture plate are you using? (Type # of wells): ")
            if not plate.isdigit():
                raise ValueError("Input cannot be string. Please enter a number.")
            plate = int(plate)
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

    return vol_array

