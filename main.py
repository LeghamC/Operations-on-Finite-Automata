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

test2 = automata.FiniteAutomaton()
test2.read_automaton_from_file("Automatons/project_automaton_test_2")
test2.display_automaton()

print(test2.terminal_states)
print(test2.transitions)
print(test2.initial_states)
#print(recognize_word_recursive("abaabababababababababbbaabbabababbbbbbaaaaabbbbabababababababaabbaa", test ))

