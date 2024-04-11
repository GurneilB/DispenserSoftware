import Calculations as calc
import Value as val
import Aspiration as asp
import Dispensing as disp

""" Finds and executes appropriate aspiration/dispensing procedure for given preferences.
 Supports 96 well EZ-Seed and no-insert, with 25mL and 1.5mL reservoirs.
 No 6-well or 3-in-1 insert support (To be added)."""

def build_procedure(name: str, r_vol: list, insert: str, tip: int, vol_array, restype):
    """
    Finds correct dispensing and aspiration functions for procedure and writes commands to file

    :param name: name of file to write to
    :param r_vol: volume of reagent in reservoirs
    :param insert: Type of insert used for procedure
    :param tip: max volume of tip
    :param vol_array: Volumetric design of plate
    :param restype: Type of reservoir used for procedure
    """

    # Run EZ SEED 4 Tip Dispensing
    if calc.get_protocol(vol_array) == val._4_tip_96well_protocol:

        # Run EZ SEED 4 Tip Dispensing
        if insert == val.ez_seed:
            t_vol = asp.asp_4tip(name, r_vol, insert, tip, restype)
            disp.ez_4tip_dispense(name, r_vol, tip, vol_array, t_vol, restype)

        # Run General 96-Well 4 Tip Dispensing
        else:
            t_vol = asp.asp_4tip(name, r_vol, insert, tip, restype)
            disp.n_ez_4tip_dispense(name, r_vol, tip, vol_array, t_vol, restype)

    # Run EZ SEED 2 Tip Dispensing
    elif calc.get_protocol(vol_array) == val._2_tip_96well_protocol:

        # Run EZ SEED 2 Tip Dispensing
        if insert == val.ez_seed:
            t_vol = asp.asp_2tip(name, r_vol, insert, tip, restype)
            disp.ez_2tip_dispense(name, r_vol, tip, vol_array, t_vol, restype)

        # Run General 96-Well 2 Tip Dispensing
        else:
            t_vol = asp.asp_2tip(name, r_vol, insert, tip, restype)
            disp.n_ez_2tip_dispense(name, r_vol, tip, vol_array, t_vol, restype)

    # Run 3-in-1 2 Tip Dispensing
    elif calc.get_protocol(vol_array) == val._2_tip_6well_protocol:

        # Run 3-in-1 2 Tip Dispensing
        if insert == val.three_in_one:
            # WRITE CODE HERE
            pass

        # Run General 6-Well 2 Tip Dispensing
        else:
            # WRITE CODE HERE
            pass

    # Run 3-in-1 1 Tip Dispensing
    elif calc.get_protocol(vol_array) == val._1_tip_6well_protocol:

        # Run 3-in-1 1 Tip Dispensing
        if insert == val.three_in_one:
            # WRITE CODE HERE
            pass

        # Run General 6-Well 1 Tip Dispensing
        else:
            # WRITE CODE HERE
            pass
