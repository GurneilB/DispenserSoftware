import tkinter as tk
from tkinter import messagebox

import json

# Create the main window
root = tk.Tk()
root.title("FluidCAM")
#root.configure(bg="white")

#Create a frame to fit everything
main_frame = tk.Frame(root) # Main frame to contain everything
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

controls_frame = tk.Frame(main_frame) # Frame for controls (buttons, dropdowns, entry fields)
controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

grid_frame = tk.Frame(main_frame) # Frame for the 8x12 grid
grid_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

# Storing the selection of the dropdowns
selections = {
    'name': None,
    'plate': None,
    'insert': None,
    'reservoir': None,
    'tip': None
}

# Add entry field for procedure name, should press enter key to save name
entry = tk.Entry(controls_frame, width=30)
entry.bind('<Return>', lambda event: update_selection('name', entry.get()))
entry.pack()

# Function to create a 8x12 grid of entry widgets
def create_grid(frame):
    for i in range(12):
        for j in range(8):
            entry = tk.Entry(frame, width=3, justify='center')
            entry.grid(row=i, column=j, padx=5, pady=5)

create_grid(grid_frame)

#assigns a variable using user's choice
def update_selection(name, value):
    selections[name] = value

# Add Dropdowns
def dropdown(name, prompt, options):
    var = tk.StringVar(controls_frame)
    var.set(prompt) # default value

    def callback(value): #can't be called outside
        update_selection(name, value)

    w = tk.OptionMenu(controls_frame, var, *options, command= callback)
    w.pack() #creates and packs dropdown menu

### Plate Size
opt_plate = ["6 well plate", "96 well plate"]
p_plate = ["Choose a tip type"]
dropdown('plate',p_plate, opt_plate)

### Insert type
opt_insert = ["none", "EZ-seed", "3-in-1"]
p_insert = ["Choose an insert type"]
dropdown('insert',p_insert, opt_insert)

### Reservoir size
opt_res = ["5mL", "25mL"]
p_res = ["Choose a reservoir type"]
dropdown('reservoir',p_res, opt_res)


### Tip Type
opt_tip = ["250mL"]
p_tip = ["Choose a tip type"]
dropdown('tip',p_tip, opt_tip)

# Add Checkboxes:
### Tip equip (only button, no saving)
CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(controls_frame, text="Press when tips are equipped",
                    fg="black",bd=10, variable=CheckVar1,
                    onvalue=1, offvalue=0)
C1.pack()

### Tip eject (only button, no saving)
CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(controls_frame, text="Press when ejection bowl is equipped",
                    fg="black", bd=10, variable=CheckVar2,
                    onvalue=1, offvalue=0)
C2.pack()

# Add "Run Procedure" Button (builds file)
# Add save "preferences button"

# Add in-program grid that simulates 96-well plate, saves as np matrix

# Add file menu items

# Add Save
def save_selections():
    # creates the filename name
    filename = f"{selections['name']}.json" if selections['name'] else "untitled.json"

    # Saves the updated list of selections to save.json
    with open(filename, "w") as file:
        json.dump(selections, file)
    messagebox.showinfo("Save", "Your Preferences are Saved")

save_button = tk.Button(root, text="Save Preferences", command=save_selections)
save_button.pack()


# exit button
def on_exit():
    print(f"Name of the Procedure: {selections['name']}")
    print(f"Last selected plate size: {selections['plate']}")
    print(f"Last selected insert size: {selections['insert']}")
    print(f"Last selected reservoir size: {selections['reservoir']}")
    root.destroy()

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()


root.mainloop()