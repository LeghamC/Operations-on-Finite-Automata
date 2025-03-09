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

    # we initialize the initial state of the CDFA as a set of the FA initial states
    initial_state = frozenset(FA.initial_states)  # Use frozenset to represent a set of states that is unchangeable
    cdfa.states.append(initial_state)
    cdfa.initial_states = [initial_state]

    # we make a list to track the unprocessed sets of states
    unprocessed_states = [initial_state]

    # and we process them
    while unprocessed_states:
        current_state = unprocessed_states.pop()

        # for each symbol in the alphabet, we find the next state
        for symbol in FA.alphabet:
            # we take the set from the FA of states reachable from the current set of states on symbol
            next_state = set()
            for state in current_state:
                if (state, symbol) in FA.transitions:
                    next_state.update(FA.transitions[(state, symbol)])

            next_state = frozenset(next_state)

            # if the next state is not already in the CDFA states, we add it
            if next_state and next_state not in cdfa.states:
                cdfa.states.append(next_state)
                unprocessed_states.append(next_state)

            # we add the transition for the current state to the next state
            if next_state:
                cdfa.transitions[(current_state, symbol)] = next_state

        # then we mark the terminal states in the CDFA
        if any(state in FA.terminal_states for state in current_state):
            cdfa.terminal_states.append(current_state)

        # finally, we check if our cdfa is complete
        if properties_check.is_complete(cdfa):
            return cdfa
        # else we complete it
        else:
            completion(cdfa)
            return cdfa





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
