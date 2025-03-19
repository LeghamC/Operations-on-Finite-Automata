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

user_automaton = input("Enter the number corresponding to the automaton you want to manipulate: ")



test = automata.FiniteAutomaton()
test.read_automaton_from_file(f"Automatons/automaton_{user_automaton}.txt")
test.display_automaton()

minimal_auto = operations.minimization2(test)

minimal_auto.display_automaton()