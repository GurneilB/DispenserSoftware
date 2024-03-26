import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("200x200")
root.title("FluidCAM")

# Add entry field for procedure name

# Storing the selection of the dropdowns
selections = {
    'plate': None,
    'insert': None,
    'reservoir': None
}
def update_selection(name, value):
    selections[name] = value #assigns a variable using user's choice

# Add Dropdowns
def dropdown(name, prompt, options):
    var = tk.StringVar(root)
    var.set(prompt) # default value
    def callback(value):
        update_selection(name, value)

    w = tk.OptionMenu(root, var, *options, command= callback)
    w.pack() #creates and packs dropdown menu

### Plate Size
opt_plate = ["6 well plate", "96 well plate"]
p_plate = ["Choose a tip type"]

dropdown('plate',p_plate, opt_plate)

### Insert type (is this needed?)
opt_insert = ["EZ-seed", "3-in-1"]
p_insert = ["Choose an insert type"]

dropdown('insert',p_insert, opt_insert)

### Reservoir size
opt_res = ["5mL", "25mL"]
p_res = ["Choose a reservoir type"]

dropdown('reservoir',p_res, opt_res)


#exit button

def on_exit():
    print(f"Selected plate size: {selections['plate']}")
    print(f"Selected insert size: {selections['insert']}")
    print(f"Selected reservoir size: {selections['reservoir']}")
    root.destroy()

button = tk.Button(root, text="Exit", command=on_exit)
button.pack()

# Tip Type

# Add Checkboxes for tip equip and tip eject

# Add "Run Procedure" Button (builds file)
# Add save "preferences button"

# Add in-program grid that simulates 96-well plate, saves as np matrix

# Add file menu items
# Add Save

# Preferences are saved as custom file format (create it)


root.mainloop()