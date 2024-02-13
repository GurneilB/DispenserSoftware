def write_preference(name, reservoir, rnum, tip, tnum,
                     plate, insert):
    with open("%s.gcode" % name, "w") as file:
        file.write(";FLAVOR: Repetier\n")
        file.write(";RESERVOIR TYPE: %s\n" % reservoir)
        file.write(";NUMBER: %d\n" % rnum)
        file.write(";TIP TYPE: %s\n" % tip)
        file.write(";NUMBER: %d\n" % tnum)
        file.write(";PLATE TYPE: %s\n" % plate)
        file.write(";INSERT TYPE: %s\n" % insert)


def home(name):
    with open("%s.gcode" % name, "a") as file:
        file.write("G28 ;home")
