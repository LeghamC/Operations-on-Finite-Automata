# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Check file - All functions to check the properties of an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES


'''
 * @brief : Check if an FA is valid or not
 * @param FA : The FA that we want to check if is valid or not
 * @return : a boolean  with 1: the automaton is valid, 0 else
'''
def is_an_automaton(FA):
    pass


'''
 * @brief : Checks if an FA is standard or not
 * @param FA : The FA that we want to check if is standard or not
 * @return : a boolean  with 1: the automaton is not standard, 0 else
 '''
def is_not_standard(FA):
    pass


'''
 * @brief : Checks if an FA is deterministic or not
 * @param FA : The FA that we want to check if is deterministic or not
 * @return : a boolean  with 1: the automaton is deterministic, 0 else
 '''
def is_deterministic(FA):
    pass


'''
 * @brief : Checks if an FA is complete or not
 * @param FA : The FA that we want to check if is complete or not
 * @return : a boolean  with 1: the automaton is complete, 0 else
 '''
def is_complete(FA):
    for state in FA.states:
        for letter in FA.alphabet:
            if [(state,letter)] not in FA.transitions :
                return False
    return True
