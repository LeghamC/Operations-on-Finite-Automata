# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
from inspect import stack

import automata
import general_functions

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

    for (state, symbol), next_state in transitions.items():  # We go through all the transitions
        if first_state in next_state:  # If there is a transition towards the initial state, the automaton is not
            # standard
            return False

    return True  # If the automaton has only one state and there is no transition towards it, then it is standard and
    # we return true.


'''
 * @brief : Standardize an automaton
 * @param FA : The FA that we want to standardize
 * @return SFA: The standardized automaton
 '''


def standardization(FA: automata.FiniteAutomaton) -> automata.FiniteAutomaton:
    """
        When using this function, we assume that the automaton is not standard and is deterministic.
        It handles two cases :
            1. The automaton has more than one initial state
            2. There are transitions toward the initial sta

        In both cases, we just replace the initial state(s) by a new one and copy the transition of the
        former initial state(s)

    """
    if is_standard(FA):  # If the automaton is already standard, we return it as it is
        return FA
    else:
        nb_initial_states = len(FA.initial_states)  # gives the number of initial states
        FA.states.append('I')  # Add the new initial state to the existing states
        FA.initial_states.append('I')  # Add I as an initial state
        new_transitions = {}  # The dictionary of transitions containing I

        for (state, symbol), next_state in FA.transitions.items():
            # If we have the transition of an initial state we copy the transition with I
            if state in FA.initial_states:
                new_transitions[('I', symbol)] = next_state.copy()

        # Add the transitions of all states including the former initial ones
        for (state, symbol), next_state in FA.transitions.items():
            new_transitions[(state, symbol)] = next_state.copy()

        FA.transitions = new_transitions  # We replace with our new dictionary
        FA.initial_states = ['I']  # There is only one state and is I

        return FA


'''
 * @brief : Completes an automaton
 * @param FA : The FA that we want to complete
 * @return CDFA: The complete automaton
 '''


def completion(FA):
    """
    This function completes an automaton by adding a bin state and transitions to it for every missing transition
    :param FA: The automaton to complete
    :return: The completed automaton
    """
    # we go through all states to check if they have a transition for every letter of the alphabet
    for state in FA.states:  # we go through all the states
        for symbol in FA.alphabet:  # we go through all the symbols of the alphabet

            # we check if the combination is in the transitions (a.k.a there is a transition linked to the symbol)
            if (state, symbol) not in FA.transitions:

                # if we found a missing symbol transition, we check if a bin exists
                if "P" not in FA.states:
                    # if the bin doesn't exist we create it and create the transitions to itself to complete the bin
                    FA.states.append("P")

                # Once we made sure a bin exist, we add the missing transition towards the bin.
                FA.transitions[(state, symbol)] = {"P"}
    return FA


# this function isn't great because it only works on standardized FA


'''
 * @brief : Determinizes and completes an automaton
 * @param FA : The FA that we want to determinize then complete
 * @return CDFA : The determinized and complete automaton
 '''


def determinization_and_completion_of_automaton(FA):
    pass


'''
 * @brief : Minimizes an automaton
 * @param CDFA : The CDFA that we want to minimize
 * @return MCDFA: The minimized CDFA
 '''


def minimization(CDFA):
    pass


'''
 * @brief : Constructs an automaton recognizing the complementary language
 * @param A : previously obtained CDFA or MCDFA
 * @return complementary_A: The automaton recognizing the complementary language
 '''


def complementary_automaton(A: automata.FiniteAutomaton):
    """
    This function returns the complementary automaton of the automaton A
    :param A:
    :return:
    """
    B = automata.FiniteAutomaton()
    B.terminal_states = []
    B.initial_states = A.initial_states
    B.states = A.states
    B.alphabet = A.alphabet
    B.transitions = A.transitions

    for i in B.states:
        if i not in A.terminal_states:
            B.terminal_states.append(i)
    return B


def epsilon_closure(FA: automata.FiniteAutomaton, state: int) -> str:
    """
    This function computes the epsilon closure of a state given in parameter in a finite automaton
    :param FA: The finite automaton in which we want to compute the epsilon closure
    :param state: The state for which we want to compute the epsilon closure
    :return: The epsilon closure of the given state as a string
    """
    closure = set()  # set of states reachable from the given state with only epsilon transitions
    stack_state = {state}  # stack of states to explore

    while stack_state:  # while there are states to explore
        current_state = stack_state.pop()  # we take the last state added to the stack
        if current_state not in closure:  # if the state is not already in the closure
            closure.add(current_state)  # we add it
            reachable_states = FA.transitions.get((current_state, "ε"), set())  # we get the states reachable with
            # epsilon
            stack_state.update(reachable_states)  # we add the states reachable with
            # epsilon from the current state
    str_states = ""
    for state in closure:
        str_states += str(state)
    return str_states


def determinization_asynchronous(FA: automata.FiniteAutomaton):
    """
    This function determined an asynchronous automaton. This function should be used after checking that the automaton
    given in parameter is asynchronous, so not deterministic. So we don't have to check again that this automaton
    is not deterministic.
    :param FA: a finite automaton that we already know is not deterministic as it is asynchronous
    :return: the determined asynchronous automaton
    """

    # ------------------------------------------------------------------------------------------------------------------
    # First compute all the epsilon closure of this asynchronous automaton
    # ------------------------------------------------------------------------------------------------------------------
    new_set_of_states = set()  # we create a set that will contain all the new states

    for state in FA.states:  # we compute the epsilon closure of each state
        closure_current_state = epsilon_closure(FA, state)
        new_set_of_states.add(closure_current_state)  # after computing a new epsilon closure we add it to the set of
        # states

    new_set_of_states = general_functions.order_set_of_string(new_set_of_states)  # convert the set of new states
    # into an ordered list. We could avoid doing this, but it's just to better understand the final determined automaton
    return new_set_of_states

    # ------------------------------------------------------------------------------------------------------------------
    # Change the initial states
    # ------------------------------------------------------------------------------------------------------------------
    # now that we retrieved all the new states, we can compute the initial states
    # if we have several initial states, we need to combine them


    """
    # ------------------------------------------------------------------------------------------------------------------
    # Second, we now need to retrieve the old transitions taking into account the epsilon closures
    # ------------------------------------------------------------------------------------------------------------------
    transitions_copy = {}  # make a copy of all the transitions using the copy function that can
    # be applied to dictionaries

    for states in new_set_of_states:  # iterate through all the new states we have get, state is a string
        transitions_with_closure = set()
        for chr_state in states:  # iterate through each character of the string state
            for symbol in FA.alphabet:  # iterate through all the symbols in the alphabet
                current_state = int(chr_state)  # convert the current state into a string
                # create a set that will contain all the transitions from the current state that
                # use the current symbol
                if (current_state, symbol) not in transitions_copy:
                    nex_states = FA.transitions.get((current_state, symbol), set())  # here next_states is of type set
        transitions_copy[states, symbol] = nex_states
    """

    return new_set_of_states
