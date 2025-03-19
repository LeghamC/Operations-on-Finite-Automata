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

operations.is_standard(test)
if operations.is_standard(test) == False :
    operations.standardization(test)
test.display_automaton()


test2 = automata.FiniteAutomaton()
test2.read_automaton_from_file("Automatons/project_automaton_test_2")
test2.display_automaton()

operations.is_standard(test2)
if operations.is_standard(test2) == False :
    operations.standardization(test2)
test2.display_automaton()

test_automaton = automata.FiniteAutomaton()  # create an automaton
test_automaton.read_automaton_from_file("Automatons/project_automaton_test.txt")  # read the automaton from a file
test_automaton.display_automaton()
for transition in test_automaton.transitions:
    print(transition)