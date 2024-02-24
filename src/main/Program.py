import UserInput as inp
import Initialize as init
import Calculations as calc
import BuildProcedure as bp
import Exceptions as E

name = E.Exception_name()
plate = E.Exception_plate()
insert = inp.get_insert_type(plate)
res_type = E.Exception_reservoir()
tip_type = E.Exception_tip()
design = E.Exception_design() #I'm working on testing this
rnum = calc.num_reservoir(design, res_type)
tnum = calc.num_tip(design)

init.initialization(name, res_type, rnum, tip_type, tnum, plate, insert)
r_vol = calc.vol_per_res(design,res_type)
bp.equip(name)
bp.aspirate(name, r_vol, insert, tip_type)
bp.build_procedure(name,r_vol,insert,tip_type, design)
bp.eject(name)
init.home(name)

