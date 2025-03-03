# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
from automata import FiniteAutomaton


'''
 * @brief : Standardize an automaton
 * @param FA : The FA that we want to standardize
 * @return SFA: The standardized automaton
 '''
def standardization(FA):
       pass

def is_standard(filename :str) :

    fa = FiniteAutomaton()
    fa.read_automaton_from_file(filename)
    standard = True           # we begin by saying that the automata is standard

    with open(filename, "r") as file:
        lines = file.readlines()  # read the entire file and store it in a list of strings
        first_lines = lines[:4]  # retrieve the first 4 lines as they contain
        # the general information of the automaton | use readlines() as the first 4 lines are always the same

    next_state=[]

    initial_states_line = first_lines[2].split()  # split the line into a list of strings
    nb_initial_states = initial_states_line[0].strip()  # retrieve the number of initial states
    initial_states = initial_states_line[1:]

    transitions = fa.transitions

    for states in transitions :
        third_char = states[2:]
        next_state.append(third_char)


    if int(nb_initial_states) > 1 :
        standard = False  #If there is more than one initial state, the automata is not standard

    for i in next_state :
        for j in initial_states:
            if i == j :
                standard = False

    return standard



filename = "Automatons/project_automaton_test.txt"
standard = is_standard(filename)
print(standard)











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

