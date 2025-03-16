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
def merge(self, state1, state2):
    # Creation of new merged state
    new_state = f"{state1}_{state2}"
    if new_state not in self.states:
        self.states.append(new_state)

    # We need to make terminal the new state if one of the merged state was originally terminal
    if state1 in self.terminal_states or state2 in self.terminal_states:
        self.terminal_states.append(new_state)

    new_transitions = {}

    # Then we update the transitions
    for (state, label), targets in self.transitions.items():
        updated_targets = {new_state if t in {state1, state2} else t for t in targets}

        new_transitions[(state, label)] = updated_targets

        # Update transitions that pointed to state1 or state2, replacing with new_state
        if state in {state1, state2}:
            new_transitions[(new_state, label)] = updated_targets

    # Then we remove the original states that we merged
    self.states.remove(state1)
    self.states.remove(state2)

    # Then finally we update the transitions
    self.transitions = new_transitions




'''
 * @brief : If multiple initial states exist, we merge them into a single initial state
 * @param FA : The fa
 '''
def merge_initial_states(self):

    # We first make a copy of the original initial states
    original_initial_states = set(self.initial_states)

    # Then we create of new unique initial state
    new_initial_state = "_".join(sorted(map(str, original_initial_states))) # map() is to apply the str function on each iterable
    self.states.append(new_initial_state)
    # We replace the original initial states by our new unique one
    self.initial_states = [new_initial_state]

    # We need to make terminal the new initial state if one of the merged state was originally terminal
    if any(state in self.terminal_states for state in original_initial_states):
        self.terminal_states.append(new_initial_state)

    # Then we merge the transitions too
    new_transitions = {}

    for (state, label), targets in self.transitions.items():
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
    for state in self.states:
        if state in original_initial_states:
            self.states.remove(state)


    # Then finally we update the transitions
    self.transitions = new_transitions

