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
        self.transitions = []  # The transitions of the automaton

    # ---------------------------------------------------------------------------------------------------------------

    #Methods of the class

    def read_automaton_from_file(self, filename: str) -> None:
        """
        Reads the automaton from a .txt file and stores it
        :param filename:
        :return:
        """
        with open(filename, "r") as file:
            first_lines = file.readlines()[:4]  # retrieve the first 4 lines as they contain
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

            #store the transitions (still in development)
            """for line in file:
                current_transition = line.strip()
                self.transitions.append(current_transition)"""




'''
 * @brief : Reads the FA from a .txt file and stores it
 * @param filename : The .txt file with the automata's propeties
 * @return : ...
 '''


def read_automaton_from_file(filename):
    pass


'''
 * @brief : Displays the FA with indications of initial states, terminal states, and the transition table.
 * @param FA : The FA that we want to display
 * @return : ...
 '''


def display_automaton(FA):
    pass


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
print(test.transitions)
