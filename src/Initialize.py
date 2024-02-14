def write_preference(name, reservoir, rnum, tip, tnum,
                     plate, insert):                        # Initialize file, write user preferences to top of file
    with open("%s.gcode" % name, "w") as file:
        file.write(";FLAVOR: Repetier\n")                   # Write firmware type
        file.write(";RESERVOIR TYPE: %s\n" % reservoir)     # Write reagent reservoir type
        file.write(";NUMBER: %d\n" % rnum)                  # Write # of reservoirs
        file.write(";TIP TYPE: %s\n" % tip)                 # Write tip type
        file.write(";NUMBER: %d\n" % tnum)                  # Write # of tips
        file.write(";PLATE TYPE: %s\n" % plate)             # Write plate type
        file.write(";INSERT TYPE: %s\n" % insert)           # Write insert type


def home(name):                                             # Write home axes command to file
    with open("%s.gcode" % name, "a") as file:
        file.write("G28 ;home\n")                           # G28 is the Home command
