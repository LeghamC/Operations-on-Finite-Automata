# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
from automata import FiniteAutomaton

'''
 * @brief : Says if an automaton is standard or not
 * @param FA : A FA 
 * @return bool : True if it is a standard automaton, False otherwise
 '''
def is_standard(filename : str) -> bool :
    fa = FiniteAutomaton()
    fa.read_automaton_from_file(filename)  # Read the automaton to retrieve the needed informations

    initial_states = fa.initial_states
    transitions = fa.transitions

    terminal_states = fa.terminal_states
    nb_initial_states = len(initial_states) #gives the number of initial states

    if nb_initial_states != 1:
        return False  #If there is more than one initial state, the automata is not standard so we return false

    first_state = initial_states[0]
    next_state = []

    for transi in transitions: # It gives us the next state of each transition. They are in the form AbC and we only need the C.
        third_char = transi[2]
        next_state.append(third_char)

    for state in next_state: # It verifies if there is a transition that goes towards the initial state. If it is the case, the automaton is not standard so we return false.
        if state == first_state :
            return False
    return True #If the automaton has only one state and there is no transition towards it, then it is standard and we return true.







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
    pass


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
    pass

