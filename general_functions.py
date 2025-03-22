# ---------------------------------------------------------------------------------------------------------------
# Name:        general_functions.py
# Author:      ...
# Purpose:     Project automata file - General functions that help in the project
# Created:     09/03/2025
# ---------------------------------------------------------------------------------------------------------------

def total_table_length(alphabet_length: int, max_transition_length: int, longest_state: int) -> int:
    nb_character_state = alphabet_length * 5
    nb_character_state_cube_left_top_corner = longest_state * longest_state
    nb_character_transition = round_up(max_transition_length * 4)
    return nb_character_state + nb_character_state_cube_left_top_corner + nb_character_transition + 5


def retrieve_max_transition_length(dict: dict) -> int:
    max_transition_length = 5
    for key, value in dict.items():
        current_length = len(value)
        if current_length > max_transition_length:
            max_transition_length = current_length
    return max_transition_length


def retrieve_longest_state(states: list) -> int:
    longest_state = 0
    for state in states:
        if type(state) == str:
            if len(state) > longest_state:
                longest_state = len(state)
    if longest_state == 1:
        return 5
    return longest_state


def all_int(list: list) -> int:
    yes = 1
    for item in list:
        if type(item) != int:
            yes = 0
    return yes


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


def retrieve_initial_state_asynch(states: list, original_initial_states: list) -> list:
    """
    This function retrieve the initial state of a given set of states
    :param states: the set of states
    :param original_initial_states: the original initial states
    :return: the initial states
    """
    initial_states = []
    set_original_states = set(original_initial_states)
    for states in states:
        if int(states[0]) in set_original_states:
            initial_states.append(states)
    return initial_states


'''
 * @brief : Merge 2 states into 1 when a state transitions to more than one state with the same label
 * @param FA : The fa and the 2 states that we want to merge into one
 '''
def merge(fa, state1, state2):
    # Creation of new merged state
    new_state = f"{state1}_{state2}"
    if new_state not in fa.states:
        fa.states.append(new_state)

    # We need to make terminal the new state if one of the merged state was originally terminal
    if state1 in fa.terminal_states or state2 in fa.terminal_states:
        fa.terminal_states.append(new_state)

    new_transitions = {}

    # Then we update the transitions
    for (state, label), targets in fa.transitions.items():
        updated_targets = {new_state if t in {state1, state2} else t for t in targets}

        new_transitions[(state, label)] = updated_targets

        # Update transitions that pointed to state1 or state2, replacing with new_state
        if state in {state1, state2}:
            new_transitions[(new_state, label)] = updated_targets

    # Then we remove the original states that we merged
    fa.states.remove(state1)
    fa.states.remove(state2)

    # Then finally we update the transitions
    fa.transitions = new_transitions


'''
 * @brief : If multiple initial states exist, we merge them into a single initial state
 * @param self : The fa for which we will merge all its initial states
 '''
def merge_initial_states(fa):

    # We first make a copy of the original initial states
    original_initial_states = set(fa.initial_states)

    # Then we create of new unique initial state
    new_initial_state = "_".join(sorted(map(str, original_initial_states))) # map() is to apply the str function on each iterable
    fa.states.append(new_initial_state)
    # We replace the original initial states by our new unique one
    fa.initial_states = [new_initial_state]

    # We need to make terminal the new initial state if one of the merged state was originally terminal
    if any(state in fa.terminal_states for state in original_initial_states):
        fa.terminal_states.append(new_initial_state)

    # Then we merge the transitions too
    new_transitions = {}

    for (state, label), targets in fa.transitions.items():
        if state in original_initial_states:
            # We transfer the transitions from the initial states to our new unique initial state
            if (new_initial_state, label) not in new_transitions:
                new_transitions[(new_initial_state, label)] = set()
            new_transitions[(new_initial_state, label)].update(targets)
        else:
            new_transitions[(state, label)] = targets

    # Then we update the transitions so that they point to our new unique initial state
    for (state, label), targets in new_transitions.items():
        new_transitions[(state, label)] = {new_initial_state if t in original_initial_states else t for t in targets}

    # Then we remove the previously initial states
    for state in fa.states:
        if state in original_initial_states:
            fa.states.remove(state)


    # Finally we update the transitions
    fa.transitions = new_transitions



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

