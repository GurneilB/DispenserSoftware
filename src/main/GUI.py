import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("200x200")
root.title("FluidCAM")

# Add entry field for procedure name

# Add Dropdowns
def dropdown(prompt, options):
    var = tk.StringVar(root)
    var.set(prompt) # default value

    w = tk.OptionMenu(root, var, *options)
    w.pack() #creates and packs dropdown menu

# Plate Size
opt_plate = ["6 well plate", "96 well plate"]
p_plate = ["Choose a tip type"]

dropdown(p_plate, opt_plate)

# Insert type (is this needed?)
opt_insert = ["EZ-seed", "3-in-1"]
p_insert = ["Choose an insert type"]

dropdown(p_insert, opt_insert)

# Reservoir size
opt_res = ["5mL", "25mL"]
p_res = ["Choose a reservoir type"]

dropdown(p_res, opt_res)

# Tip Type

# Add Checkboxes for tip equip and tip eject

# Add "Run Procedure" Button (builds file)
# Add save button
# Add save "preferences button"

# Add in-program grid that simulates 96-well plate, saves as np matrix

# Add file menu items

# Preferences are saved as custom file format (create it)


root.mainloop()