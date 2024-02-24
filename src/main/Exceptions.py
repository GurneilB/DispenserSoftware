import src.main.UserInput as UI
import numpy as np

def Exception_name():
    while True:
        try:
            name = UI.get_procedure_name()
            if name == "":
                raise TypeError("The procedure name cannot be empty. Please try again")
            return name
        except TypeError as e:
            print(e)

def Exception_plate():
    while True:
        try:
            plate = UI.get_plate_type()
            if plate not in {6, 96}:
                raise ValueError("Plate type must be either 6 or 96. Please try again")
            return plate
        except ValueError as e:
            print(e)


def Exception_reservoir():
    while True:
        try:
            tube = UI.get_reservoir_type()
            if tube not in {"A", "B"}:
                raise ValueError("Please choose either A or B.")
            return tube
        except ValueError as e:
            print(e)

def Exception_tip():
    while True:
        try:
            tip = int(UI.get_tip_type())
            return tip
        except ValueError:
            print("Volume should be an integer. Please enter a number.")

def Exception_design():
    while True:
        vol_array = UI.get_design()
        try:
            vol_array = np.array(vol_array, dtype = float)
        except ValueError:
            print("Error: The file contains non-numeric values.")
            continue

        if vol_array.shape != (8, 12):
            print("Volume array is not the correct size. Ensure the array of values is a (8x12) matrix.")
        else:
            return vol_array

