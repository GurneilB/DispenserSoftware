import WriteCoordinates as wc
import Initialize as init
import Calculations as calc

# Coordinate Bank
tip_tray_8 = [0, 0]
reservoir_5ml_4 = [0,0]
plate_96 = 0
equip_height = 0
dispense_height = 0
eject_height = 0
aspirate_height = 0


def aspirate(name: str, r_vol: list, insert: str, tip: int):
    """
    Writes Aspiration-related commands to G-code file

    :param name: name of file to write to
    :param r_vol: volume remaining in reservoir
    :param insert: type of insert used for procedure
    :param tip: max volume of tip
    """
    init.set_asp(name)
    for i in range (2):
        init.set_absolute(name)
        # Write XYZ pos of reservoirs
        wc.rapid_xy_pos(name, reservoir_5ml_4)
        wc.rapid_z_pos(name, aspirate_height)
        init.set_relative(name)
        init.pick_tool(name,insert, i)
        # Write aspiration command, change remaining reservoir volume
        if r_vol[i] >= tip:
            wc.rapid_e_pos(name, wc.rapid_e_pos(name, calc.convert_vol(tip)) )
            r_vol[i] =  r_vol[i] - tip
        else:
            wc.rapid_e_pos(name, wc.rapid_e_pos(name, calc.convert_vol(r_vol[i])))
            r_vol[i] = 0

    init.set_absolute(name)

#def build_procedure(name, vol_array):
