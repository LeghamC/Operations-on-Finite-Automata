# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata as a


'''
 * @brief :Says if an automaton is standard or not
 * @param FA : The FA that we want to standardize
 * @return bool: True if it is standard. False otherwise.
 '''



def is_standard(FA : a.FiniteAutomaton) -> bool:
    initial_states = FA.initial_states
    transitions = FA.transitions

    nb_initial_states = len(initial_states)  # gives the number of initial states

    if nb_initial_states != 1:
        return False  # If there is more than one initial state, the automata is not standard so we return false

    first_state = initial_states[0]

    for (state, symbol), next_state in transitions.items():
        if first_state in next_state:
            return False


    return True  # If the automaton has only one state and there is no transition towards it, then it is standard and we return true.




'''
 * @brief : Standardize an automaton
 * @param FA : The FA that we want to standardize
 * @return SFA: The standardized automaton
 '''
def standardization(FA : a.FiniteAutomaton)->a.FiniteAutomaton:
    '''
        When using this function, we assume that the automaton is not standard and is deterministic.
        It handles two cases :
            1. The automaton has more than one initial state
            2. There are transitions toward the initial sta

        In both cases, we just replace the initial state(s) by a new one and copy the transition of the
        former initial state(s)

    '''
    nb_initial_states = len(FA.initial_states)  # gives the number of initial states
    FA.states.append('I') # Add the new initial state to the existing states
    FA.initial_states.append('I') # Add I as an initial state
    new_transitions = {} # The dictionary of transitions containing I


    for (state, symbol), next_state in FA.transitions.items() :
        # If we have the transition of an initial state we copy the transition with I
        if state in FA.initial_states:
            new_transitions[('I', symbol)] = next_state.copy()

    # Add the transitions of all states including the former initial ones
    for(state, symbol), next_state in FA.transitions.items():
        new_transitions[(state, symbol)] = next_state.copy()

    FA.transitions = new_transitions # We replace with our new dictionary
    FA.initial_states = ['I'] # There is only one state and is I

    return FA




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

    B = a.FiniteAutomaton()
    B.terminal_states = []
    B.initial_states = A.initial_states
    B.states = A.states
    B.alphabet = A.alphabet
    B.transitions = A.transitions

    for i in B.states :
        if i not in A.terminal_states :
            B.terminal_states.append(i)
    return B

