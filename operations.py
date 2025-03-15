# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
from automata import FiniteAutomaton

fa = FiniteAutomaton()
'''
 * @brief :Says if an automaton is standard or not
 * @param FA : The FA that we want to standardize
 * @return bool: True if it is standard. False otherwise.
 '''



def is_standard(filename: str) -> bool:
    
    fa.read_automaton_from_file(filename)  # Read the automaton to retrieve the needed informations

    initial_states = fa.initial_states
    transitions = fa.transitions

    terminal_states = fa.terminal_states
    nb_initial_states = len(initial_states)  # gives the number of initial states

    if nb_initial_states != 1:
        return False  # If there is more than one initial state, the automata is not standard so we return false

    first_state = initial_states[0]

    for (state, symbol), next_state in transitions.items():
        if first_state in next_state:
            return False


    return True  # If the automaton has only one state and there is no transition towards it, then it is standard and we return true.


filename = "Automatons/project_automaton_test.txt"
standard = is_standard(filename)
print(standard)



'''
 * @brief : Standardize an automaton
 * @param FA : The FA that we want to standardize
 * @return SFA: The standardized automaton
 '''
def standardization(FA):
    pass


'''
 * @brief : Completes an automaton
 * @param FA : The FA that we want to complete
 * @return CDFA: The complete automaton
 '''
def completion(FA):

#we go through all states to check if they have a transition for every letter of the alphabet
    for state in FA.states :
        for symbol in FA.alphabet :

            #we check if the combination is in the transitions (a.k.a there is a transition linked to the symbol)
            if (state, symbol) not in FA.transitions :

                #if we found a missing symbol transition, we check if a bin exists
                if "P" not in FA.states :

                #if the bin doesn't exist we create it and create the transitions to itself to complete the bin
                    FA.states.append("P")
                    for s in FA.alphabet :
                        FA.transitions[("P", s)] = "P"

                # once we made sure a bin exist, we add the missing transition towards the bin.
                FA.transitions[(state,symbol)] = "P"
    return FA
    pass


#this function isn't great because it only works on standardized FA



'''
 * @brief : Determinizes and completes an automaton
 * @param FA : The FA that we want to determinize then complete
 * @return CDFA : The determinized and complete automaton
 '''
def determinization_and_completion_of_automaton(FA):
    pass


'''
 * @brief : Minimizes an automaton
 * @param CDFA : The CDFA that we want to minimize
 * @return MCDFA: The minimized CDFA
 '''
def minimization(CDFA):
    pass


'''
 * @brief : Constructs an automaton recognizing the complementary language
 * @param A : previously obtained CDFA or MCDFA
 * @return complementary_A: The automaton recognizing the complementary language
 '''
def complementary_automaton(A):

    B = automata.FiniteAutomaton()
    B.terminal_states = []
    B.initial_states = A.initial_states
    B.states = A.states
    B.alphabet = A.alphabet
    B.transitions = A.transitions

    for i in B.states :
        if i not in A.terminal_states :
            B.terminal_states.append(i)
    return B

