# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import properties_check
import operations
import useful_methods


if __name__ == '__main__':

    # Test to know if deterministic
    fa = automata.FiniteAutomaton()
    fa.read_automaton_from_file("Automatons/project_automaton_test.txt")  # this automaton is not deterministic
    fa.display_automaton()
    print(fa.transitions)

    properties_check.is_deterministic(fa)
    useful_methods.merge_initial_states(fa)
    useful_methods.merge(fa,1, 3)


    print(fa.alphabet)
    print(fa.states)
    print("The initial states are : ", fa.initial_states)
    print(fa.terminal_states)
    print(fa.transitions)
    fa.display_automaton()
