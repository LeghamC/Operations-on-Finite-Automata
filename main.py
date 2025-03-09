# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import properties_check


if __name__ == '__main__':

    # Test to know if deterministic
    fa = automata.FiniteAutomaton()
    fa.read_automaton_from_file("Automatons/project_automaton_test.txt")  # this automaton is not deterministic
    properties_check.is_deterministic(fa)

    fa2 = automata.FiniteAutomaton()
    fa2.read_automaton_from_file("Automatons/project_automaton_test_deterministic")  # this automaton is deterministic
    properties_check.is_deterministic(fa2)