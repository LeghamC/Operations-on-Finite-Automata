# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
from inspect import stack

import automata

'''
 * @brief : Standardize an automaton
 * @param FA : The FA that we want to standardize
 * @return SFA: The standardized automaton
 '''


def standardization(FA):
    pass


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


def complementary_automaton(A):
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


def epsilon_closure(FA, state):
    closure = set()
    stack = {state}

    while stack:
        current_state = stack.pop()
        if current_state not in closure:
            closure.add(current_state)
            stack.update(FA.transitions.get((current_state, "ε"), set()))
    pass
