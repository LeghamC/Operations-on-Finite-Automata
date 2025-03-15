# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import operations
import properties_check





test = automata.FiniteAutomaton()
test.read_automaton_from_file("Automatons/project_automaton_test.txt")
test.display_automaton()

test2 = automata.FiniteAutomaton()
test2.read_automaton_from_file("Automatons/project_automaton_test_2")
test2.display_automaton()

