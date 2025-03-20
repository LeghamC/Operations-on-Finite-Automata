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
 * @brief :Says if an automaton is standard or not
 * @param FA : The FA that we want to standardize
 * @return bool: True if it is standard. False otherwise.
 '''


def is_standard(FA: automata.FiniteAutomaton) -> bool:
    initial_states = FA.initial_states
    transitions = FA.transitions

    nb_initial_states = len(initial_states)  # gives the number of initial states

    if nb_initial_states != 1:
        return False  # If there is more than one initial state, the automata is not standard so we return false

    first_state = initial_states[0]

    for (state, symbol), next_state in transitions.items():  # We go through all the transitions
        if first_state in next_state:  # If there is a transition towards the initial state, the automaton is not
            # standard
            return False

    return True  # If the automaton has only one state and there is no transition towards it, then it is standard and
    # we return true.


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
    # We store the conditions determining if the fa is deterministic or not
    deterministic_conditions = properties_check.is_deterministic(FA)

    # if the automaton is already deterministic
    if all(condition == 1 for condition in deterministic_conditions):
        # we check if it is complete
        if properties_check.is_complete(FA):
            print("The automaton is already deterministic and complete.")
            return FA
        # else we complete it
        else:
            completion(FA)
            print("The automaton was already deterministic but not complete. Hence, we completed it.")
            return FA

    # else it is not deterministic, and we need to determinize it
    else:
        # We create a new FA instance that will become our CDFA to return
        CDFA = automata.FiniteAutomaton()
        CDFA.alphabet = FA.alphabet.copy()

        # We keep track of the new states we create
        temp_new_states_list = []
        # And we do a mapping of the state sets to the new CDFA states
        state_mapping = {}

        def state_name(state_set):
            """Local function to create a more explicit state name (state1_state2)."""
            # map() is to apply the str function on each iterable
            return "_".join(map(str, sorted(state_set))) if state_set else "empty"

        # Then we initialize our CDFA with the FA's initial state(s)
        initial_cdfa_state = frozenset(FA.initial_states)  # We use a frozenset as it is an immutable set
        initial_cdfa_state_name = state_name(initial_cdfa_state)
        temp_new_states_list.append(initial_cdfa_state)
        state_mapping[initial_cdfa_state] = initial_cdfa_state_name
        CDFA.states.append(initial_cdfa_state_name)
        CDFA.initial_states.append(initial_cdfa_state_name)

        # We also check if the initial state is terminal
        # We use & operator to do a bitwise AND (if basic AND then all states will end up terminal)
        if initial_cdfa_state & set(FA.terminal_states):
            CDFA.terminal_states.append(initial_cdfa_state_name)

        # We then start creating the CDFA by exploring the transitions of the new states we create
        while temp_new_states_list:
            current_cdfa_state = temp_new_states_list.pop(0)
            current_cdfa_state_name = state_mapping[current_cdfa_state]

            for label in CDFA.alphabet:
                next_state_set = set()

                for fa_state in current_cdfa_state:
                    if (fa_state, label) in FA.transitions:
                        next_state_set.update(FA.transitions[(fa_state, label)])

                # We now create a new state for the CDFA if it does not exist yet
                next_state_frozen = frozenset(next_state_set)
                next_state_name = state_name(next_state_frozen)

                if next_state_frozen not in state_mapping:
                    state_mapping[next_state_frozen] = next_state_name
                    temp_new_states_list.append(next_state_frozen)
                    CDFA.states.append(next_state_name)

                    # We now check if the new state is terminal
                    # We use & operator to do a bitwise AND (if basic AND then all states will end up terminal)
                    if next_state_frozen & set(FA.terminal_states):
                        CDFA.terminal_states.append(next_state_name)

                # Finally, we add the transition to the CDFA
                CDFA.transitions[(state_mapping[current_cdfa_state], label)] = {state_mapping[next_state_frozen]}

        # We now check if our new CDFA is complete
        if properties_check.is_complete(CDFA):
            print("The automaton has been determininized and was already complete after determinization.")
            return CDFA
        # else we complete it
        else:
            completion(CDFA)
            print("The automaton has been determininized and as it was not complete, we completed it.")
            return CDFA


'''
 * @brief : Minimizes an automaton
 * @param CDFA : The CDFA that we want to minimize
 * @return MCDFA: The minimized CDFA
 '''

def minimization2(CDFA):

    MCDFA = automata.FiniteAutomaton()
    MCDFA.alphabet = CDFA.alphabet

    current_partitioning = [] # list of lists of states representing the groups
    current_partitioning.append(CDFA.terminal_states)
    current_partitioning.append([state for state in CDFA.states if state not in CDFA.terminal_states]) # Non-terminal states

    minimized = 0
    while not minimized:
        patterns = []
        # patterns will contain the pattern for each state. The indexes are equal to the names of the state, the pattern of the state named '0' is at the index 0.
        # At the end, we make new groups, joining the states having the same patterns

        for i in range(len(CDFA.states)):

            this_pattern = []   # the pattern of the current state
            for char in CDFA.alphabet :
                for j in range(len(current_partitioning)):
                    if next(iter(CDFA.transitions[(CDFA.states[i], char)])) in current_partitioning[j] :
                        this_pattern.append(j)

            this_pattern.append(CDFA.states[i] in CDFA.terminal_states) # 0 or 1 for terminal or not

            patterns.append(tuple(this_pattern))

        next_partitioning = []
        for pattern in patterns:
            new_group = [i for i, p in enumerate(patterns) if p == pattern]
            if new_group not in next_partitioning :
                next_partitioning.append(new_group)

        if len(current_partitioning) == len(next_partitioning): # If the number of groups is still the same, it means no group have been created, so we're done
            minimized = 1
        else :
            current_partitioning = next_partitioning
    # end of while

    # We now have found the minimal automaton, we have to build it

    MCDFA.states = [i for i in range(len(current_partitioning))]

    MCDFA.initial_states = [i for i in MCDFA.states if CDFA.initial_states[0] in current_partitioning[i]]


    MCDFA.terminal_states = []

    for i in MCDFA.states :
        for t in CDFA.terminal_states :
            if i not in MCDFA.terminal_states :
                if t in current_partitioning[i] :
                    MCDFA.terminal_states.append(i)


    # Transitions part
    MCDFA.transitions = {}

    for key, value in CDFA.transitions.items():

        # dermining the corresponding state
        for i in MCDFA.states :
            if key[0] in current_partitioning[i]:
                starting_state = i
            if next(iter(value)) in current_partitioning[i] :   # value is a set of 1 element, because CDFA is deterministic
                arriving_state = i

        if (starting_state, key[1]) not in MCDFA.transitions :
            MCDFA.transitions[(starting_state, key[1])] = {arriving_state}

    return MCDFA


'''
 * @brief : Constructs an automaton recognizing the complementary language
 * @param A : previously obtained CDFA or MCDFA
 * @return complementary_A: The automaton recognizing the complementary language
 '''


def complementary_automaton(A: automata.FiniteAutomaton):
    """
    This function returns the complementary automaton of the automaton A
    :param A:
    :return:
    """
    B = automata.FiniteAutomaton()
    B.terminal_states = []
    B.initial_states = A.initial_states
    B.states = A.states
    B.alphabet = A.alphabet
    B.transitions = A.transitions

    for i in B.states:
        if i not in A.terminal_states:
            B.terminal_states.append(i)
    return B
