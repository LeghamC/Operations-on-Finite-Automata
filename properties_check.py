# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Check file - All functions to check the properties of an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata



'''
 * @brief :Says if an automaton is standard or not
 * @param FA : The FA that we want to standardize
 * @return bool: True if it is standard. False otherwise.
 '''

def is_standard(FA: automata.FiniteAutomaton) -> bool:
    initial_states = FA.initial_states
    transitions = FA.transitions

    nb_initial_states = len(initial_states)  # gives the number of initial states

    if nb_initial_states != 1:
        return False  # If there is more than one initial state, the automata is not standard so we return false

    first_state = initial_states[0]

    for next_state in transitions.values():  # We go through all the transitions
        if first_state in next_state:  # If there is a transition towards the initial state, the automaton is not
            # standard
            return False

    return True  # If the automaton has only one state and there is no transition towards it, then it is standard and
    # we return true.


'''
 * @brief : Checks if an FA is deterministic or not
 * @param FA : The FA that we want to check if is deterministic or not
 * @return : a boolean  with 1: the automaton is deterministic, 0 else
 '''


def is_deterministic(FA):
    """We have to check 3 conditions to know if an automaton is deterministic :
            1. Only one initial state
            2. No two transitions of same label from same state
            3. No epsilon (ε) transition"""

    initial = 1
    transitions = 1
    epsilon = 1

    # check of first condition
    if len(FA.initial_states) != 1:
        initial = 0
        print("The automaton is not deterministic as we have do not have a unique initial state.")

    # check of second condition
    for (state, label), target_state in FA.transitions.items():
        if len(target_state) > 1:
            transitions = 0
            print(
                f"The automaton is not deterministic as state '{state}' has multiple transitions for label '{label}'.")

    # check of third condition
    if any(label == 'ε' for (_, label) in FA.transitions.keys()):
        epsilon = 0
        print("The automaton is not deterministic as it contains an epsilon (ε) transition.")

    # else the automaton is deterministic
    if initial == 1 and transitions == 1 and epsilon == 1:
        print("The automaton is deterministic.")

    return [initial, transitions, epsilon]


'''
 * @brief : Checks if an FA is complete or not
 * @param FA : The FA that we want to check if is complete or not
 * @return : a boolean  with 1: the automaton is complete, 0 else
 '''


def is_complete(FA):
    complete = 1
    for state in FA.states:
        for symbol in FA.alphabet:
            if (state, symbol) not in FA.transitions:
                complete = 0
                print(f"The automaton is not complete as state '{state}' has no transitions for label '{symbol}'.")

    # else the automaton is complete
    if complete == 1:
        print("The automaton is complete")

    return complete



def is_asynchronous(FA):
        """
        This function checks if the automaton contains epsilon transitions, if so it is an asynchronous automaton
        :return: True if the automaton contains epsilon transitions, False otherwise
        """
        for transition in FA.transitions:
            if transition[1] == "ε":
                return True
        return False