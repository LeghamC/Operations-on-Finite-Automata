# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
from IPython.core.display_functions import display

import automata
import operations
import properties_check
from word_recognition import recognize_word

"""
user_automaton = input("Enter the number corresponding to the automaton you want to manipulate: ")
test = automata.FiniteAutomaton()
test.read_automaton_from_file(f"Automatons/automaton_{user_automaton}.txt")
test.display_automaton()
"""

test2 = automata.FiniteAutomaton()
test2.read_automaton_from_file("Automatons/automaton_31.txt")


print(test2.terminal_states)
print(test2.transitions)
print(test2.initial_states)
test2.display_automaton()
print(recognize_word("abaabb", test2))



#print(recognize_word_recursive("abaabababababababababbbaabbabababbbbbbaaaaabbbbabababababababaabbaa", test ))

