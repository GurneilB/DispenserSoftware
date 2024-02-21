import csv

tube_5mL = 5000.000
tube_1500uL = 1500.000
# No. of wells in 96-well plate
plate_96 = 96
# No. of wells in 6-well plate
plate_6 = 6

def get_procedure_name():
    """
    Prompts user for procedure name

    :return: (String) procedure name
    """
    name = input("Please type in your procedure name: ")
    return name


def get_reservoir_type():
    """
    Prompts user for reservoir type

    :return: (Float) size of reservoir in uL
    """
    tube = input("Which reservoir are you using? (Type A for 5mL tube, "
                 "B for 1.5mL PCR tube): ")
    if tube == "A":
        return tube_5mL
    else:
        return tube_1500uL


def get_tip_type():
    """
    Prompts user for nozzle tip type

    :return: (Int) size of tip in uL
    """
    tip = int(input("Which size nozzle tip are you using? (Type size in uL): "))
    return tip


def get_plate_type():
    """
    Prompts user for culture plate type

    :return: (Int) size of culture plate
    """
    plate = int(input("What size culture plate are you using? (Type # of wells): "))
    #  ***Value error exception and only accept 96 and 6 as inputs***
    return plate


def get_insert_type(plate):
    """
    Prompts user for culture plate insert type

    :return: (String) name of culture plate insert
    """
    if plate == plate_96:
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
                vol_array = [row for row in reader]
                break
        except FileNotFoundError:
            print("Error: File not found.")
            file = input("Enter the name of the CSV file: ")

    return vol_array
