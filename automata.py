# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project automata file - Lecture and display of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import sys

import general_functions
from general_functions import retrieve_max_transition_length


class FiniteAutomaton:
    """
    Class representing a finite automaton
    """

    def __init__(self):
        """
        Constructor of the class
        """
        self.alphabet = []  # The alphabet of the automaton
        self.states = []  # The states of the automaton
        self.initial_states = []  # The initial states of the automaton
        self.terminal_states = []  # The terminal states of the automaton
        self.transitions = {}  # The transitions of the automaton : each key is a tuple (state, symbol) and the value
        # is the next state which is stored in an array. The key represents the current state and the symbol that is
        # read to go to the next state. Key's value is stored as set containing the next states.
        self.epsilon_closure = {}  # we will use it when doing the determinization of the automaton containing epsilon

    # ---------------------------------------------------------------------------------------------------------------

    # Methods of the class

    def read_automaton_from_file(self, filename: str) -> None:
        """
        Reads the automaton from a .txt file and stores it
        :param filename: The .txt file with the automata's properties
        :return: None
        """
        with open(filename, "r", encoding='utf-8') as file:
            lines = file.readlines()  # read the entire file and store it in a list of strings
            first_lines = lines[:4]  # retrieve the first 4 lines as they contain
            # the general information of the automaton | use readlines() as the first 4 lines are always the same

            # store the alphabet
            nb_elem_alphabet = first_lines[0].strip()  # .strip() removes the '\n' character, we get as a result a
            # string that contains the number of symbols in the alphabet

            if int(nb_elem_alphabet) == 0:  # Special case for the empty automaton
                self.alphabet.append("a")
                self.states.append("0")
                self.initial_states.append("0")
                self.terminal_states.append("0")
            else:
                for i in range(int(nb_elem_alphabet)):  # we want to add the alphabet depending on the number of the
                    # symbols in the alphabet, every alphabet starts with a than b and so on | int() converts the string
                    self.alphabet.append(
                        chr(97 + i))  # take the ASCII code of 'a' which is 97 and add i to it to get the
                    # corresponding character

                # store the states
                nb_states = first_lines[1].strip()  # retrieve the number of states which is the second line
                for i in range(int(nb_states)):  # add the states depending on the number of states
                    self.states.append(i)  # add the states from 0 to the number of states

                # store the initial states
                initial_states_line = first_lines[2].split()  # split the line into a list of strings
                nb_initial_states = initial_states_line[0].strip()  # retrieve the number of initial states
                for i in range(
                        int(nb_initial_states)):  # add the initial states depending on the number of initial states
                    self.initial_states.append(int(initial_states_line[i + 1]))  # add the initial states from the list

                # store the terminal states
                # we do the same as for the initial states
                terminal_states_line = first_lines[3].split()
                nb_terminal_states = terminal_states_line[0].strip()
                for i in range(int(nb_terminal_states)):
                    self.terminal_states.append(int(terminal_states_line[i + 1]))

                #  the transitions
                transition_txt = lines[5:]  # retrieve the transitions from the file, skip the fifth line as it contains
                # only contain the number of transitions, but we can get it back by getting the length of the array with
                # len()
                for line in transition_txt:  # iterate through the transitions
                    current_transition = line.strip().split()  # remove the '\n' character and split the different
                    # strings into a list

                    # We should put here the verification for ε transitions

                    current_state = int(current_transition[0])  # retrieve the current state which is always the first
                    # element

                    symbol = current_transition[1]  # retrieve the symbol which is always the second element

                    next_states = {int(state) for state in current_transition[2:]}  # retrieve the next states and
                    # convert them into integers, the braces {} are used to create a set which ensure that the elements
                    # are unique

                    if (current_state, symbol) not in self.transitions:
                        self.transitions[(current_state, symbol)] = set()  # if the key is not in the dictionary,
                        # we add it
                    self.transitions[(current_state, symbol)].update(next_states)  # add the next states to the
                    # current key

    def display_automaton(self):
        """
        Displays the FA with indications of initial states, terminal states, and the transition table.
        :return: nothing
        """
        alphabet_length = len(self.alphabet)  # get the length of the alphabet
        max_transition_length = retrieve_max_transition_length(self.transitions)  # get the length of the longest
        if general_functions.all_int(self.states):
            length_table = general_functions.total_table_length(alphabet_length,
                                                                max_transition_length, 5)  # get the length
        else:
            longest_state = general_functions.retrieve_longest_state(self.states)  # get the length of the longest state
            length_table = general_functions.total_table_length(alphabet_length, max_transition_length, longest_state)

        # of the table in terms of characters
        size_box = length_table // alphabet_length + 1

        # --------------------------------------------------------------------------------------------------------------
        # display of the upper border of the table
        # --------------------------------------------------------------------------------------------------------------
        # if we are at the beginning of the table, we display the top left corner
        print("┌", end="")
        print("─" * (size_box - 3), end="")
        for i in range(alphabet_length):
            print("┬", end="")
            print("─" * (size_box - 3), end="")
        print("┐")

        # --------------------------------------------------------------------------------------------------------------
        # display of the alphabet
        # --------------------------------------------------------------------------------------------------------------
        state_placing = f"│{'S':^{size_box - 3}}"  # calculate the spacing for the state S place
        alphabet_line = "│".join(
            f"{alphabet:^{size_box - 3}}" for alphabet in self.alphabet)  # calculate the spacing for the
        # alphabet line and join the elements of the alphabet with the vertical line
        alphabet_line = f"│{alphabet_line}│"
        print(state_placing + alphabet_line)  # display the alphabet line

        # --------------------------------------------------------------------------------------------------------------
        # display the border between the alphabet and the states
        # --------------------------------------------------------------------------------------------------------------
        print("├", end="")
        print("─" * (size_box - 3), end="")
        for i in range(alphabet_length):
            print("┼", end="")
            print("─" * (size_box - 3), end="")
        print("┤")

        # --------------------------------------------------------------------------------------------------------------
        # display all the states with its transitions
        # --------------------------------------------------------------------------------------------------------------
        for state in self.states:  # iterate through the states

            # check if the state is terminal, initial, both or none ----------------------------------------------------
            if state in self.terminal_states and state in self.initial_states:
                beginning_character = "│ ←→"  # if the state is both terminal and initial

            elif state in self.terminal_states:
                beginning_character = "│ ←"  # if the state is terminal

            elif state in self.initial_states:
                beginning_character = "│ →"  # if the state is initial

            else:
                beginning_character = "│ "  # the beginning character of the row

            # ----------------------------------------------------------------------------------------------------------
            if beginning_character == "│ ":
                row = f"{state}".center(size_box - 6) + " "
            elif beginning_character == "│ ←→":
                row = f"{state}".center(size_box - 10) + "   "
            elif beginning_character == "│ ←":
                row = f"{state}".center(size_box - 8) + "  "
            else:
                row = f"{state}".center(size_box - 8) + "  "
            # create a new string that will store the row of the current
            # state, and we convert the state into a string using f"{state}" to be able to concatenate it with
            # other strings

            for symbol in self.alphabet:  # iterate through the alphabet
                next_states = self.transitions.get((state, symbol), set())  # get the next states of the current state
                if next_states:  # if there are next states, we add them to the row
                    curr_state_str = ",".join(str(state) for state in next_states)  # convert the next states into a
                    # string
                    row += f"│{curr_state_str:^{size_box - 3}}"  # add the next states to the row
                else:
                    empty_transitions = "_" * max_transition_length
                    row += f"│{empty_transitions:^{size_box - 3}}"  # if there are no next states, we add an empty
                    # string to the row

            print(f"{beginning_character} {row}│")  # display the row

        # --------------------------------------------------------------------------------------------------------------
        # display of the lower border of the table
        # --------------------------------------------------------------------------------------------------------------
        print("└", end="")
        print("─" * (size_box - 3), end="")
        for i in range(alphabet_length):
            print("┴", end="")
            print("─" * (size_box - 3), end="")
        print("┘")

    def display_automaton_redirected(self, redirect_file_path: str):
        """
        Displays the FA with indications of initial states, terminal states, and the transition table.
        :return: nothing
        """
        alphabet_length = len(self.alphabet)  # get the length of the alphabet
        max_transition_length = retrieve_max_transition_length(self.transitions)  # get the length of the longest
        if general_functions.all_int(self.states):
            length_table = general_functions.total_table_length(alphabet_length,
                                                                max_transition_length, 5)  # get the length
        else:
            longest_state = general_functions.retrieve_longest_state(self.states)  # get the length of the longest state
            length_table = general_functions.total_table_length(alphabet_length, max_transition_length, longest_state)

        # of the table in terms of characters
        size_box = length_table // alphabet_length + 1

        # --------------------------------------------------------------------------------------------------------------
        # display of the upper border of the table
        # --------------------------------------------------------------------------------------------------------------
        # if we are at the beginning of the table, we display the top left corner
        with open(redirect_file_path, "a", encoding="utf-8") as output_file:
            output_file.write("┌")
            output_file.write("─" * (size_box - 3))
            for i in range(alphabet_length):
                output_file.write("┬")
                output_file.write("─" * (size_box - 3))
            output_file.write("┐" + "\n")

            # --------------------------------------------------------------------------------------------------------------
            # display of the alphabet
            # --------------------------------------------------------------------------------------------------------------
            state_placing = f"│{'S':^{size_box - 3}}"  # calculate the spacing for the state S place
            alphabet_line = "│".join(
                f"{alphabet:^{size_box - 3}}" for alphabet in self.alphabet)  # calculate the spacing for the
            # alphabet line and join the elements of the alphabet with the vertical line
            alphabet_line = f"│{alphabet_line}│"
            output_file.write(state_placing + alphabet_line + "\n")  # display the alphabet line

            # --------------------------------------------------------------------------------------------------------------
            # display the border between the alphabet and the states
            # --------------------------------------------------------------------------------------------------------------
            output_file.write("├")
            output_file.write("─" * (size_box - 3))
            for i in range(alphabet_length):
                output_file.write("┼")
                output_file.write("─" * (size_box - 3))
            output_file.write("┤" + "\n")

            # --------------------------------------------------------------------------------------------------------------
            # display all the states with its transitions
            # --------------------------------------------------------------------------------------------------------------
            for state in self.states:  # iterate through the states

                # check if the state is terminal, initial, both or none ------------------------------------------------
                if state in self.terminal_states and state in self.initial_states:
                    beginning_character = "│ ←→"  # if the state is both terminal and initial

                elif state in self.terminal_states:
                    beginning_character = "│ ←"  # if the state is terminal

                elif state in self.initial_states:
                    beginning_character = "│ →"  # if the state is initial

                else:
                    beginning_character = "│ "  # the beginning character of the row

                # ----------------------------------------------------------------------------------------------------------
                if beginning_character == "│ ":
                    row = f"{state}".center(size_box - 6) + " "
                elif beginning_character == "│ ←→":
                    row = f"{state}".center(size_box - 10) + "   "
                elif beginning_character == "│ ←":
                    row = f"{state}".center(size_box - 8) + "  "
                else:
                    row = f"{state}".center(size_box - 8) + "  "
                # create a new string that will store the row of the current
                # state, and we convert the state into a string using f"{state}" to be able to concatenate it with
                # other strings

                for symbol in self.alphabet:  # iterate through the alphabet
                    next_states = self.transitions.get((state, symbol),
                                                       set())  # get the next states of the current state
                    if next_states:  # if there are next states, we add them to the row
                        curr_state_str = ",".join(str(state) for state in next_states)  # convert the next states into a
                        # string
                        row += f"│{curr_state_str:^{size_box - 3}}"  # add the next states to the row
                    else:
                        empty_transitions = "_" * max_transition_length
                        row += f"│{empty_transitions:^{size_box - 3}}"  # if there are no next states, we add an empty
                        # string to the row

                output_file.write(f"{beginning_character} {row}│" + "\n")  # display the row

            # --------------------------------------------------------------------------------------------------------------
            # display of the lower border of the table
            # --------------------------------------------------------------------------------------------------------------
            output_file.write("└")
            output_file.write("─" * (size_box - 3))
            for i in range(alphabet_length):
                output_file.write("┴")
                output_file.write("─" * (size_box - 3))
            output_file.write("┘" + "\n")
