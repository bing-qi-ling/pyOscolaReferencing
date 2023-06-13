import os
import pyperclip

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# All case functions

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_court_menu_choice():
    clear_console()
    print("Where was this reported?")
    print("1. United Kingdom Supreme Court (post-2007)\n2. House of Lords (pre-2007)\n3. Court of Appeal, Criminal Division\n4. Court of Appeal, Civil Division\n5. England and Wales High Court (Opens a new menu)\n6. Weekly Law Reports (WLR)\n7. All England Law Reports\nIf the case is not reported in any of the prior listings, please see below.\n8. Custom report citation")

    return get_integer_input("Enter the number corresponding to the correct response: ")

def get_high_court_choice():
    clear_console()
    print("Select the correct option from this list of High Courts:")
    print("1. England and Wales High Court (Chancery Division)")
    print("2. England and Wales High Court (Patents Court)")
    print("3. England and Wales High Court (Queen's Bench Division)")
    print("4. England and Wales High Court (King's Bench Division)") 
    print("5. England and Wales High Court (Administrative Court)")
    print("6. England and Wales High Court (Commercial Court)")
    print("7. England and Wales High Court (Admiralty Court)")
    print("8. England and Wales High Court (Technology & Construction Court)")
    print("9. England and Wales High Court (Family Division)")

    return get_integer_input("Enter your selection: ")

def get_custom_court():
    return input("Enter the location where it was reported: ").strip()

def court_menu(case_no):
    court_list_choice = get_court_menu_choice()
    if court_list_choice == 1:
        return "UKSC"
    elif court_list_choice == 2:
        return "UKHL"
    elif court_list_choice == 3:
        return "EWCA Crim"
    elif court_list_choice == 4:
        return "EWCA Civ"
    elif court_list_choice == 5:
        clear_console()
        court1 = "EWHC "
        high_court_choice = get_high_court_choice()
        high_court_specs = {
            1: " (Ch)",
            2: " (Pat)",
            3: " (QB)",
            4: " (KB)",
            5: " (Admin)",
            6: " (Comm)",
            7: " (Admlty)",
            8: " (TCC)",
            9: " (Fam)"
        }
        high_court_spec = high_court_specs.get(high_court_choice)
        if high_court_spec:
            high_court_case_no = court1 + case_no + high_court_spec
            return high_court_case_no
        else:
            print("Invalid High Court choice.")
    elif court_list_choice == 6:
        return "WLR"
    elif court_list_choice == 7:
        return "All ER"
    elif court_list_choice == 8:
        return get_custom_court()
    else:
        print("Invalid court choice.")

def get_case_choice():
    clear_console()
    print("Ensure your case isn't already OSCOLA referenced.\nOSCOLA referenced cases should look like this: R v Brown [1993] UKHL 19.")
    case_party1 = input("Who is the first named in the case? ").strip()
    case_party2 = input("Who is the second named in the case? ").strip()
    case_year = input("What year was the case reported? ").strip()
    case_no = input("Enter the case number: ").strip()

    return case_party1, case_party2, case_year, case_no

def format_case_citation(case_party1, case_party2, case_year, court, case_no=None):
    if court.startswith("EWHC"):
        if case_no is not None:
            citation = f"{case_party1} v {case_party2} [{case_year}] {court} {case_no}"
        else:
            citation = f"{case_party1} v {case_party2} [{case_year}] {court}"
    else:
        citation = f"{case_party1} v {case_party2} [{case_year}] {court} {case_no}"
    return citation

def CaseChoice():
    clear_console()
    case_party1, case_party2, case_year, case_no = get_case_choice()
    court = court_menu(case_no)
    if court:
        case_output = format_case_citation(case_party1, case_party2, case_year, court, case_no)
        pyperclip.copy(case_output)
        print("Your OSCOLA referenced case is:", case_output)
        print("It has been copied to the clipboard!")
    else:
        print("Invalid court selection.")

# End of the case functions


def main_menu(): # Main menu function
    clear_console()
    print("Welcome to the OSCOLA referencing generator!\nWhat are you trying to cite?")
    print("1. United Kingdom Cases (currently greater support for English cases)")
    print("13. Credits")
    menu_option = input("Enter your required service: ")
    if menu_option == "1":
        CaseChoice()
        input("Remember to add a full stop to the end of the citation if you're only citing this, or a semicolon if you're citing something else!\nPress ENTER to return to the main menu.")
        main_menu()
    elif menu_option == "13":
        input("Credits to be displayed here. Press ENTER to return to the main menu.")
        main_menu()
    else:
        input("Invalid option. Press ENTER to return to the main menu.")
        main_menu()

main_menu()