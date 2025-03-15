# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project automata file - Lecture and display of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import operations
import properties_check
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
        # read to go to the next state

    # ---------------------------------------------------------------------------------------------------------------

    #Methods of the class

    def read_automaton_from_file(self, filename: str) -> None:
        """
        Reads the automaton from a .txt file and stores it
        :param filename: The .txt file with the automata's properties
        :return: None
        """
        with open(filename, "r") as file:
            lines = file.readlines()  # read the entire file and store it in a list of strings
            first_lines = lines[:4]  # retrieve the first 4 lines as they contain
            # the general information of the automaton | use readlines() as the first 4 lines are always the same

            #store the alphabet
            nb_elem_alphabet = first_lines[0].strip()  # .strip() removes the '\n' character, we get as a result a
            # string that contains the number of the symbols in the alphabet
            for i in range(int(nb_elem_alphabet)):  # we want to add the alphabet depending on the number of the
                # symbols in the alphabet, every alphabet starts with a than b and so on | int() converts the string
                self.alphabet.append(chr(97 + i))  # take the ASCII code of 'a' which is 97 and add i to it to get the
                # corresponding character

            #store the states
            nb_states = first_lines[1].strip()  # retrieve the number of states which is the second line
            for i in range(int(nb_states)):  # add the states depending on the number of states
                self.states.append(i)  # add the states from 0 to the number of states

            #store the initial states
            initial_states_line = first_lines[2].split()  # split the line into a list of strings
            nb_initial_states = initial_states_line[0].strip()  # retrieve the number of initial states
            for i in range(int(nb_initial_states)):  # add the initial states depending on the number of initial states
                self.initial_states.append(int(initial_states_line[i + 1]))  # add the initial states from the list

            #store the terminal states
            #we do the same as for the initial states
            terminal_states_line = first_lines[3].split()
            nb_terminal_states = terminal_states_line[0].strip()
            for i in range(int(nb_terminal_states)):
                self.terminal_states.append(int(terminal_states_line[i + 1]))

            #store the transitions
            transition_txt = lines[5:]  # retrieve the transitions from the file, skip the fifth line as it contains
            # only contain the number of transitions, but we can get it back by getting the length of the array with
            # len()
            for line in transition_txt:  # iterate through the transitions
                current_transition = line.strip().split()  # remove the '\n' character and split the different
                # strings into a list

                current_state = int(current_transition[0])  # retrieve the current state which is always the first
                # element

                symbol = current_transition[1]  # retrieve the symbol which is always the second element

                next_states = {int(state) for state in current_transition[2:]}  # retrieve the next states and
                # convert them into integers, the braces {} are used to create a set which ensure that the elements
                # are unique

                if (current_state, symbol) not in self.transitions:
                    self.transitions[(current_state, symbol)] = set()  # if the key is not in the dictionary, we add it
                self.transitions[(current_state, symbol)].update(next_states)  # add the next states to the current key

    def display_automaton(self):
        alphabet_length = len(self.alphabet)  # get the length of the alphabet
        max_transition_length = retrieve_max_transition_length(self.transitions)  # get the length of the longest
        print("maximum transition length : ", max_transition_length)
        length_table = general_functions.total_table_length(alphabet_length, max_transition_length)  # get the length
        # of the table in terms of characters
        size_box = length_table // alphabet_length + 1

        # --------------------------------------------------------------------------------------------------------------
        # display of the upper border of the table
        # --------------------------------------------------------------------------------------------------------------
        # if we are at the beginning of the table, we display the top left corner
        print("┌", end="")
        print("─" * (size_box-3), end="")
        for i in range(alphabet_length):
            print("┬", end="")
            print("─" * (size_box-3), end="")
        print("┐")

        # --------------------------------------------------------------------------------------------------------------
        # display of the alphabet
        # --------------------------------------------------------------------------------------------------------------
        state_placing = f"│{'S':^{size_box-3}}"  # calculate the spacing for the state S place
        alphabet_line = "│".join(f"{alphabet:^{size_box-3}}" for alphabet in self.alphabet)  # calculate the spacing for the
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
        for state in self.states:
            if state in self.terminal_states and state in self.initial_states:
                beginning_character = "│↔"  # if the state is both terminal and initial
                row = [f"{state}".ljust(size_box-5)]  # create a list that will store the row of the current state, we convert
                # the state into a string using f"{state}" to be able to concatenate it with other strings
            elif state in self.terminal_states:
                beginning_character = "│←"  # if the state is terminal
                row = [f"{state}".ljust(size_box-5)]
            elif state in self.initial_states:
                beginning_character = "│→"  # if the state is initial
                row = [f"{state}".ljust(size_box-5)]
            else:
                beginning_character = "│ "  # the beginning character of the row
                row = [f"{state}".ljust(size_box-5)]

            for symbol in self.alphabet:
                next_states = self.transitions.get((state, symbol), set())  # get the next states of the current state
                if next_states:
                    row.append(", ".join(map(str, next_states)))  # if there are next states, we add them to the row
                else:
                    row.append("__")  # if there are no next states, we add "__" to the row

            print(beginning_character + " | ".join(row) + " |")  # display the row

        # --------------------------------------------------------------------------------------------------------------
        # display of the lower border of the table
        # --------------------------------------------------------------------------------------------------------------
        print("└", end="")
        print("─" * (size_box - 3), end="")
        for i in range(alphabet_length):
            print("┴", end="")
            print("─" * (size_box - 3), end="")
        print("┘")


'''
 * @brief : Displays the FA with indications of initial states, terminal states, and the transition table.
 * @param FA : The FA that we want to display
 * @return : ...
 '''


def display_automaton(FA):
    automaton_array = []  # create an empty array to store the automaton so that we will be easier to display it later
    for i in range(len(FA.states)):  # iterate through the states
        automaton_array.append([])  # for each state, we create an array that will store the state we can reach from
        # the current state


'''
 * @brief : Displays the CDFA with indications of initial states, terminal states, and the transition table.
 * @param CDFA : The FA that we want to display
 * @return : ...
 '''


def display_complete_dererministic_automaton(CDFA):
    pass


'''
 * @brief : Displays the MCDFA with indications of initial states, terminal states, and the transition table.
 * @param MCDFA : The MCDFA that we want to display
 * @return : ...
 '''


def display_minimal_automaton(MCDFA):
    pass


