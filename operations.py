# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import properties_check
import useful_methods


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
"""def determinization_and_completion_automaton(FA):
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

    # First condition : Only one initial state
    if deterministic_conditions[0] != 1:
        useful_methods.merge_initial_states(FA)"""


def determinization(fa):

    # We create a new FA instance that will become our CDFA to return
    cdfa = automata.FiniteAutomaton()
    cdfa.alphabet = fa.alphabet.copy()

    # We keep track of the new states we create
    temp_new_states_list = []
    # And we do a mapping of the state sets to the new CDFA states
    state_mapping = {}

    def state_name(state_set):
        """Local function to create a more explicit state name."""
        # map() is to apply the str function on each iterable
        return "_".join(map(str, sorted(state_set))) if state_set else "empty"

    # Then we initialize our CDFA with the FA's initial state(s)
    initial_cdfa_state = frozenset(fa.initial_states)  # We use a frozenset as it is an immutable set
    initial_cdfa_state_name = state_name(initial_cdfa_state)
    temp_new_states_list.append(initial_cdfa_state)
    state_mapping[initial_cdfa_state] = initial_cdfa_state_name
    cdfa.states.append(initial_cdfa_state_name)
    cdfa.initial_states.append(initial_cdfa_state_name)

    # We also check if the initial state is terminal
    # We use & operator to do a bitwise AND (if basic AND then all states will end up terminal)
    if initial_cdfa_state & set(fa.terminal_states):
        cdfa.terminal_states.append(initial_cdfa_state_name)


    # We then start creating the CDFA by exploring the transitions of the new states we create
    while temp_new_states_list:
        current_cdfa_state = temp_new_states_list.pop(0)
        current_cdfa_state_name = state_mapping[current_cdfa_state]

        for label in cdfa.alphabet:
            next_state_set = set()

            for fa_state in current_cdfa_state:
                if (fa_state, label) in fa.transitions:
                    next_state_set.update(fa.transitions[(fa_state, label)])

            # We now create a new state for the CDFA if it does not exist yet
            next_state_frozen = frozenset(next_state_set)
            next_state_name = state_name(next_state_frozen)

            if next_state_frozen not in state_mapping:
                state_mapping[next_state_frozen] = next_state_name
                temp_new_states_list.append(next_state_frozen)
                cdfa.states.append(next_state_name)

                # We now check if the new state is terminal
                # We use & operator to do a bitwise AND (if basic AND then all states will end up terminal)
                if next_state_frozen & set(fa.terminal_states):
                    cdfa.terminal_states.append(next_state_name)


            # Finally, we add the transition to the CDFA
            cdfa.transitions[(state_mapping[current_cdfa_state], label)] = {state_mapping[next_state_frozen]}

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
