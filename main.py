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


user_automaton = int(input("Enter the number corresponding to the automaton you want to manipulate: "))

if user_automaton == 1:
    test = automata.FiniteAutomaton()
    test.read_automaton_from_file("Automatons/project_automaton_test.txt")
    test.display_automaton()
elif user_automaton == 2:
    test2 = automata.FiniteAutomaton()
    test2.read_automaton_from_file("Automatons/project_automaton_test_2")
    test2.display_automaton()
elif user_automaton == 3:
    test3 = automata.FiniteAutomaton()
    test3.read_automaton_from_file("Automatons/automaton_20.txt")
    test3.display_automaton()
elif user_automaton == 4:  # ensure that the completion function works
    test4 = automata.FiniteAutomaton()
    test4.read_automaton_from_file("Automatons/automaton_23.txt")
    test4.display_automaton()
    completed_automaton = operations.completion(test4)
    completed_automaton.display_automaton()