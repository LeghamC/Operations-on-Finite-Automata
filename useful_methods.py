# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project general functions file - Supplementary functions used for methods
# Created:     15/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata
import properties_check


'''
 * @brief : Merge 2 states into 1 when a state transitions to more than one state with the same label
 * @param FA : The fa and the 2 states that we want to merge into one
 '''
def merge(fa, state1, state2):
    # Creation of new merged state
    new_state = f"{state1}_{state2}"
    if new_state not in fa.states:
        fa.states.append(new_state)

    # We need to make terminal the new state if one of the merged state was originally terminal
    if state1 in fa.terminal_states or state2 in fa.terminal_states:
        fa.terminal_states.append(new_state)

    new_transitions = {}

    # Then we update the transitions
    for (state, label), targets in fa.transitions.items():
        updated_targets = {new_state if t in {state1, state2} else t for t in targets}

        new_transitions[(state, label)] = updated_targets

        # Update transitions that pointed to state1 or state2, replacing with new_state
        if state in {state1, state2}:
            new_transitions[(new_state, label)] = updated_targets

    # Then we remove the original states that we merged
    fa.states.remove(state1)
    fa.states.remove(state2)

    # Then finally we update the transitions
    fa.transitions = new_transitions




'''
 * @brief : If multiple initial states exist, we merge them into a single initial state
 * @param self : The fa
 '''
def merge_initial_states(fa):

    # We first make a copy of the original initial states
    original_initial_states = set(fa.initial_states)

    # Then we create of new unique initial state
    new_initial_state = "_".join(sorted(map(str, original_initial_states))) # map() is to apply the str function on each iterable
    fa.states.append(new_initial_state)
    # We replace the original initial states by our new unique one
    fa.initial_states = [new_initial_state]

    # We need to make terminal the new initial state if one of the merged state was originally terminal
    if any(state in fa.terminal_states for state in original_initial_states):
        fa.terminal_states.append(new_initial_state)

    # Then we merge the transitions too
    new_transitions = {}

    for (state, label), targets in fa.transitions.items():
        if state in original_initial_states:
            # We transfer the transitions from the initial states to our new unique initial state
            if (new_initial_state, label) not in new_transitions:
                new_transitions[(new_initial_state, label)] = set()
            new_transitions[(new_initial_state, label)].update(targets)
        else:
            new_transitions[(state, label)] = targets

    # Then we update the transitions so that they point to our new unique initial state
    for (state, label), targets in new_transitions.items():
        new_transitions[(state, label)] = {new_initial_state if t in original_initial_states else t for t in targets}

    # Then we remove the previously initial states
    for state in fa.states:
        if state in original_initial_states:
            fa.states.remove(state)


    # Finally we update the transitions
    fa.transitions = new_transitions

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



