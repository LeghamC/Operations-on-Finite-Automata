# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES


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
                if "bin" not in FA.states :

                #if the bin doesn't exist we create it and create the transitions to itself to complete the bin
                    FA.state.append("bin")
                    for s in FA.alphabet :
                        FA.transitions[("bin", s)] = "bin"

                # once we made sure a bin exist, we add the missing transition towards the bin.
                FA.transitions[(state,symbol)] = "bin"
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
    pass
