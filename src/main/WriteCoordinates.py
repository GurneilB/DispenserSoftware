from typing import List

import Value as val

""" Functions related to writing movement related commands to G-code file"""


def rapid_z_pos(name: str, pos: float, message: str):
    """
    Writes a rapid Z command to file

    :param name: name of file to write to
    :param pos: Z coordinate (absolute or relative) to move to
    :param message: Comment to add to the file
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G0 Z%.3f; %s \n" % (pos, message))


def linear_z_pos(name: str, pos: float, speed: float, message: str):
    """
    Writes a linear Z command to file

    :param name: name of file to write to
    :param pos: Z coordinate (absolute or relative) to move to
    :param speed: speed of motor movement
    :param message: Comment to add to the file
    """
    with open("%s.gcode" % name, "a") as file:
        file.write("G1 Z%.3f F%.3f; %s \n" % (pos, speed, message))


def rapid_e_pos(name: str, pos: float, message: str):
    """
    Writes a rapid E command to file

    :param name: name of file to write to
    :param pos: E coordinate (absolute or relative) to move to
    :param message: Comment to add to the file
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G0 E%.3f; %s \n" % (pos, message))


def linear_e_pos(name: str, pos: float, speed: float, message: str):
    """
    Writes a linear E command to file

    :param name: name of file to write to
    :param pos: E coordinate (absolute or relative) to move to
    :param speed: speed of motor movement
    :param message: Comment to add to the file
    """
    with open("%s.gcode" % name, "a") as file:
        file.write("G1 E%.3f F%.3f; %s \n" % (pos, speed, message))


def rapid_xy_pos(name: str, pos: List[float], message: str):
    """
    Writes a rapid XY command to file

    :param name: name of file to write to
    :param pos: list of X,Y (absolute or relative) coordinates to move to
    :param message: Comment to add to the file
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G0 X%.3f Y%.3f; %s \n" % (pos[val.x], pos[val.y], message))


def linear_xy_pos(name: str, pos: List[float], speed: float, message: str):
    """
    Writes a linear XY command to file

    :param name: name of file to write to
    :param pos: list of X,Y (absolute or relative) coordinates to move to
    :param speed: speed of motor movement
    :param message: Comment to add to the file
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G1 X%.3f Y%.3f F%.3f; %s \n" % (pos[val.x], pos[val.y], speed, message))


def dwell(name: str, time: int):
    """
    Writes a wait command to file

    :param name: name of file to write to
    :param time: time to wait in seconds
    """
    with open("%s.gcode" % name, "a") as file:
        file.write("G4 S%d ; Dwell\n" % time)


def pause(name: str, message: str):
    """
    Writes a pause command to file

    :param name: name of file to write to
    :param message: Comment to add to the file
    """
    with open("%s.gcode" % name, "a") as file:
        file.write("@pause ; %s\n" % message)
