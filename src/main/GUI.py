import src.main.BuildProcedure as bp
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import json
import csv

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

# Storing all the user preferences
preference = {
    'name': None,
    'plate': None,
    'insert': None,
    'reservoir': None,
    'tip': None,
    'equip': None,
    'eject': None,
    'grid': None
}

# Add in-program grid that simulates 96-well plate, saves as np matrix
### GRID
entries = {}

# Function to toggle the entire matrix
def toggle_matrix(var):
    fill_number = fill.get() if var.get() and fill.get() else ""
    for r in range(12):
        for c in range(8):
            entries[(r, c)].delete(0, tk.END)
            entries[(r, c)].insert(0, fill_number)

# Function to toggle a row
def toggle_row_zero(r, var):
    fill_number = fill.get() if var.get() and fill.get() else ""
    for c in range(8):
        entries[(r, c)].delete(0, tk.END)
        entries[(r, c)].insert(0, fill_number)

# Function to toggle a column
def toggle_col_zero(c, var):
    fill_number = fill.get() if var.get() and fill.get() else ""
    for r in range(12):
        entries[(r, c)].delete(0, tk.END)
        entries[(r, c)].insert(0, fill_number)

# Variable to store the fill number from the entry box
fill = tk.StringVar()
# Specify number to be filled inside the grids
fill_number_entry = tk.Entry(controls_frame, textvariable=fill, width=10)
fill_number_entry.pack(side='bottom', anchor='e', padx=5, pady=(5, 0))
# Label for the entry box
label = tk.Label(controls_frame, text="Enter volume (in uL)\nto fill the grid:")
label.pack(side='bottom', anchor='e', padx=5, pady=(0, 5))  # 'e' for east/right


# Create the "All" (fill grid with specified number) checkbox
all_var = tk.IntVar()
all_check = tk.Checkbutton(grid_frame, text="All", variable=all_var,
                           onvalue=1, offvalue=0, command=lambda: toggle_matrix(all_var))
all_check.grid(row=0, column=0)

# Create column checkboxes to fill with the specified number
for c in range(8):
    col_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=col_var,
                         onvalue=1, offvalue=0,
                         command=lambda col=c, var=col_var: toggle_col_zero(col, var))
    chk.grid(row=0, column=c+1)

# Create row checkboxes to fill with the specified number
for r in range(12):
    row_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=row_var,
                         onvalue=1, offvalue=0,
                         command=lambda row=r, var=row_var: toggle_row_zero(row, var))
    chk.grid(row=r+1, column=0)

# Create a 12x8 grid of entry widgets
for r in range(12):
    for c in range(8):
        entry = tk.Entry(grid_frame, width=5, justify='center')
        entry.grid(row=r+1, column=c+1)
        entries[(r, c)] = entry
###GRID end

#assigns a variable using user's choice
def update_selection(name, value):
    preference[name] = value

# Add procedure name, should press enter key to save name
pname_label = tk.Label(controls_frame, text="Enter procedure name:")
pname_label.pack() 

pname = tk.Entry(controls_frame, width=30)
pname.pack()

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
opt_insert = ["none", "EZ-SEED", "3-IN-1"]
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

### Tip equipped
def tip_set():
    # Fill empty cells with '0's
    for r in range(12):
        for c in range(8):
            if entries[(r, c)].get() == '':
                entries[(r, c)].delete(0, tk.END)
                entries[(r, c)].insert(0, '0')

    # Initialize all letters to light grey (assuming no columns are filled)
    for label in letter_labels.values():
        label.config(fg="grey")

    # Mapping each letter to its corresponding columns
    column_pairs = {
        'A': (0, 1),
        'B': (2, 3),
        'C': (4, 5),
        'D': (6, 7)
    }

    # Check each pair of columns in the grid to determine if they are filled
    for letter, (col_start, col_end) in column_pairs.items():
        is_filled = True
        for r in range(12):
            if entries[(r, col_start)].get() == '0' and entries[(r, col_end)].get() == '0':
                is_filled = False
                break
        # Update the color of the letter based on whether its columns are filled
        if is_filled:
            letter_labels[letter].config(fg="blue")
        else:
            letter_labels[letter].config(fg="grey")

# Message label
equip_label = tk.Label(controls_frame, text="Equip tips at positions:")
equip_label.pack(pady=(10,0))

#Add button to update tip selection
tips_equip=tk.Button(controls_frame, text="Press for tips", command=tip_set)
tips_equip.pack()

#Frame for the letters
letters_frame = tk.Frame(controls_frame)
letters_frame.pack()

#Letter labels
letters = ['A', 'B', 'C', 'D']
letter_labels = {}
for letter in letters:
    letter_labels[letter]= tk.Label(letters_frame, text= letter, fg="grey")
    letter_labels[letter].pack(side='left', expand=True)

# Updates Preference when checkbox is ticked
def update_equip():
    preference['equip'] = "TRUE" if CheckVar1.get() == 1 else None
CheckVar1 = tk.IntVar()
#Creates the checkbox
equip = tk.Checkbutton(controls_frame, text="Press when tips are equipped",
                    fg="black", bd=10, variable=CheckVar1,
                    onvalue=1, offvalue=0, command=update_equip)
equip.pack()

### Tip ejection bowl equipped
def update_eject():
    preference['eject'] = "TRUE" if CheckVar2.get() == 1 else None
CheckVar2 = tk.IntVar()

eject = tk.Checkbutton(controls_frame, text="Press when ejection bowl is equipped",
                    fg="black", bd=10, variable=CheckVar2,
                    onvalue=1, offvalue=0, command=update_eject)
eject.pack()


# Add "Run Procedure" Button (builds file)

# Add file menu items

# Add Save
def save_preference():
    # Temporarily capture the state of the grid to check validity
    grid = [[entries[(r, c)].get() for c in range(8)] for r in range(12)]

    # Check the matrix for a string or a number above 1000 in any of the cells
    if any(True for row in grid for cell in row if not cell.isdigit() or int(cell) > 1000):
        messagebox.showwarning("Invalid Grid Input", "Please ensure all volumes are between 0 and 1000uL.")
    else:
        # updates the 'grid' in preference otherwise
        update_selection('grid', grid)
   
        # Capture name and save it
        update_selection('name', pname.get())

        # creates the filename name
        filename = f"{preference['name']}.json" if preference['name'] else "untitled.json"

        # Saves the updated list of preference to save.json
        with open(filename, "w") as file:
            json.dump(preference, file)
        messagebox.showinfo("Save", "Your Preferences are Saved")

save_button = tk.Button(root, text="Save Preferences", command=save_preference)
save_button.pack()

#Add Run Procedure
def run_procedure():
    # Filename based on the procedure name and defaults to "untitled.json" if not provided.
    filename = f"{preference['name']}.json" if preference['name'] else "untitled.json"

    try:
        with open(filename, "r") as file:
            data = json.load(file)

        # Extract variables for build_procedure from the .json
        name = data.get('name', 'untitled')
        insert = data.get('insert', 'none')
        tip = int(data.get('tip', 250))
        vol_array = data.get('grid', [[]])
        restype = data.get('reservoir', '5mL')
        r_vol = data.get('reservoir', '5mL')  #unsure

        # Calls build_procedure
        bp.build_procedure(name, r_vol, insert, tip, vol_array, restype)

        messagebox.showinfo("Procedure Run", "Procedure has been successfully run.")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"Could not find the file: {filename}")


run_procedure_button = tk.Button(root, text="Run Procedure", command=lambda: run_procedure())
run_procedure_button.pack()

# exit button
def on_exit():
    print(f"Name of the Procedure: {preference['name']}")
    print(f"Last selected plate size: {preference['plate']}")
    print(f"Last selected insert size: {preference['insert']}")
    print(f"Last selected reservoir size: {preference['reservoir']}")
    print(f"Last entered grid: {preference['grid']}")
    root.destroy()

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()


###Import csv file
def import_csv_file():
    # Specify the options for opening the dialog
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filename = filedialog.askopenfilename(title="Open a file", initialdir="/", filetypes=filetypes)
    
    # Check if a file was selected (filename will not be empty)
    if filename:
        # Reads the CSV file
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            matrix = list(reader)
            
            # Checks if the matrix exceeds 12x8 dimensions
            if len(matrix) > 12 or any(len(row) > 8 for row in matrix):
                messagebox.showwarning("Invalid File", "Please submit an appropriate csv file with a 12x8 matrix or smaller.")
                return  # Stop processing this file
            
            # Populates the grid with the matrix values or zeros
            for r in range(12):
                for c in range(8):
                    entries[(r, c)].delete(0, tk.END)
                    if r < len(matrix) and c < len(matrix[r]):
                        entries[(r, c)].insert(0, matrix[r][c])
                    else:
                        entries[(r, c)].insert(0, "0")

# Create a bottom frame (like controls and grid frames)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Create the "Import .csv File" button
import_button = tk.Button(bottom_frame, text="Import .csv File", command=import_csv_file)
import_button.pack(side=tk.LEFT, padx=10, pady=10)  # Pack to the left side of the bottom_frame



root.mainloop()