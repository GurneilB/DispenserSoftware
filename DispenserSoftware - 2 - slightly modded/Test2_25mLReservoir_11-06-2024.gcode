;FLAVOR: Repetier
;RESERVOIR TYPE: 25000.0
;NUMBER: 1
;TIP TYPE: 250uL
;NUMBER: 4
;PLATE TYPE: 96
;INSERT TYPE: EZ-SEED
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G21 ;sets units to mm
G28 ;home
G90 ;sets absolute positioning
G0 Z0.000; Present height 
G0 X65.000 Y0.000; Present 
@pause ; Load Stage and Continue
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y23.000; Move to well plate 
;Begin Dispensing
G0 X120.700 Y23.000; Move to 96 well plate 
G0 Z28.850; Dispense Height at well 0 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y32.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 1 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y41.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 2 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y50.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 3 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y59.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 4 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y68.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 5 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y77.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 6 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y86.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 7 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y95.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 8 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y104.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 9 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y113.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 10 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X120.700 Y122.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 11 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y122.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 12 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y113.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 13 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y104.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 14 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y95.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 15 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y86.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 16 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y77.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 17 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y68.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 18 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y59.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 19 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y50.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 20 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y41.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 21 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E40.750; Aspirate 250.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y32.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 22 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y45.000; Go to 25mL reservoir 
G0 Z30.000; Aspiration height 
T0 ;select EZ-SEED tool 
G91 ;sets relative positioning
G0 E16.300; Aspirate 100.0 uL 
T1 ;select EZ-SEED tool 
G91 ;sets relative positioning
G0 E16.300; Aspirate 100.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X129.700 Y23.000; Move to well plate 
;Begin Dispensing
G0 Z28.850; Dispense Height at well 23 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
T1 ;select EZ-SEED tool 
G0 E-28.525; Dispense 175.0 uL 
G90 ;sets absolute positioning
G90 ;sets absolute positioning
G0 Z0.000; Present height 
G0 X65.000 Y0.000; Present 
