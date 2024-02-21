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


def pick_tool(name, insert, tool_=True):
    """
    Writes the tool select command to file

    :param name: name of file
    :param insert: type of insert
    :param tool_: True if tool 0 is desired, False for tool 1
    """

    if insert == "EZ-Seed":

        if tool_ == True:
            tool = 0
        elif tool_ == False:
            tool = 1
    else:
        tool = 2

    with open("%s.gcode" % name, "a") as file:
        file.write("T%d ;select %s tool \n"
                   % (tool, insert))  # T is the select tool command


def set_absolute(name):
    """
    Writes absolute positioning command to file

    :param name: name of file
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G90 ;sets absolute positioning\n"
                   )


def set_relative(name):
    """
    Writes relative positioning command to file

    :param name: name of file
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G91 ;sets relative positioning\n"
                   )


def set_mm(name):
    """
    Writes command to set units to mm to file

    :param name: name of file
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G21 ;sets units to mm\n"
                   )


def set_equip(name):
    """
    Writes tip equipping comment to file

    :param name: name of file to write to
    """
    with open("%s.gcode" % name, "a") as file:
        file.write(";Begin Tip Equipping\n"
                   )


def set_asp(name):
    """
    Writes aspiration comment to file

    :param name: name of file to write to
    """
    with open("%s.gcode" % name, "a") as file:
        file.write(";Begin Aspiration\n"
                   )


def set_disp(name):
    """
    Writes dispensing comment to file

    :param name: name of file to write to
    """
    with open("%s.gcode" % name, "a") as file:
        file.write(";Begin Dispensing\n"
                   )


def set_eject(name):
    """
    Writes tip ejection comment to file

    :param name: name of file to write to
    """
    with open("%s.gcode" % name, "a") as file:
        file.write(";Begin tip ejection\n"
                   )


def initialization(name, reservoir, rnum, tip, tnum,
                   plate, insert):
    """
    Full initialization of G-code file including writing preferences,
    selecting tools, and setting to absolute positioning

    :param name: name of the file
    :param reservoir: Type of reagent reservoir
    :param rnum: # of reservoirs
    :param tip: Type of tip
    :param tnum: # of tips
    :param plate: Type of culture plate
    :param insert: Type of custom insert (EZ-Seed or 3-in-1)
    """

    write_preference(name, reservoir, rnum, tip, tnum, plate, insert)
    pick_tool(name, insert)
    set_absolute(name)
    set_mm(name)
    home(name)