# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project Operations file - All functions to transform an automaton
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata

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
 * @brief : Standardize an automaton
 * @param FA : The FA that we want to standardize
 * @return SFA: The standardized automaton
 '''


def standardization(FA: automata.FiniteAutomaton) -> automata.FiniteAutomaton:
    """
        When using this function, we assume that the automaton is not standard and is deterministic.
        It handles two cases :
            1. The automaton has more than one initial state
            2. There are transitions toward the initial sta

        In both cases, we just replace the initial state(s) by a new one and copy the transition of the
        former initial state(s)

    """
    if is_standard(FA):  # If the automaton is already standard, we return it as it is
        return FA
    else:
        nb_initial_states = len(FA.initial_states)  # gives the number of initial states
        FA.states.append('I')  # Add the new initial state to the existing states
        FA.initial_states.append('I')  # Add I as an initial state
        new_transitions = {}  # The dictionary of transitions containing I

        for (state, symbol), next_state in FA.transitions.items():
            # If we have the transition of an initial state we copy the transition with I
            if state in FA.initial_states:
                new_transitions[('I', symbol)] = next_state.copy()

        # Add the transitions of all states including the former initial ones
        for (state, symbol), next_state in FA.transitions.items():
            new_transitions[(state, symbol)] = next_state.copy()

        FA.transitions = new_transitions  # We replace with our new dictionary
        FA.initial_states = ['I']  # There is only one state and is I

        return FA


'''
 * @brief : Completes an automaton
 * @param FA : The FA that we want to complete
 * @return CDFA: The complete automaton
 '''


def completion(FA):
    """
    This function completes an automaton by adding a bin state and transitions to it for every missing transition
    :param FA: The automaton to complete
    :return: The completed automaton
    """
    # we go through all states to check if they have a transition for every letter of the alphabet
    for state in FA.states:  # we go through all the states
        for symbol in FA.alphabet:  # we go through all the symbols of the alphabet

            # we check if the combination is in the transitions (a.k.a there is a transition linked to the symbol)
            if (state, symbol) not in FA.transitions:

                # if we found a missing symbol transition, we check if a bin exists
                if "P" not in FA.states:
                    # if the bin doesn't exist we create it and create the transitions to itself to complete the bin
                    FA.states.append("P")

                # Once we made sure a bin exist, we add the missing transition towards the bin.
                FA.transitions[(state, symbol)] = {"P"}
    return FA


# this function isn't great because it only works on standardized FA


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
