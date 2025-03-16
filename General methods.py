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
 * @param FA : The 2 states that we want to merge into one
 '''
def merge(self, state1, state2):
    new_transitions = {}

    for (state,label), targets in self.transitions.items():
        if len(targets) > 1:
            # We create a new merged state
            new_state = "_".join(map(str, sorted(targets))) # map() is to execute the function str for each item in the iterable

            # We check that the new state does not already exist and if not we add it to the list of states
            if new_state not in self.states:
                self.states.append(new_state)

                # We now have to make a union of the transition and transfer them to the new state
                # N.B : we are still in the first loop so we cannot use the same names : s = state & symbol = label & ns = next state
                for next_state in targets:
                    for (s,symbol), ns in self.transitions.items():
                        if s == next_state:
                            if (new_state, symbol) not in new_transitions:
                                pass




