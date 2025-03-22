import automata
import operations
import properties_check
import general_functions


def get_execution_trace(num_automaton: int, file_name: str):
    """

    :param num_automaton : the number of the corresponding automaton you want to get the trace
    :param file_name: the file where you want to get the execution trace
    :return: nothing
    """

    # Set up the automaton with the corresponding number
    FA = automata.FiniteAutomaton()
    FA.read_automaton_from_file(f"Automatons/Automaton_{num_automaton}.txt")

    with open(file_name, "w", encoding="utf-8") as trace:
        menu_str = general_functions.display_menu()  # get the menu in a variable, it contains the exact one as the
        # one showing on the
        # terminal

        trace.write(menu_str + "\n")
        trace.write("[TERMINAL] Enter the number corresponding to the operation you want to do: \n")
        trace.write("[USER] " + str(1) + "\n")
        trace.write("\n")
        trace.write("[TERMINAL] Enter the number corresponding to the automaton you want to manipulate: \n")
        trace.write("[USER] " + str(num_automaton) + "\n")
        trace.write(general_functions.display_mid_menu() + 2 * "\n")
        trace.write("[USER] I chose to display the automaton\n")
        trace.write("[TERMINAL] Here is the display of the automaton you are manipulating: \n")
        if properties_check.is_asynchronous(FA):
            trace.write(
                "[TERMINAL] The automaton is asynchronous it cannot be shown right now, it should be determined "
                "before\n")
            trace.write("[TERMINAL] Your automaton has been determined in order to display it\n")
    # Careful here, we have to check for asynchronous automaton as they cannot be displayed, it needs to be
    # determined first
    if properties_check.is_asynchronous(FA):
        new_FA = operations.determinization_asynchronous(FA)
        new_FA.display_automaton_redirected(file_name)
    else:
        FA.display_automaton_redirected(file_name)

    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write(menu_str + "\n")

    trace.close()


get_execution_trace(10, "Automatons/test.txt")
