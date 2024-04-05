# import src.main.BuildProcedure as bp
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import json
import csv
import src.main.Value as val
#import src.main.Program as program

# Create the main window
root = tk.Tk()
root.title("FluidCAM")

# Create a frame to fit everything
main_frame = tk.Frame(root)  # Main frame to contain everything
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

controls_frame = tk.Frame(main_frame)  # Frame for controls (buttons, dropdowns, entry fields)
controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

grid_frame = tk.Frame(main_frame)  # Frame for the 8x12 grid
grid_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

bottom_frame = tk.Frame(main_frame)  # This is a new frame for the bottom elements
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

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
    for r in range(12):  # Now loops through columns first
        for c in range(8):  # Then rows
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
    for r in range(12):  # Adjusted for new dimensions
        entries[(r, c)].delete(0, tk.END)
        entries[(r, c)].insert(0, fill_number)


# Variable to store the fill number from the entry box
fill = tk.StringVar()
# Label for the entry box
label = tk.Label(bottom_frame, text="Enter volume (in uL)\nto fill the grid:")
label.pack(side='top', anchor='e', padx=5)  # 'e' for east/right
# Specify number to be filled inside the grids
fill_number_entry = tk.Entry(bottom_frame, textvariable=fill, width=10)
fill_number_entry.pack(side='top', padx=0, pady=(0, 150))

# Create the "All" (fill grid with specified number) checkbox
all_var = tk.IntVar()
all_check = tk.Checkbutton(grid_frame, text="All", variable=all_var,
                           onvalue=1, offvalue=0, command=lambda: toggle_matrix(all_var))
all_check.grid(row=0, column=0)

# Create column checkboxes to fill with the specified number
for c in range(8):  # Adjusted loop for rows
    col_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=col_var,
                         onvalue=1, offvalue=0,
                         command=lambda col=c, var=col_var: toggle_col_zero(col, var))
    chk.grid(row=0, column=c + 2)

    # Add a label below each row checkbox
    letter =chr(72-c%8)
    label = tk.Label(grid_frame, text=f"{letter}")
    label.grid(row=1, column=c + 2)

# Create row checkboxes to fill with the specified number
for r in range(12):  # Adjusted loop for columns
    row_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=row_var,
                         onvalue=1, offvalue=0,
                         command=lambda row=r, var=row_var: toggle_row_zero(row, var))  # Adjusted command
    chk.grid(row=r + 2, column=0)  # Adjusted position

    # Add a label to the right of each column checkbox
    label = tk.Label(grid_frame, text=f"{r+1}")
    label.grid(row=r + 2, column=10)

# Create an 12x8 grid of entry widgets
for r in range(12):  # Adjusted loop for rows
    for c in range(8):  # Adjusted loop for columns
        entry = tk.Entry(grid_frame, width=5, justify='center')
        entry.grid(row=r + 2, column=c + 2)  # Adjusted position
        entries[(r, c)] = entry


###GRID end

# assigns a variable using user's choice
def update_selection(name, value):
    preference[name] = value


# Add procedure name, should press enter key to save name
pname_label = tk.Label(controls_frame, text="Enter procedure name:")
pname_label.pack()

pname = tk.Entry(controls_frame, width=30)
pname.pack()


# Add Dropdowns
def dropdown(name, prompt, options, message, callback=None):
    f = tk.Frame(controls_frame)  # Creates frame
    f.pack(fill='x', expand=True)

    mes = tk.Label(f, text=message)  # displays the message
    mes.grid(row=0, column=0, sticky='w', padx=5)

    var = tk.StringVar(f)
    var.set(prompt)  # default value

    def call(value):  # can't be called outside
        if callback:
            callback(value)
        update_selection(name, value)

    w = tk.OptionMenu(f, var, *options, command=call)
    w.grid(row=0, column=1)  # creates and packs dropdown menu

    f.grid_columnconfigure(1, weight=1)
    w.config(anchor='w')
    return var, w


# Implement the callback for updating insert options
def insert_opts(selected_plate_size):
    opt_insert = {
        "6 well plate": ["none", val.three_in_one],
        "96 well plate": ["none", val.ez_seed],
    }
    new_options = opt_insert.get(selected_plate_size, ["none"])  # Default to ["none"] if not found
    dropdown_insert['menu'].delete(0, 'end')  # Clears the current options from the insert type dropdown

    # update insert in preference
    def update_in(value):
        insert_var.set(value)
        update_selection('insert', value)

    # Add new options to the insert type dropdown
    for option in new_options:
        dropdown_insert['menu'].add_command(label=option, command=lambda value=option: update_in(value))
    # Update the displayed value to the first option of the new list
    insert_var.set(new_options[0])


### Plate Size
opt_plate = ["6 well plate", "96 well plate"]
p_plate = ["Choose a plate size"]
dropdown('plate', p_plate, opt_plate, "Plate Size:", insert_opts)

### Insert type
p_insert = ["Choose an insert type"]
insert_var, dropdown_insert = dropdown('insert', p_insert, ["none"], "Insert Type:")

### Reservoir size
opt_res = ["1.5", "5", "25"]
p_res = ["Choose a reservoir type"]
dropdown('reservoir', p_res, opt_res, "Reservoir Type (in mL):")

### Tip Type
opt_tip = [250]
p_tip = ["Choose a tip type"]
dropdown('tip', p_tip, opt_tip, "Tip Type (in uL):")


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
        is_filled = False
        for r in range(12):
            if entries[(r, col_start)].get() != '0' and entries[(r, col_end)].get() != '0':
                is_filled = True
                break
        # Update the color of the letter based on whether its columns are filled
        if is_filled:
            letter_labels[letter].config(fg="blue")
        else:
            letter_labels[letter].config(fg="grey")


# Message label
equip_label = tk.Label(bottom_frame, text="Equip tips at positions:")
equip_label.pack(pady=(10, 0))

# Add button to update tip selection
tips_equip = tk.Button(bottom_frame, text="Press for tips", command=tip_set)
tips_equip.pack()

# Frame for the letters
letters_frame = tk.Frame(bottom_frame)
letters_frame.pack()

# Letter labels
letters = ['A', 'B', 'C', 'D']
letter_labels = {}
for letter in letters:
    letter_labels[letter] = tk.Label(letters_frame, text=letter, fg="grey")
    letter_labels[letter].pack(side='left', expand=True)


# Updates Preference when checkbox is ticked
def update_equip():
    preference['equip'] = "TRUE" if CheckVar1.get() == 1 else None


CheckVar1 = tk.IntVar()

# Creates the checkbox
equip = tk.Checkbutton(controls_frame, text="Auto-Equip Tips",
                       fg="black", variable=CheckVar1,
                       onvalue=1, offvalue=0, command=update_equip)
equip.pack()


# Tip ejection bowl equipped
def update_eject():
    preference['eject'] = "TRUE" if CheckVar2.get() == 1 else None


CheckVar2 = tk.IntVar()

eject = tk.Checkbutton(controls_frame, text="Auto-Eject Tips",
                       fg="black", variable=CheckVar2,
                       onvalue=1, offvalue=0, command=update_eject)
eject.pack()


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


# Add Run Procedure
# def run_procedure():
#     save_preference()
#     # Filename based on the procedure name and defaults to "untitled.json" if not provided.
#     filename = f"{preference['name']}.json" if preference['name'] else "untitled.json"
#
#     try:
#         with open(filename, "r") as file:
#             data = json.load(file)
#
#         # Extract variables for build_procedure from the .json
#         name = data.get('name')
#         plate = data.get('plate')
#         insert = data.get('insert')
#         tip = int(data.get('tip'))
#         vol_array = data.get('grid')
#         restype = data.get('reservoir')
#         equip_ = data.get('equip')
#         eject_ = data.get('eject')
#
#         # Calls program
#         program.gui(name, plate, insert, restype, tip, vol_array, equip_, eject_)
#
#         messagebox.showinfo("Procedure Run", "File Saved")
#     except FileNotFoundError:
#         messagebox.showerror("File Not Found", f"Could not find the file: {filename}")


#run_procedure_button = tk.Button(root, text="Generate Procedure", command=lambda: run_procedure())
#run_procedure_button.pack()


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


# Import csv file
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
                messagebox.showwarning("Invalid File",
                                       "Please submit an appropriate csv file with a 12x8 matrix or smaller.")
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
import_button = tk.Button(bottom_frame, text="Import CSV File", command=import_csv_file)
import_button.pack(side=tk.LEFT, padx=10, pady=10)  # Pack to the left side of the bottom_frame

root.mainloop()
