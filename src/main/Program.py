import UserInput as inp
import Initialize as init
import Calculations as calc
import BuildProcedure as bp

name = inp.get_procedure_name()
plate = inp.get_plate_type()
insert = inp.get_insert_type(plate)
res_type = inp.get_reservoir_type()
tip_type = inp.get_tip_type()
design = inp.get_design()
rnum = calc.num_reservoir(design, res_type)
tnum = calc.num_tip(design)

init.initialization(name, res_type, rnum, tip_type, tnum, plate, insert)
