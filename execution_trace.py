import automata
import operations
import properties_check
import general_functions
import word_recognition as WR


def get_execution_trace(num_automaton: int, word_to_test: str, file_name: str):
    """

    :param word_to_test: the word you want to test
    :param num_automaton : the number of the corresponding automaton you want to get the trace
    :param file_name: the file where you want to get the execution trace
    :return: nothing
    """

    # Set up the automaton with the corresponding number
    FA = automata.FiniteAutomaton()
    FA.read_automaton_from_file(f"Automatons/Automaton_{num_automaton}.txt")

    menu_str = general_functions.display_menu()  # get the menu in a variable, it contains the exact one as the
    # one showing on the terminal
    mid_menu_str = general_functions.display_mid_menu()

    with open(file_name, "w", encoding="utf-8") as trace:
        trace.write(menu_str + "\n")
        trace.write("[TERMINAL] Enter the number corresponding to the automaton you want to manipulate or type -1 to "
                    "exit: \n")
        trace.write("[USER] " + str(num_automaton) + "\n")
        trace.write("\n")
        trace.write("[TERMINAL] Here is the display of the automaton you are manipulating: \n")
    FA.display_automaton_redirected(file_name)
    trace.close()

    # -------------- Standardization ----------------------------------
    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write(mid_menu_str + "\n")
        trace.write("[USER] 1\n")
    if properties_check.is_standard(FA):
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write("[TERMINAL] The automaton is already standard.\n\n")
        trace.close()
    else:
        FA = operations.standardization(FA)
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write("[TERMINAL] The standardized version of the automaton is the following: \n")
            FA.display_automaton_redirected(file_name)

    trace.close()
    # ------------------------------------------------------------------

    # ---------------- Determinization and completion -------------------
    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write(
            "[TERMINAL] Displays the menu again in order for the user to choose the operation he wants to do: \n")
        trace.write("[USER] 2" + "\n")
    trace.close()

    if properties_check.is_asynchronous(FA):
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write("\nThe automaton you selected was asynchronous. Hence, we determinized it using the "
                        "asynchronous method.\n")
        # We determinize the asynchronous automaton
        trace.close()
        CDFA_A = operations.determinization_asynchronous(FA)

        # We now check if it also needs to be completed
        complete_A = properties_check.is_complete(CDFA_A)
        if complete_A == 1:
            with open(file_name, "a", encoding="utf-8") as trace:
                trace.write("\nThe automaton is already deterministic and complete.\n")
            trace.close()
            CDFA_A.display_automaton_redirected(file_name)

        # if the automaton is deterministic but not complete
        else:
            operations.completion(CDFA_A)
            with open(file_name, "a", encoding="utf-8") as trace:
                trace.write("\nThe automaton was already deterministic but not complete. Hence, we completed it.\n")
            trace.close()
            CDFA_A.display_automaton_redirected(file_name)

    # Else we want to determinize and complete a synchronous automaton
    deterministic_conditions = properties_check.is_deterministic(FA)

    # if the automaton is already deterministic
    if all(condition == 1 for condition in deterministic_conditions):
        complete_S = properties_check.is_complete(FA)
        if complete_S == 1:
            with open(file_name, "a", encoding="utf-8") as trace:
                trace.write("\nThe automaton is already deterministic and complete.\n")
            trace.close()
            FA.display_automaton_redirected(file_name)

        # if the automaton is deterministic but not complete
        else:
            operations.completion(FA)
            with open(file_name, "a", encoding="utf-8") as trace:
                trace.write("\nThe automaton was already deterministic but not complete. Hence, we completed it.\n")
            trace.close()
            FA.display_automaton_redirected(file_name)

    # else the automaton was not deterministic, and we determinize it
    else:
        CDFA_S = automata.FiniteAutomaton()
        CDFA_S = operations.determinization_and_completion_automaton(FA)

        # We now have the determinized our automaton but we need to check if it complete

        if properties_check.is_complete(CDFA_S):
            if properties_check.is_complete(CDFA_S):
                with open(file_name, "a", encoding="utf-8") as trace:
                    trace.write("\nThe automaton has been determininized and was already complete after "
                                "determinization.\n")
                trace.close()
                CDFA_S.display_automaton_redirected(file_name)

        else:
            operations.completion(CDFA_S)
            with open(file_name, "a", encoding="utf-8") as trace:
                trace.write("\nThe automaton has been determininized and as it was not complete, we completed it.\n")
            trace.close()
            CDFA_S.display_automaton_redirected(file_name)

    trace.close()
    # ------------------------------------------------------------------

    # # ------ Minimization part ---------------------------------------
    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write(
            "[TERMINAL] Displays the menu again in order for the user to choose the operation he wants to do: \n")
        trace.write("[USER] 3" + "\n")

    deterministic_conditions = properties_check.is_deterministic(FA)
    complete = properties_check.is_complete(FA)

    if all(condition == 1 for condition in deterministic_conditions) and complete == 1:
        MCDFA = operations.minimization(FA)
        MCDFA.display_automaton_redirected(file_name)
    elif all(condition == 1 for condition in deterministic_conditions) and complete == 0:
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write("The automaton you entered was deterministic but not complete."
                        "Hence, we completed it before minimizing it."
                        "\nThe minimized automaton is the following: \n")
        CDFA = operations.determinization_and_completion_automaton(FA)
        MCDFA = operations.minimization(CDFA)
        MCDFA.display_automaton_redirected(file_name)

    else:
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write(
                "The automaton you entered was not deterministic. Hence, we determinized and if needed completed"
                "it before minimizing it."
                "\n The minimized automaton is the following: \n")
        CDFA = operations.determinization_and_completion_automaton(FA)
        MCDFA = operations.minimization(CDFA)
        MCDFA.display_automaton_redirected(file_name)

    trace.close()
    # --------------------------------------

    # -------------Word recognition-----------------------------
    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write(
            "\n[TERMINAL] Displays the menu again in order for the user to choose the operation he wants to do: \n")
        trace.write("[USER] 4" + "\n")
        trace.write("[TERMINAL] Enter a word you want to read : \n")
        trace.write("[USER] " + word_to_test + "\n")
    if WR.recognize_word(word_to_test, FA):
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write(f"[TERMINAL] The automaton recognizes the word '{word_to_test}'.\n")
    else:
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write(f"[TERMINAL] The automaton does not recognize the word '{word_to_test}'.\n")
    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write("\nATTENTION YOU HAVE TO COPY WHAT IS RIGHT AFTER AND PASTE IT AFTER THE USER 5\n")
    trace.close()
    # ----------------------------------------------------------

    # -------------Word recognition-----------------------------
    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write(
            "\n[TERMINAL] Displays the menu again in order for the user to choose the operation he wants to do: \n")
        trace.write("[USER] 5" + "\n")
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write("The automaton recognizing the complementary language of the current automaton is the "
                        "following: \n")
        CFA = operations.complementary_automaton(FA)
        CFA.display_automaton_redirected(file_name)
    trace.close()
    # ----------------------------------------------------------

    # ----------------Word recognition of the complementary language --------------------------------------
    with open(file_name, "a", encoding="utf-8") as trace:
        trace.write(
            "\n[TERMINAL] Displays the menu again in order for the user to choose the operation he wants to do: \n")
        trace.write("[USER] 6" + "\n")
        trace.write("[TERMINAL] Enter a word you want to read : \n")

    CFA = operations.complementary_automaton(FA)
    if WR.recognize_word(word_to_test, CFA):
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write(f"The automaton recognizing the complementary language of the current automaton recognizes the"
                  f"word '{word_to_test}'.\n'.")
    else:
        with open(file_name, "a", encoding="utf-8") as trace:
            trace.write(f"The automaton recognizing the complementary language of the current automaton does not "
                  f"recognize the word '{word_to_test}'.\n'.")
    # -------------------------------------- -----------------------------------------------------------

# Modify here The order of the parameters is : num_automaton_to_test, the_word_to_test(to be chosen randomly by you)
# , the destination file
get_execution_trace(31, "ab", "execution_traces/execution_trace_automaton_31.txt")
