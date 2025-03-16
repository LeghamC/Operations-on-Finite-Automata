# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import properties_check


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
    if not properties_check.is_complete(FA):
        # if the bin doesn't exist we create it and create the transitions to itself to complete the bin
        if "P" not in FA.states:
            FA.states.append("P")
            for s in FA.alphabet:
                FA.transitions[("P", s)] = {"P"}

        # Now we add the transition to the think state for all states missing it
        for state in FA.states:
            for symbol in FA.alphabet:
                if (state, symbol) not in FA.transitions:
                    FA.transitions[(state, symbol)] = {"P"}
    return FA





'''
 * @brief : Determinizes and completes an automaton
 * @param FA : The FA that we want to determinize then complete
 * @return CDFA : The determinized and complete automaton
 '''
def determinization_and_completion_automaton(FA):
    # to store the conditions respected or not for the fa to be deterministic
    deterministic_conditions = properties_check.is_deterministic(FA)

    # if the automaton is already deterministic
    if all(condition == 1 for condition in deterministic_conditions):
        # we check if it is complete
        if properties_check.is_complete(FA):
            return FA
        # else we complete it
        else:
            completion(FA)
            return FA

    # else it is not deterministic, and we need to determinize it
    cdfa = automata.FiniteAutomaton()







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
