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
from word_recognition import recognize_word_recursive

""""
print(test.alphabet)
print(test.states)
print("The initial states are : ",test.initial_states)
print(test.terminal_states)
print(test.transitions)
test.display_automaton()
print(properties_check.is_complete(test))

print("completing FA : ")
operations.completion(test)
test.display_automaton()
print(properties_check.is_complete(test))

print("finding the complementary FA")
B = operations.complementary_automaton(test)
test.display_automaton()
B.display_automaton()
"""

test = automata.FiniteAutomaton()
test.read_automaton_from_file("Automatons/project_automaton_test.txt")
test.display_automaton()

test2 = automata.FiniteAutomaton()
test2.read_automaton_from_file("Automatons/project_automaton_test_2")
test2.display_automaton()

print(test2.terminal_states)
print(test2.transitions)
print(test2.initial_states)
print(recognize_word_recursive("abaabababababababababbbaabbabababbbbbbaaaaabbbbabababababababaabbaa", test ))

