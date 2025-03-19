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


def order_set_of_string(set_of_string: set) -> list:
    """
    This function sort a set of strings into a list
    :param set_of_string:
    :return: the ordered set of strings as a list
    """
    list_of_string = list(set_of_string)  # convert the current set into an array
    list_of_string.sort()  # as we now have an array, we use the function sort on that
    return list_of_string


def retrieve_initial_state_asynch(states: list, original_initial_states : list) -> list:
    """
    This function retrieve the initial state of a given set of states
    :param states: the set of states
    :param original_initial_states: the original initial states
    :return: the initial states
    """
    initial_states = []
    set_initial_states = set(original_initial_states)
    print(set_initial_states)
    for states in states:
        if int(states[0]) in set_initial_states:
            initial_states.append(states)
    return initial_states


