import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os
import numpy as np
import json
import csv
import Value as val
import ConfigCalibration as calval
import Program as program
import Calculations as calc
import xml.etree.ElementTree as ET

""" Generates GUI for dispenser software, called FluidCAM """


def toggle_matrix(var):
    """
    Fills entire matrix with value

    :param var: value to fill matrix
    """

    fill_number = fill.get() if var.get() and fill.get() else ""

    # Loop through rows
    for r in range(12):

        # Loop through columns
        for c in range(8):
            # Fill entry with var
            entries[(r, c)].delete(0, tk.END)
            entries[(r, c)].insert(0, fill_number)


def toggle_row_zero(r, var):
    """
    Fills entire matrix row with value

    :param r: row number
    :param var: value to fill matrix
    """

    fill_number = fill.get() if var.get() and fill.get() else ""

    # Loop through each column
    for c in range(8):
        # Fill entry with var
        entries[(r, c)].delete(0, tk.END)
        entries[(r, c)].insert(0, fill_number)


def toggle_col_zero(c, var):
    """
    Fills entire matrix column with value

    :param c: column number
    :param var: value to fill matrix
    """

    fill_number = fill.get() if var.get() and fill.get() else ""

    # Loop through each row
    for r in range(12):
        # Fill entry with var
        entries[(r, c)].delete(0, tk.END)
        entries[(r, c)].insert(0, fill_number)


def update_selection(name, value):
    """
    Updates preference dictionary with value

    :param name: key
    :param value: value
    """

    preference[name] = value


def dropdown(name, prompt, options, message, var, callback=None, selection_callback=None):
    """
    Creates dropdown widgets

    :param name: Preference dictionary key
    :param prompt: Initial value for dropdown
    :param options: All optional values for dropdown
    :param message: Message in dropdown
    :param var:
    :param callback:
    :param selection_callback:
    """

    # Create frame
    f = tk.Frame(controls_frame)
    f.pack(fill='x', expand=True)

    # display the message
    mes = tk.Label(f, text=message)
    mes.grid(row=0, column=0, sticky='w', padx=5)

    # default value
    var.set(prompt)

    def call(value):
        if callback:
            callback(value)
        update_selection(name, value)
        if selection_callback:  # new callback after selection
            selection_callback(value)

    # Create and pack dropdown menu
    w = tk.OptionMenu(f, var, *options, command=call)
    w.grid(row=0, column=1)

    f.grid_columnconfigure(1, weight=1)
    w.config(anchor='w')

    return w


def insert_opts(selected_plate_size):
    """
    Updates insert dropdowns for selected plate size

    :param selected_plate_size: Plate Size
    """

    # Insert options for each plate size
    opt_insert = {
        "6 well plate": ["none", val.three_in_one],
        "96 well plate": ["none", val.ez_seed],
    }

    # Default to ["none"] if not found
    new_options = opt_insert.get(selected_plate_size, ["none"])

    # Access the menu of the OptionMenu widget
    menu = dropdown_insert['menu']

    # Clear current options
    menu.delete(0, 'end')

    # update insert in preference
    def update_in(value):
        """
        Updates insert key in preferences dictionary

        :param value: Value to update insert key with
        """

        insert_var.set(value)
        update_selection('insert', value)

    # Add new options to the insert type dropdown
    for option in new_options:
        dropdown_insert['menu'].add_command(label=option, command=lambda value=option: update_in(value))

    # Update the displayed value to the first option of the new list
    insert_var.set(new_options[0])


def greying(value):
    """
    Disables Equip Tip Checkbox

    :param value: Reservoir selection
    """

    # Disable checkbox for 25mL reservoir
    if value == "25":
        equip.config(state=tk.DISABLED)  # Disables the checkbox
        CheckVar1.set(0)  # also unchecks it
    else:
        equip.config(state=tk.NORMAL)


def tip_set(protocol):
    """
    Displays procedure active tips for user

    :param protocol: Procedure protocol
    """

    # 4-Tip 96 well Protocol, Activate all tips
    if protocol == val._4_tip_96well_protocol:
        for letter_ in letters:
            letter_labels[letter_].config(fg="blue")

    # 2-Tip 96 well Protocol, activate Tips A and C
    elif protocol == val._2_tip_96well_protocol:
        for letter_ in letters:
            letter_labels[letter_].config(fg="grey")
        letter_labels['A'].config(fg="blue")
        letter_labels['C'].config(fg="blue")


def update_equip():
    """
    Updates equip key value in preference when checkbox is ticked
    """
    preference['equip'] = True if CheckVar1.get() == 1 else False


def update_eject():
    """
    Updates eject key value in preference when checkbox is ticked
    """
    preference['eject'] = True if CheckVar2.get() == 1 else False


def check_preference(pref):
    """
    Checks dictionary values are all non-None Type

    :param pref: user preferences dictionary
    :return: True if one or more values are None
    """
    for i in pref:
        if pref[i] is None:
            return True

    return False


def import_csv_file():
    """
    Imports contents of .csv file into GUI volumetric plate design
    """

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

def run_procedure():
    """
    Checks validity of procedure, generates G-code file
    """

    # Save user preferences, suppress confirmation message
    if save_preference(True) is False:
        return

    # Filename based on the procedure name and defaults to "untitled.json" if not provided.
    filename = f"{preference['name']}.json" if preference['name'] else "untitled.json"

    try:
        with open(filename, "r") as file:
            data = json.load(file)

        # Extract variables for build_procedure from the .json
        name = data.get('name')
        plate = data.get('plate')
        insert = data.get('insert')
        tip = int(data.get('tip'))
        vol_array = np.array(data.get('grid')).astype(np.float_)
        restype = data.get('reservoir')
        equip_ = data.get('equip')
        eject_ = data.get('eject')

        # Check if total procedure volume is compatible with 1.5 mL tubes (if applicable)
        if restype == "1.5" and calc.get_protocol(vol_array) == val._2_tip_96well_protocol:
            if np.sum(vol_array[:, [0, 1, 2, 3]]) > 3000 or np.sum(vol_array[:, [4, 5, 6, 7]]) > 3000:
                messagebox.showerror("Volume Error", "Total culture plate volume is too large for reservoir")
                return

        elif restype == "1.5" and calc.get_protocol(vol_array) == val._4_tip_96well_protocol:
            if (np.sum(vol_array[:, [0, 1]]) > 3000 or np.sum(vol_array[:, [2, 3]]) > 3000
                    or np.sum(vol_array[:, [4, 5]]) > 3000 or np.sum(vol_array[:, [6, 7]]) > 3000):
                messagebox.showerror("Volume Error", "Total culture plate volume is too large for reservoir")
                return

        # Check if tip is being equipped with 25mL reservoir on stage
        if restype == "25" and equip_:
            messagebox.showerror("Setup Error", "Cannot Auto-Equip Tips with 25mL Reservoir")
            return

        # Calls program to develop gcode file
        res_volumes = program.gui(name, plate, insert, restype, tip, vol_array, equip_, eject_)

        # Display Tip Arrangement
        protocol = calc.get_protocol(vol_array)
        tip_set(protocol)

        # Display Reservoir Volumes and Arrangement
        if restype == "25":
            volumes.config(text="%.3f mL" % (sum(res_volumes) / 1000), fg="blue")
        elif restype == "1.5":
            converted_vol = [x / 1000 for x in res_volumes]
            volumes.config(text="(mL)\nRow A:   %.3f   %.3f   %.3f   %.3f\nRow B:   %.3f   %.3f   %.3f   %.3f"
                                % (converted_vol[3], converted_vol[2], converted_vol[1], converted_vol[0],
                                   converted_vol[7], converted_vol[6], converted_vol[5], converted_vol[4]),
                           fg="blue")

        # Get the current working directory
        current_directory = os.getcwd()

        # Ask user to select the destination folder
        destination_folder = filedialog.askdirectory(title="Select destination folder")

        # Check if the user selected a destination folder
        if destination_folder:
            source_path = os.path.join(current_directory, f"{name}.gcode")

            # Move the file to the destination folder
            destination_path = os.path.join(destination_folder, f"{name}.gcode")
            shutil.move(source_path, destination_path)
            messagebox.showinfo("Procedure Run", "Preferences and Procedure Saved")
        else:
            messagebox.showwarning("Save Error", "No destination folder selected.")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", f"Could not find the file: {filename}")


# *****Add documentation*****
def save_preference(suppress_message: bool = False):

    """
    Saves user preferences to current working directory
    """

    # Fill empty cells with '0's
    for r in range(12):
        for c in range(8):
            if entries[(r, c)].get() == '':
                entries[(r, c)].delete(0, tk.END)
                entries[(r, c)].insert(0, '0')

    # Temporarily capture the state of the grid to check validity
    grid = [[entries[(r, c)].get() for c in range(8)] for r in range(12)]

    # Check the matrix for a string or a number above 1000 in any of the cells
    if any(True for row in grid for cell in row if not cell.isdigit() or int(cell) > 200):
        messagebox.showwarning("Volume Error", "Please ensure all volumes are between 20 and 200uL, or 0.")
        return False
    else:
        # updates the 'grid' in preference otherwise
        update_selection('grid', grid)

        # Capture name and save it
        update_selection('name', pname.get())

        # creates the filename name
        filename = f"{preference['name']}.json" if preference['name'] else "untitled.json"

        if check_preference(preference):
            messagebox.showwarning("Incomplete Procedure", "Please Select All Preferences")
            return False

        # Saves the updated list of preference to save.json
        with open(filename, "w") as file:
            json.dump(preference, file)
        if suppress_message:
            pass
        else:
            messagebox.showinfo("Save", "Preferences Saved")


""" LOAD PREFERENCES START """


def load_pref(filename):
    """
    Loads previously saved user preferences into GUI

    :param filename: JSON file with user preferences
    """
    # filetypes = [('JSON files', '*.json'), ('All files', '*.*')]
    # filename = filedialog.askopenfilename(title='Open Preferences .json File', initialdir="/", filetypes=filetypes)

    if filename:
        with open(filename, 'r') as file:
            loaded_pref = json.load(file)
        global preference
        preference.update(loaded_pref)

    # updating procedure name
    pname.delete(0, tk.END)
    pname.insert(0, preference.get('name', ''))

    # updating dropdowns
    global plate_var, insert_var, reservoir_var, tip_var
    plate_var.set(preference.get('plate', 'Choose a plate size'))
    insert_var.set(preference.get('insert', 'Choose an insert type'))
    reservoir_var.set(preference.get('reservoir', 'Choose a reservoir type'))
    tip_var.set(str(preference.get('tip', 'Choose a tip type')))

    # updating checkboxes
    CheckVar1.set(1 if preference.get('equip') == "TRUE" else 0)
    CheckVar2.set(1 if preference.get('eject') == "TRUE" else 0)

    # updating grid
    grid_values = preference.get('grid', [])  # Default to an empty list if 'grid' key is not found
    for r, row in enumerate(grid_values):
        for c, cell_value in enumerate(row):
            if r < 12 and c < 8:  # Ensure within grid bounds
                entry = entries[(r, c)]
                entry.delete(0, tk.END)
                entry.insert(0, cell_value)


def open_preferences():
    """
    Creates load preferences window
    """
    def select_preference():
        """
        Activates load_pref function on selection
        """

        # Checks if list item is selected
        if pref_listbox.curselection():

            # Get selection, load preference, close window
            selected_preference = pref_files[pref_listbox.curselection()[0]]
            load_pref(selected_preference + ".json")
            preference_window.destroy()
        else:
            pass

    # Initiate pop-up window
    preference_window = tk.Toplevel(root)

    # Title for the pop-up window
    preference_window.title("Load Preferences")

    # Pop-up window label
    pref_label = tk.Label(preference_window, text="Load Preferences", font=("Helvetica", 18, "bold"))
    pref_label.pack(padx=10, pady=7)
    pref_sublabel = tk.Label(preference_window, text="Select Previously Saved Preferences", font=("Helvetica", 13, "italic"))
    pref_sublabel.pack(padx=10)

    # Create Listbox
    pref_listbox = tk.Listbox(preference_window, selectmode=tk.SINGLE)
    pref_listbox.pack(pady=10)

    # Get contents for preferences listbox
    pref_files = []

    for file in os.listdir(os.getcwd()):

        # Check if the file has the specified extension
        if file.endswith(".json"):

            # Add the file to the list
            pref_files.append(file.rsplit(".", 1)[0])

    for item in pref_files:
        pref_listbox.insert(tk.END, item)

    load_pref_button = tk.Button(preference_window, text="Load", command=select_preference)
    load_pref_button.pack(pady=10)

    # Bind the select_preference function to the listbox
    pref_listbox.bind("<<ListboxSelect>>", select_preference())


""" LOAD PREFERENCES END """

""" CALIBRATION SETTINGS START """


def value_to_xml():
    """
    Stores default coordinates inside calibration XML file
    """
    root_ = ET.Element("CalibrationValues")

    # Get and store default coordinates for each element
    ET.SubElement(root_, "plate_96", x=str(calval.plate_96[0]), y=str(calval.plate_96[1]),
                  z=str(calval.dispense_height_EZ),
                  z_movement=str(calval.plate96_movement_height))
    ET.SubElement(root_, "plate_6", x=str(calval.plate_6[0]), y=str(calval.plate_6[1]),
                  z=str(calval.dispense_height_3in1),
                  z_movement=str(calval.plate6_movement_height))
    ET.SubElement(root_, "pos_reservoir_25ml", x=str(calval.pos_reservoir_25ml[0]), y=str(calval.pos_reservoir_25ml[1]),
                  z=str(calval.aspirate_height_25ml), z_movement=str(calval.movement_height_25mL))
    ET.SubElement(root_, "tubes4tips", x=str(val.tubes4tips[0][0]), y=str(val.tubes4tips[0][1]),
                  z=str(calval.aspirate_height_1_5ml), z_movement=str(calval.movement_height_1_5ml))
    ET.SubElement(root_, "eject_bowl", x=str(calval.eject_bowl[0]), y=str(calval.eject_bowl[1]),
                  z=str(calval.eject_height))
    ET.SubElement(root_, "tip_tray_8", x=str(calval.tip_tray_8[0]), y=str(calval.tip_tray_8[1]),
                  z=str(calval.equip_height))

    tree = ET.ElementTree(root_)
    tree.write("calibration_values.xml")


def save_updates():
    """
    Saves changes inside calibration XML file
    """
    global entries_
    root_ = ET.Element("CalibrationValues")

    for tag, ents in entries_.items():

        # Start building the element with x and y, which are always present
        elem_attribs = {
            'x': ents[0].get() or "0",
            'y': ents[1].get() or "0",
            'z': ents[2].get().strip() or "0"}

        # Check if there's a zmove value to add
        if len(ents) > 3:
            elem_attribs['z_movement'] = ents[3].get() or "0"

        # Create the XML element with the appropriate attributes
        ET.SubElement(root_, tag, **elem_attribs)

    tree = ET.ElementTree(root_)
    tree.write("calibration_values.xml")
    toggle_entries("normal")


def toggle_entries(state):
    """
    Deactivates/Activates Calibration entry boxes on command

    :param state: Activation state
    """
    global entries, save_button
    # If currently readonly, switch to editable
    if state == "readonly":
        newState = "normal"
        buttonText = "Save"

        # Call save_updates when button is clicked
        commandAction = save_updates

    # If currently editable (normal), switch back to readonly
    else:
        newState = "readonly"
        buttonText = "Edit Coordinates"

        # Toggle back to readonly
        commandAction = lambda: toggle_entries("readonly")

    # Apply the state change to entries
    for ents in entries_.values():

        # Iterate over each widget in the tuple
        for entry in ents:
            entry.config(state=newState)

    # Update save_button text and bind the appropriate action
    save_button.config(text=buttonText, command=commandAction)


def calibration():
    """
    Create Calibration Settings Window
    """
    # Creates calibration_values.xml if it doesn't exist
    if not os.path.exists("calibration_values.xml"):
        value_to_xml()

    global entries_, save_button
    cal_window = tk.Toplevel(root)
    cal_window.title("Positional Calibration Settings")

    # Parse the XML and get its root element
    tree = ET.parse('calibration_values.xml')
    xml_root = tree.getroot()

    # Dictionary to keep track of text entries for each value
    entries_ = {}
    custom_label = {
        "plate_96": "96-Well Plate",
        "plate_6": "6-Well Plate",
        "pos_reservoir_25ml": "25ml Reservoir",
        "tubes4tips": "1.5mL Reservoir",
        "eject_bowl": "Ejection Bowl",
        "tip_tray_8": "8 Tip Tray"
    }
    row_index = 0

    # Loop through each calibration value in the XML
    for elem in xml_root:
        label_text = custom_label.get(elem.tag)
        label = tk.Label(cal_window, text=label_text, font=("Helvetica", 10, "bold"))
        label.grid(row=row_index, column=0, columnspan=9, sticky='ew', pady=(10, 0))
        row_index += 1

        x_label = tk.Label(cal_window, text="X:")
        x_label.grid(row=row_index, column=1, sticky='e')
        entry_x = tk.Entry(cal_window)
        entry_x.grid(row=row_index, column=2)

        y_label = tk.Label(cal_window, text="Y:")
        y_label.grid(row=row_index, column=3, sticky='e')
        entry_y = tk.Entry(cal_window)
        entry_y.grid(row=row_index, column=4)

        z_label = tk.Label(cal_window, text="Z:")
        z_label.grid(row=row_index, column=5, sticky='e')
        entry_z = tk.Entry(cal_window)
        entry_z.grid(row=row_index, column=6)

        # Insert coordinates into Entry widgets
        entry_x.insert(0, elem.attrib.get('x', '0'))  # Default to '0' if attribute is missing
        entry_y.insert(0, elem.attrib.get('y', '0'))  # Default to '0' if attribute is missing
        entry_z.insert(0, elem.attrib.get('z', '0'))

        # Change to "readonly" after the window is updated
        cal_window.after(1, lambda entry=entry_x: entry.config(state="readonly"))
        cal_window.after(1, lambda entry=entry_y: entry.config(state="readonly"))
        cal_window.after(1, lambda entry=entry_z: entry.config(state="readonly"))

        if elem.tag not in ["eject_bowl", "tip_tray_8"]:
            zmove_label = tk.Label(cal_window, text="Z-movement:")
            zmove_label.grid(row=row_index, column=7, sticky='e')
            entry_zmove = tk.Entry(cal_window)
            entry_zmove.grid(row=row_index, column=8)

            entry_zmove.insert(0, elem.attrib.get('z_movement', '0'))  # Default to '0' if attribute is missing

            cal_window.after(1, lambda entry=entry_zmove: entry.config(state="readonly"))

            # Adds these elements to entries
            entries_[elem.tag] = (entry_x, entry_y, entry_z, entry_zmove)
        else:
            entries_[elem.tag] = (entry_x, entry_y, entry_z)

        row_index += 2

    # Save button to update XML with new values
    save_button = tk.Button(cal_window, text="Edit Coordinates", command=lambda: toggle_entries("readonly"))
    save_button.grid(row=row_index, column=0, columnspan=9, pady=(10, 0))


""" CALIBRATION SETTINGS END """


def on_exit():
    """
    Prints preferences to console and closes window
    """
    print(f"Name of the Procedure: {preference['name']}")
    print(f"Last selected plate size: {preference['plate']}")
    print(f"Last selected insert size: {preference['insert']}")
    print(f"Last selected reservoir size: {preference['reservoir']}")
    print(f"Last entered grid: {preference['grid']}")
    root.destroy()


""" GUI START """

# Create the main window
root = tk.Tk()
root.title("FluidCAM")

# Master Frame
main_frame = tk.Frame(root)  # Main frame to contain everything
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Frame for controls (buttons, dropdowns, entry fields)
controls_frame = tk.Frame(main_frame)
controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

# Frame for the 12x8 grid
grid_frame = tk.Frame(main_frame)
grid_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

# Frame for the bottom elements
bottom_frame = tk.Frame(main_frame)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

"""CULTURE PLATE GRID START"""

# in-program grid that simulates 96-well plate, saves as np matrix
entries = {}

# Entry field to set multiple well volumes at once
fill = tk.StringVar()  # Variable to store the fill number from the entry box
label = tk.Label(bottom_frame, text="Enter volume (in uL)\nto fill the grid:")  # Label for the entry box
label.pack(side='top', padx=5)  # 'e' for east/right
fill_number_entry = tk.Entry(bottom_frame, textvariable=fill, width=10)  # Specify number to be filled inside the grids
fill_number_entry.pack(side='top', padx=0, pady=(0, 150))

# Create Set All checkbox to fill with specified number
all_var = tk.IntVar()
all_check = tk.Checkbutton(grid_frame, text="Set All", variable=all_var,
                           onvalue=1, offvalue=0, command=lambda: toggle_matrix(all_var))
all_check.grid(row=0, column=0)

# Create column checkboxes to fill with the specified number
for c in range(8):
    col_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=col_var,
                         onvalue=1, offvalue=0,
                         command=lambda col=c, var=col_var: toggle_col_zero(col, var))
    chk.grid(row=0, column=c + 2)

    # Add a label below each column checkbox
    letter = chr(65 + c % 8)
    label = tk.Label(grid_frame, text=f"{letter}")
    label.grid(row=1, column=c + 2)

# Create row checkboxes to fill with the specified number
for r in range(12):
    row_var = tk.IntVar()
    chk = tk.Checkbutton(grid_frame, variable=row_var,
                         onvalue=1, offvalue=0,
                         command=lambda row=r, var=row_var: toggle_row_zero(row, var))  # Adjusted command
    chk.grid(row=r + 2, column=0)  # Adjusted position

    # Add a label to the right of each column checkbox
    label = tk.Label(grid_frame, text=f"{r + 1}")
    label.grid(row=r + 2, column=1)

# Create a 12x8 grid of entry widgets
for r in range(12):
    for c in range(8):
        entry = tk.Entry(grid_frame, width=5, justify='center')
        entry.grid(row=r + 2, column=c + 2)  # Adjusted position
        entries[(r, c)] = entry

"""CULTURE PLATE GRID END"""

"""USER PREFERENCE INPUT START"""
# Dictionary to store user preferences
preference = {
    'name': None,
    'plate': None,
    'insert': None,
    'reservoir': None,
    'tip': None,
    'equip': False,
    'eject': False,
    'grid': None
}

# Declare StringVar objects for dropdowns
plate_var = tk.StringVar(value="Choose a plate size")
insert_var = tk.StringVar(value="Choose an insert type")
reservoir_var = tk.StringVar(value="Choose a reservoir type")
tip_var = tk.StringVar(value="Choose a tip type")

# Procedure Name Entry Field
pname_label = tk.Label(controls_frame, text="Enter procedure name:")
pname_label.pack()
pname = tk.Entry(controls_frame, width=30)
pname.pack()

# Plate Size Dropdown
opt_plate = ["6 well plate", "96 well plate"]
p_plate = ["Choose a plate size"]
dropdown('plate', p_plate, opt_plate, "Plate Size:", plate_var, insert_opts)

# Insert type Dropdown
p_insert = ["Choose an insert type"]
dropdown_insert = dropdown('insert', p_insert, ["none"], "Insert Type:", insert_var)

# Reservoir size Dropdown
opt_res = ["1.5", "5", "25"]
p_res = ["Choose a reservoir type"]
dropdown('reservoir', p_res, opt_res, "Reservoir Type (in mL):", reservoir_var, selection_callback=greying)

# Tip Type Dropdown
opt_tip = [250]
p_tip = ["Choose a tip type"]
dropdown('tip', p_tip, opt_tip, "Tip Type (in uL):", tip_var)

# Auto-Equip checkbox
CheckVar1 = tk.IntVar()
equip = tk.Checkbutton(controls_frame, text="Auto-Equip Tips",
                       fg="black", variable=CheckVar1,
                       onvalue=1, offvalue=0, command=update_equip)
equip.pack()

# Auto-Eject checkbox
CheckVar2 = tk.IntVar()
eject = tk.Checkbutton(controls_frame, text="Auto-Eject Tips",
                       fg="black", variable=CheckVar2,
                       onvalue=1, offvalue=0, command=update_eject)
eject.pack()

"""USER PREFERENCE INPUT END"""

"""MACHINE LOADING INSTRUCTIONS START"""

# Tip Placement Label
equip_label = tk.Label(bottom_frame, text="Tip Placement", font=('Helvetica', 18, 'bold'))
equip_label.pack(pady=(10, 0))

# Frame for the Tip Positions
letters_frame = tk.Frame(bottom_frame)
letters_frame.pack()

# Reservoir Volumes Label
equip_label = tk.Label(bottom_frame, text="Reservoir Volumes", font=('Helvetica', 18, 'bold'))
equip_label.pack(pady=(10, 0))

# Frame for the Volume Positions
volume_frame = tk.Frame(bottom_frame)
volume_frame.pack()

volumes = tk.Label(volume_frame, text="Generate Procedure \nTo View Volumes", font=('Helvetica', 14, 'italic'),
                   fg="grey")
volumes.pack()

# Letter labels
letters = ['A', 'B', 'C', 'D']
letter_labels = {}
for letter in letters:
    letter_labels[letter] = tk.Label(letters_frame, text=letter, fg="grey")
    letter_labels[letter].pack(side='left', expand=True)

"""MACHINE LOADING INSTRUCTIONS END"""

# equip_label = tk.Label(bottom_frame, text="Minimum Reservoir Volumes")
# equip_label.pack(pady=(10, 0))

# # Add button to update tip selection
# tips_equip = tk.Button(bottom_frame, text="Press for tips", command=tip_set)
# tips_equip.pack()

""" SAVE, LOAD, GENERATE BUTTONS START """

# Run procedure button
run_procedure_button = tk.Button(root, text="Generate Procedure", command=lambda: run_procedure())
run_procedure_button.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()

# Create a bottom frame (like controls and grid frames)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Import CSV File button
import_button = tk.Button(bottom_frame, text="Import CSV File", command=import_csv_file)
import_button.pack(side=tk.LEFT, padx=10, pady=10)  # Pack to the left side of the bottom_frame

# Load Preferences button
load_button = tk.Button(bottom_frame, text="Load Preferences", command=open_preferences)
load_button.pack(side=tk.LEFT, padx=0, pady=10)  # Pack to the left side of the bottom_frame

# Calibration Button
cal_button = tk.Button(bottom_frame, text="Calibration Settings", command=calibration)
cal_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Save Preferences Button
save_button = tk.Button(bottom_frame, text="Save Preferences", command=save_preference)
save_button.pack(side=tk.RIGHT, padx=0, pady=0)

""" SAVE, LOAD, GENERATE BUTTONS END """

root.mainloop()

""" GUI END """
