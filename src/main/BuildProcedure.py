import src.main.WriteCoordinates as wc
import src.main.Initialize as init
import src.main.Calculations as calc
import src.main.Value as val
import src.main.Aspiration as asp
import src.main.Dispensing as disp
import numpy as np


def build_procedure(name: str, r_vol: list, insert: str, tip: int, vol_array, t_vol):
    """

    :param name: name of file to write to
    :param r_vol: volume of reagent in reservoirs
    :param insert:
    :param tip: max volume of tip
    :param vol_array: Volumetric design of plate
    :param t_vol: Current volume of reagent in tip
    """

    # Write dispensing comment to file
    init.set_disp(name)

    # Run protocol 1 (1x4 dispensing)
    if calc.get_protocol(vol_array) in {0, 1}:
        protocol1_dispense(name, r_vol, tip, vol_array, t_vol)

    # Run protocol 2 (2x1 dispensing)
    else:
        protocol2_dispense(name, r_vol, tip, vol_array, t_vol)