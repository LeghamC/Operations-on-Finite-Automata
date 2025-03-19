# ---------------------------------------------------------------------------------------------------------------
# Name:        general_functions.py
# Author:      ...
# Purpose:     Project automata file - General functions that help in the project
# Created:     09/03/2025
# ---------------------------------------------------------------------------------------------------------------

def total_table_length(alphabet_length: int, max_transition_length: int) -> int:
    nb_character_state = alphabet_length * 5
    nb_character_state_cube_left_top_corner = 5
    nb_character_transition = round_up(max_transition_length * 4)
    return nb_character_state + nb_character_state_cube_left_top_corner + nb_character_transition


def retrieve_max_transition_length(dict: dict) -> int:
    max_transition_length = 0
    for key, value in dict.items():
        current_length = len(value)
        if current_length > max_transition_length:
            max_transition_length = current_length
    return max_transition_length


def round_up(number) -> int:
    if number == int(number):
        return number
    else:
        return int(number) + 1


def display_menu():
    title = "Finite Automata emulator"
    description = "Description : Oe tkt"
    menu_options = [
        "1. Load Automaton",
        "2. Display Automaton",
    ]

    border = "═" * 40
    print(f"╔{border}╗")
    print(f"║{title:^40}║")
    print(f"╠{border}╣")
    print(f"║{description:^40}║")
    print(f"╠{border}╣")
    for option in menu_options:
        print(f"║ {option:^39}║")
    print(f"╚{border}╝")

