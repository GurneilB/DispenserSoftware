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

# Add in-program grid that simulates 96-well plate, saves as np matrix
### GRID
entries = {}

def toggle_matrix(var):
    action = "0" if var.get() else ""
    for r in range(12):
        for c in range(8):
            entries[(r, c)].delete(0, tk.END)
            entries[(r, c)].insert(0, action)

# Create the all (fill grid with 0s) checkbox
all_var = tk.IntVar()
all_check = tk.Checkbutton(grid_frame, text="All", variable=all_var,
                            onvalue=1, offvalue=0, command=lambda: toggle_matrix(all_var))
all_check.grid(row=0, column=0)

for c in range(8):  # Create column checkboxes to fill with zeroes
    col_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=col_var,
                         onvalue=1, offvalue=0,
                         command=lambda col=c, var=col_var: toggle_col_zero(col, var))
    chk.grid(row=0, column=c+1)

for r in range(12):  # Create row checkboxes to fill with zeroes
    row_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=row_var,
                         onvalue=1, offvalue=0,
                         command=lambda row=r, var=row_var: toggle_row_zero(row, var))
    chk.grid(row=r+1, column=0)

# checks if checkbox is toggled or not, adapts the zeroes for it
def toggle_row_zero(r, var):
    action = "0" if var.get() else ""
    for c in range(8): entries[(r, c)].delete(0, tk.END); entries[(r, c)].insert(0, action)

def toggle_col_zero(c, var):
    action = "0" if var.get() else ""
    for r in range(12): entries[(r, c)].delete(0, tk.END); entries[(r, c)].insert(0, action)

# Creates a 12x8 grid of entry
for r in range(12):
    for c in range(8):
        entry = tk.Entry(grid_frame, width=5, justify='center')
        entry.grid(row=r+1, column=c+1)
        entries[(r, c)] = entry

###GRID end

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