# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import properties_check
import operations


if __name__ == '__main__':

    # Tests on automata

    # Review display automata : 16, 25, 29

    user_automaton = input("Enter the number corresponding to the automaton you want to manipulate: ")
    test = automata.FiniteAutomaton()
    test.read_automaton_from_file(f"Automatons/automaton_{user_automaton}.txt")
    test.display_automaton()
    test2 = operations.determinization_asynchronous(test)
    
    test2.display_automaton()

    test3 = operations.completion(test2)
    test3.display_automaton()

    test4 = operations.minimization(test3)
    test4.display_automaton()

