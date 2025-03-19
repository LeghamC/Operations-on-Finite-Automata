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
test.read_automaton_from_file(f"Automatons/automaton_{31}.txt")
test.display_automaton()
#print(operations.epsilon_closure(test, 0))
oe = operations.determinization_asynchronous(test)
print(oe)
oetkt = general_functions.retrieve_initial_state_asynch(oe, [0, 1])
print(oetkt)