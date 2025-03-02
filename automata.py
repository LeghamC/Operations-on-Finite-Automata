# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project automata file - Lecture and display of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES


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
                print(current_transition[0])
                current_state = int(current_transition[0])  # retrieve the current state which is always the first
                # element
                symbol = current_transition[1]  # retrieve the symbol which is always the second element

                next_states = {int(state) for state in current_transition[2:]}  # retrieve the next states and
                # convert them into integers, the braces {} are used to create a set which ensure that the elements
                # are unique

                if (current_state, symbol) not in self.transitions:
                    self.transitions[(current_state, symbol)] = set()  # if the key is not in the dictionary, we add it
                self.transitions[(current_state, symbol)].update(next_states)  # add the next states to the current key


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


test = FiniteAutomaton()
test.read_automaton_from_file("Automatons/project_automaton_test.txt")
print(test.alphabet)
print(test.states)
print(test.initial_states)
print(test.terminal_states)
print(test.transitions)
