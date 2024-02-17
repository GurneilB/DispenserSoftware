def rapid_z_pos(rel, name, abs_pos=0, rel_pos=0):
    """
    Writes a rapid Z command to file

    :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
    :param abs_pos: absolute coordinate to move to (default = 0)
    :param rel_pos: relative coordinate to move to (default = 0)
    :param name: name of file to write to
    """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G0 Z%.3f \n" % rel_pos)
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G0 Z%.3f \n" % abs_pos)


def linear_z_pos(rel, name, speed, abs_pos=0, rel_pos=0, ):
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
            file.write("G0 Z%.3f F%.3f \n" % (rel_pos, speed))
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G0 Z%.3f F%.3f \n" % (abs_pos, speed))


def rapid_e_pos(rel, name, abs_pos=0, rel_pos=0):
    """
        Writes a rapid E command to file

        :param rel: TRUE if using relative coordinates, FALSE if using absolute coordinates
        :param abs_pos: absolute coordinate to move to (default = 0)
        :param rel_pos: relative coordinate to move to (default = 0)
        :param name: name of file to write to
        """
    if rel:

        with open("%s.gcode" % name, "a") as file:
            file.write("G0 E%.3f \n" % rel_pos)
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G0 E%.3f \n" % abs_pos)


def linear_e_pos(rel, name, speed, abs_pos=0, rel_pos=0, ):
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
            file.write("G0 E%.3f F%.3f \n" % (rel_pos, speed))
    else:
        with open("%s.gcode" % name, "a") as file:
            file.write("G0 E%.3f F%.3f \n" % (abs_pos, speed))
