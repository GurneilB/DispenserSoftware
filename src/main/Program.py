import UserInput as inp
import Initialize as init
import Calculations as calc
import BuildProcedure as bp
import MiscOperations as mo
import numpy as np

name = inp.get_procedure_name()
plate = inp.get_plate_type()
insert = inp.get_insert_type(plate)
res_type = inp.get_reservoir_type()
tip_type = inp.get_tip_type()
design = inp.get_design()

# UPDATE THIS FUNCTION
rnum = calc.num_reservoir(design, res_type)

tnum = calc.num_tip(design)

init.initialization(name, res_type, rnum, tip_type, tnum, plate, insert)
r_vol = calc.vol_per_res(design, res_type)
mo.equip(name)
bp.build_procedure(name, r_vol, insert, tip_type, design, res_type)

for i in range(2):
    mo.eject(name, i)

mo.present(name)

print("File successfully generated!")