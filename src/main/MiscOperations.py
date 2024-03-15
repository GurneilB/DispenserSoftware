import src.main.WriteCoordinates as wc
import src.main.Initialize as init
import src.main.Calculations as calc
import src.main.Value as val
import numpy as np


def equip(name):
    """
    Writes tip-equipping commands to file

    :param name: name of file to write to
    """
    init.set_equip(name)
    init.set_absolute(name)
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, val.tip_tray_8)
    wc.rapid_z_pos(name, val.equip_height)
    wc.dwell(name, 2)
    wc.rapid_z_pos(name, val.movement_height_25mL)


def eject(name, tool):
    """
    Writes tip-ejection commands to file

    :param name: name of file to write to
    :param tool: motor to perform ejection
    """
    init.set_eject(name)
    init.set_absolute(name)

    # Move to Ejection Bowl
    wc.rapid_z_pos(name, val.movement_height_25mL)
    wc.rapid_xy_pos(name, val.eject_bowl)
    wc.rapid_z_pos(name, val.eject_height)

    # Eject Tips
    wc.rapid_e_pos(name, tool)
    wc.dwell(name, 2)
    wc.rapid_z_pos(name, val.movement_height_25mL)


def present(name):
    """
    Writes plate presenting commands to file

    :param name: name of file to write to
    """
    init.set_absolute(name)
    wc.rapid_z_pos(name, val.present_height)
    wc.rapid_xy_pos(name, val.present)
