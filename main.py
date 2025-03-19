# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import general_functions
import operations
import properties_check


# user_automaton = input("Enter the number corresponding to the automaton you want to manipulate: ")
test = automata.FiniteAutomaton()
test.read_automaton_from_file(f"Automatons/automaton_{20}.txt")
#test.read_automaton_from_file(f"Automatons/automaton_{31}.txt")
test.display_automaton()

general_functions.merge_initial_states(test)
test.display_automaton()
