;FLAVOR: Repetier
;RESERVOIR TYPE: 25000.0
;NUMBER: 1
;TIP TYPE: 250uL
;NUMBER: 2
;PLATE TYPE: 96
;INSERT TYPE: EZ-SEED
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G21 ;sets units to mm
G28 ;home
G90 ;sets absolute positioning
G0 Z0.000; Present height 
G0 X65.000 Y0.000; Present 
G204 P0 S0
G204 P1 S0
G204 P0 S1
G205 P0
G204 P0 S0
G204 P1 S1
G205 P1
G204 P1 S0
@pause
T0
G92 E0
G1 E17
G92 E0
T1
G92 E0
G1 E17
G92 E0
G204 P0 S0
G204 P1 S0
@pause ; Load Stage and Continue
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X6.000 Y49.000; Move to 25mL reservoir 
G0 Z45.000; Aspiration height 
T0 ;select EZ-SEED tool 
G91 ;sets relative positioning
G92 E0 ;Reset Position
G0 E9.780; Aspirate 60.0 uL 
T1 ;select EZ-SEED tool 
G91 ;sets relative positioning
G92 E0 ;Reset Position
G0 E0.000; Aspirate 0.0 uL 
G90 ;sets absolute positioning
G0 Z18.000; Move height 
G0 X125.000 Y21.000; Move to well plate 
G0 X125.000 Y21.000; Move to 96-well plate 
;Begin Dispensing
G0 Z40.000; Dispense Height at well 0 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y30.000; Move to next well 
G0 Z40.000; Dispense Height at well 1 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y39.000; Move to next well 
G0 Z40.000; Dispense Height at well 2 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y48.000; Move to next well 
G0 Z40.000; Dispense Height at well 3 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y57.000; Move to next well 
G0 Z40.000; Dispense Height at well 4 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y66.000; Move to next well 
G0 Z40.000; Dispense Height at well 5 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y75.000; Move to next well 
G0 Z40.000; Dispense Height at well 6 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y84.000; Move to next well 
G0 Z40.000; Dispense Height at well 7 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y93.000; Move to next well 
G0 Z40.000; Dispense Height at well 8 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y102.000; Move to next well 
G0 Z40.000; Dispense Height at well 9 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y111.000; Move to next well 
G0 Z40.000; Dispense Height at well 10 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X125.000 Y120.000; Move to next well 
G0 Z40.000; Dispense Height at well 11 
G91 ;sets relative positioning
T0 ;select EZ-SEED tool 
G0 E-0.815; Dispense 5.0 uL 
T1 ;select EZ-SEED tool 
G0 E-0.000; Dispense 0.0 uL 
G90 ;sets absolute positioning
G0 Z30.000; Move height 
G0 X134.000 Y21.000; Move to next well 
G90 ;sets absolute positioning
G0 Z0.000; Present height 
G0 X65.000 Y0.000; Present 
