def get_procedure_name():
    """
    Prompts user for procedure name

    :return: (String) procedure name
    """
    name = input("Please type in your procedure name: ")
    return name


def get_reservoir_type():
    """
    Prompts user for reservoir type

    :return: (Float) size of reservoir in uL
    """
    tube = input("Which reservoir are you using? (Type A for 5mL tube, "
                 "B for 1.5mL PCR tube): ")
    if tube == "A":
        return 5000.000
    else:
        return 1500.000


def get_tip_type():
    """
    Prompts user for nozzle tip type

    :return: (Int) size of tip in uL
    """
    tip = int(input("Which size nozzle tip are you using? (Type size in uL): "))
    return tip


def get_plate_type():
    """
    Prompts user for culture plate type

    :return: (Int) size of culture plate
    """
    plate = int(input("What size culture plate are you using? (Type # of wells): "))
    return plate


def get_insert_type():
    """
    Prompts user for culture plate insert type

    :return: (String) name of culture plate insert
    """
    insert = input("Which insert are you using? (Type A for EZ-Seed, B for 3-in-1): ")
    if insert == "A":
        return "EZ-Seed"
    else:
        return "3-in-1"
