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
G0 Z0.000 
G0 X65.000 Y0.000 
G4 S60 ; Dwell
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000 
G0 X6.000 Y49.000 
G0 Z45.000 
T0 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E250 
T1 ;select EZ-SEED tool 
G90 ;sets absolute positioning
G0 E250 
G90 ;sets absolute positioning
G0 Z18.000 
G0 X125.000 Y21.000 
G0 X125.000 Y21.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y30.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y39.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y48.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y57.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y66.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y75.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y84.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000 
G0 X6.000 Y49.000 
G0 Z45.000 
T2 ;select EZ-Seed tool 
G90 ;sets absolute positioning
G0 E250 
T2 ;select EZ-Seed tool 
G90 ;sets absolute positioning
G0 E250 
G90 ;sets absolute positioning
G0 Z18.000 
G0 X125.000 Y93.000 
;Begin Dispensing
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y102.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y111.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X125.000 Y120.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y120.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y111.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y102.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000 
G0 X6.000 Y49.000 
G0 Z45.000 
T2 ;select EZ-Seed tool 
G90 ;sets absolute positioning
G0 E250 
T2 ;select EZ-Seed tool 
G90 ;sets absolute positioning
G0 E250 
G90 ;sets absolute positioning
G0 Z18.000 
G0 X134.000 Y93.000 
;Begin Dispensing
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y84.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y75.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y66.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y57.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y48.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y39.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-50.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
;Begin Aspiration
G90 ;sets absolute positioning
G0 Z18.000 
G0 X6.000 Y49.000 
G0 Z45.000 
T2 ;select EZ-Seed tool 
G91 ;sets relative positioning
G0 E50.0 
T2 ;select EZ-Seed tool 
G91 ;sets relative positioning
G0 E50.0 
G90 ;sets absolute positioning
G0 Z18.000 
G0 X134.000 Y30.000 
;Begin Dispensing
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-25.0 
G90 ;sets absolute positioning
G0 Z30.000 
G0 X134.000 Y21.000 
G0 Z40.000 
G91 ;sets relative positioning
T2 ;select EZ-Seed tool 
G0 E-25.0 
T2 ;select EZ-Seed tool 
G0 E-50.0 
G90 ;sets absolute positioning
;Begin tip ejection
G90 ;sets absolute positioning
G0 Z18.000 
G0 X5.000 Y108.000 
G0 Z66.000 
G91 ;sets relative positioning
T2 ;select 0 tool 
G0 E-3 
G90 ;sets absolute positioning
G4 S2 ; Dwell
;Begin tip ejection
G90 ;sets absolute positioning
G0 Z18.000 
G0 X5.000 Y108.000 
G0 Z66.000 
G91 ;sets relative positioning
T2 ;select 1 tool 
G0 E-3 
G90 ;sets absolute positioning
G4 S2 ; Dwell
G90 ;sets absolute positioning
G0 Z0.000 
G0 X65.000 Y0.000 
