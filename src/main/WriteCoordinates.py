def rapid_z_pos(rel, name, abs_pos=0, rel_pos=0):
    """
    Writes a rapid Z command to file

    :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
    :param name: name of file to write to
    :param abs_pos: absolute coordinate to move to (default = 0)
    :param rel_pos: relative coordinate to move to (default = 0)
    """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G0 Z%.3f \n" % rel_pos)
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G0 Z%.3f \n" % abs_pos)


def linear_z_pos(rel, name, speed, abs_pos=0, rel_pos=0):
    """
    Writes a linear Z command to file

    :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
    :param name: name of file to write to
    :param speed: speed of motor movement
    :param abs_pos: absolute coordinate to move to (default = 0)
    :param rel_pos: relative coordinate to move to (default = 0)
    """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G1 Z%.3f F%.3f \n" % (rel_pos, speed))
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G1 Z%.3f F%.3f \n" % (abs_pos, speed))


def rapid_e_pos(rel, name, abs_pos=0, rel_pos=0):
    """
        Writes a rapid E command to file

        :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
        :param name: name of file to write to
        :param abs_pos: absolute coordinate to move to (default = 0)
        :param rel_pos: relative coordinate to move to (default = 0)
        """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G0 E%.3f \n" % rel_pos)
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G0 E%.3f \n" % abs_pos)


def linear_e_pos(rel, name, speed, abs_pos=0, rel_pos=0):
    """
        Writes a linear E command to file

        :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
        :param name: name of file to write to
        :param speed: speed of motor movement
        :param abs_pos: absolute coordinate to move to (default = 0)
        :param rel_pos: relative coordinate to move to (default = 0)
        """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G1 E%.3f F%.3f \n" % (rel_pos, speed))
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G1 E%.3f F%.3f \n" % (abs_pos, speed))


def rapid_xy_pos(rel, name, abs_pos=None, rel_pos=None):
    """
        Writes a rapid XY command to file

        :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
        :param name: name of file to write to
        :param abs_pos: list of X,Y absolute coordinates to move to (default = None)
        :param rel_pos: list of X,Y relative coordinates to move to (default = None)
        """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G0 X%.3f Y%.3f \n" % (rel_pos[1], rel_pos[2]))
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G0 X%.3f Y%.3f \n" % (abs_pos[1], abs_pos[2]))


def linear_xy_pos(rel, name, speed, abs_pos=None, rel_pos=None):
    """
        Writes a rapid XY command to file

        :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
        :param name: name of file to write to
        :param speed: speed of motor movement
        :param abs_pos: list of X,Y absolute coordinates to move to (default = None)
        :param rel_pos: list of X,Y relative coordinates to move to (default = None)
        """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G1 X%.3f Y%.3f F%.3f \n" % (rel_pos[1], rel_pos[2], speed))
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G1 X%.3f Y%.3f F%.3f \n" % (abs_pos[1], abs_pos[2], speed))