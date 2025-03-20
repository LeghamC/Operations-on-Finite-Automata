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
    cdfa = operations.determinization(fa)


    print(cdfa.alphabet)
    print(cdfa.states)
    print("The initial states are : ", cdfa.initial_states)
    print(cdfa.terminal_states)
    print(cdfa.transitions)
    cdfa.display_automaton()
