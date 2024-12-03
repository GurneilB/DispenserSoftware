import WriteCoordinates as wc
import Initialize as init
import Value as val

""" 
    Writes non-aspiration/dispensing related operations to gcode file.

    Equip: Writes tip-equipping commands to file

    Eject: Writes stage presenting commands to file

    Present: Presents stage contents to user
"""


def equip(name):
    """
    Writes tip-equipping commands to file

    :param name: name of file to write to
    """
    init.set_equip(name)
    init.set_absolute(name)
    wc.rapid_z_pos(name, val.movement_height_25mL, "Move height")
    wc.rapid_xy_pos(name, val.tip_tray_8, "Move to 8 Tip Tray")
    wc.rapid_z_pos(name, val.equip_height, "Equip tips")
    wc.dwell(name, 2)
    wc.rapid_z_pos(name, val.movement_height_25mL, "Move height")


def eject(name, insert, tool):
    """
    Writes tip-ejection commands to file

    :param name: name of file to write to
    :param insert: motor set to eject
    :param tool: motor to perform ejection
    """
    init.set_eject(name)
    init.set_absolute(name)

    # Move to Ejection Bowl
    wc.rapid_z_pos(name, val.movement_height_25mL, "Move height")
    wc.rapid_xy_pos(name, val.eject_bowl, "Move to ejection bowl")
    wc.rapid_z_pos(name, val.eject_height, "Ejection height")

    # Eject Tips
    init.pick_tool(name, insert, tool)
    wc.rapid_e_pos(name, -3, "Eject tips")
    wc.dwell(name, 2)


def present(name):
    """
    Writes stage presenting commands to file

    :param name: name of file to write to
    """
    init.set_absolute(name)
    wc.rapid_z_pos(name, val.present_height, "Present height")
    wc.rapid_xy_pos(name, val.present, "Present")

def homeExtruders(name: str):

    """
    Writes the homing command for both extruders

    :param name: name of file to write to 
    """

    with open("%s.gcode" % name, "a") as file:
        file.write("G204 P0 S0\n")
        file.write("G204 P1 S0\n")        
        file.write("G204 P0 S1\n")
        file.write("G205 P0\n")
        file.write("T0\n")
        file.write("G92 E0\n")
        file.write("G1 E17\n")
        file.write("G92 E0\n")
        file.write("G204 P0 S0\n")
        file.write("G204 P1 S0\n")
        file.write("G204 P1 S1\n")
        file.write("G205 P1\n")
        file.write("T1\n")
        file.write("G92 E0\n")
        file.write("G1 E17\n")
        file.write("G92 E0\n")
        file.write("G204 P0 S0\n")
        file.write("G204 P1 S0\n")