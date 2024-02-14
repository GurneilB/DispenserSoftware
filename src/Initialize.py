def write_preference(name, reservoir, rnum, tip, tnum,
                     plate, insert):
    """
    Initializes a G-code file. Writes user defined preferences to top of file

    :param name: name of the file
    :param reservoir: Type of reagent reservoir
    :param rnum: # of reservoirs
    :param tip: Type of tip
    :param tnum: # of tips
    :param plate: Type of culture plate
    :param insert: Type of custom insert (EZ-Seed or 3-in-1)
    """
    with open("%s.gcode" % name, "w") as file:
        file.write(";FLAVOR: Repetier\n")
        file.write(";RESERVOIR TYPE: %s\n" % reservoir)
        file.write(";NUMBER: %d\n" % rnum)
        file.write(";TIP TYPE: %s\n" % tip)
        file.write(";NUMBER: %d\n" % tnum)
        file.write(";PLATE TYPE: %s\n" % plate)
        file.write(";INSERT TYPE: %s\n" % insert)


def home(name):
    """
    Writes the homing axes command to file. Necessary for printer initialization

    :param name: name of the file
    """
    with open("%s.gcode" % name, "a") as file:
        file.write("G28 ;home\n")  # G28 is the Home command


def pick_tool(name, plate):
    """
    Writes the tool select command to file (picks between EZ-Seed and 3-in-1)

    :param name: name of file
    :param plate: type of plate
    :return:
    """

    if plate == "EZ-Seed":
        tool = 0
    else:
        tool = 1

    with open("%s.gcode" % name, "a") as file:
        file.write("T%d ;select %s tool \n"
                   % (tool, plate))  # T is the select tool command
