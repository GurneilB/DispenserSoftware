x = 0
y = 1


def rapid_z_pos(name: str, pos: float):
    """
    Writes a rapid Z command to file

    :param name: name of file to write to
    :param pos: Z coordinate (absolute or relative) to move to
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G0 Z%.3f \n" % pos)


def linear_z_pos(name: str, pos: float, speed: float):
    """
    Writes a linear Z command to file

    :param name: name of file to write to
    :param pos: Z coordinate (absolute or relative) to move to
    :param speed: speed of motor movement
    """
    with open("%s.gcode" % name, "a") as file:
        file.write("G1 Z%.3f F%.3f \n" % (pos, speed))


def rapid_e_pos(name: str, pos: float):
    """
    Writes a rapid E command to file

    :param name: name of file to write to
    :param pos: E coordinate (absolute or relative) to move to
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G0 E%.3f \n" % pos)


def linear_e_pos(name: str, pos: float, speed: float):
    """
    Writes a linear E command to file

    :param name: name of file to write to
    :param pos: E coordinate (absolute or relative) to move to
    :param speed: speed of motor movement
    """
    with open("%s.gcode" % name, "a") as file:
        file.write("G1 E%.3f F%.3f \n" % (pos, speed))


def rapid_xy_pos(name: str, pos: list[float]):
    """
    Writes a rapid XY command to file

    :param name: name of file to write to
    :param pos: list of X,Y (absolute or relative) coordinates to move to
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G0 X%.3f Y%.3f \n" % (pos[x], pos[y]))


def linear_xy_pos(name: str, pos: list[float], speed: float):
    """
    Writes a linear XY command to file

    :param name: name of file to write to
    :param pos: list of X,Y (absolute or relative) coordinates to move to
    :param speed: speed of motor movement
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G1 X%.3f Y%.3f F%.3f \n" % (pos[x], pos[y], speed))


def dwell(name: str, time: int):
    with open("%s.gcode" % name, "a") as file:
        file.write("G4 S%d ; Dwell\n" % time)
