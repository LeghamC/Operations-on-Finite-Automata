# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata as A
import properties_check as PC
import operations as OP
import general_functions as GF
import word_recognition as WR


def main():

    while True:

        GF.display_menu()
        user_automaton = int(input("\nEnter the number corresponding to the automaton you want to manipulate or type -1 to exit: "))

        # We check if the user entered a valid number
        while user_automaton not in range(1, 45) and user_automaton != -1:
            print("\nYou entered an invalid number. As there are 44 automata, you need to enter a number between 1 and 44.")
            user_automaton = int(input("\nEnter the number corresponding to the automaton you want to manipulate or type -1 to exit: "))

        # If the user wants to exit
        if user_automaton == -1:
            print("\nYou chose to exit the program. Goodbye! :)")
            break

        # else the user did not exit and we start loading the automaton on which he wants to work with
        FA = A.FiniteAutomaton()
        FA.read_automaton_from_file(f"Automatons/automaton_{user_automaton}.txt")
        FA.display_automaton()

        # We ask the user what operation he wants to do on the automaton
        while True:
            GF.display_mid_menu()
            choice = int(input("\nEnter the number corresponding to the operation you want to do: "))

            # 0. Back to the main menu
            if choice == 0:
                break

            # 1. Standardization
            elif choice == 1:
                if PC.is_standard(FA):
                    print("\nThe automaton is already standard.")
                else:
                    SFA = OP.standardization(FA)
                    print("\nThe standardized version of the automaton if the following: ")
                    SFA.display_automaton()


            # 2. Determinization and completion
            elif choice == 2:

                # We check if the automaton we want to determinize is synchronous or asynchronous
                if PC.is_asynchronous(FA):
                    print(
                        "\nThe automaton you selected was asynchronous. Hence, we determinized it using the "
                        "asynchronous method.")

                    # Determinize the asynchronous automaton
                    CDFA_A = OP.determinization_asynchronous(FA)

                    # Check if it needs to be completed
                    complete_A = PC.is_complete(CDFA_A)
                    if complete_A == 1:
                        print("\nThe automaton is already deterministic and complete.")
                        CDFA_A.display_automaton()
                    else:
                        OP.completion(CDFA_A)
                        print("\nThe automaton was already deterministic but not complete. Hence, we completed it.")
                        CDFA_A.display_automaton()

                else:
                    # Check if the automaton is already deterministic
                    deterministic_conditions = PC.is_deterministic(FA)

                    if all(condition == 1 for condition in deterministic_conditions):
                        # Automaton is already deterministic
                        complete_S = PC.is_complete(FA)
                        if complete_S == 1:
                            print("\nThe automaton is already deterministic and complete.")
                            FA.display_automaton()
                        else:
                            OP.completion(FA)
                            print("\nThe automaton was already deterministic but not complete. Hence, we completed it.")
                            FA.display_automaton()
                    else:
                        # Determinize and complete the synchronous automaton
                        CDFA_S = OP.determinization_and_completion_automaton(
                            FA)

                        if PC.is_complete(CDFA_S):
                            print(
                                "\nThe automaton has been determinized and was already complete after determinization.")
                            CDFA_S.display_automaton()
                        else:
                            OP.completion(CDFA_S)
                            print("\nThe automaton has been determinized and as it was not complete, we completed it.")
                            CDFA_S.display_automaton()



            # 3. Minimization
            # We must have a deterministic and complete automaton to minimize it

            elif choice == 3:
                # Check if the automaton is asynchronous
                if PC.is_asynchronous(FA):
                    print("\nThe automaton you selected was asynchronous. Hence, we determinized it using the asynchronous method.")

                    # Determinize the asynchronous automaton
                    CDFA = OP.determinization_asynchronous(FA)

                    # Ensure the automaton is complete before minimization
                    if not PC.is_complete(CDFA):
                        CDFA = OP.completion(CDFA)
                        print("\nThe automaton was asynchronous, determinized, but not complete. Hence, we completed it before minimization.")

                    # Minimize the completed deterministic automaton
                    print("\nThe minimized automaton is the following:")
                    MCDFA = OP.minimization(CDFA)
                    MCDFA.display_automaton()


                else:
                    # Handle synchronous automaton minimization
                    deterministic_conditions = PC.is_deterministic(FA)
                    complete = PC.is_complete(FA)

                    # If the automaton is already deterministic and complete, minimize directly
                    if all(condition == 1 for condition in deterministic_conditions) and complete == 1:
                        print("\nThe automaton is already deterministic and complete. Minimizing directly:")
                        MCDFA = OP.minimization(FA)
                        MCDFA.display_automaton()


                    # If the automaton is deterministic but not complete, complete before minimization
                    elif all(condition == 1 for condition in deterministic_conditions) and complete == 0:
                        print("\nThe automaton you entered was deterministic but not complete."
                              " Hence, we completed it before minimizing it."
                              "\nThe minimized automaton is the following: ")
                        CDFA = OP.completion(FA)
                        MCDFA = OP.minimization(CDFA)
                        MCDFA.display_automaton()

                    # If the automaton is not deterministic, determinize, complete, and minimize it
                    else:
                        print("\nThe automaton you entered was not deterministic. Hence, we determinized and, if needed, completed"
                              " it before minimizing it."
                              "\nThe minimized automaton is the following: ")
                        CDFA = OP.determinization_and_completion_automaton(FA)
                        MCDFA = OP.minimization(CDFA)
                        MCDFA.display_automaton()


            # 4. Word recognition
            elif choice == 4:
                word = WR.read_word()
                if WR.recognize_word(word, FA):
                    print(f"\nThe automaton recognizes the word '{word}'.")
                else:
                    print(f"\nThe automaton does not recognize the word '{word}'.")


            # 5. Complementary language
            elif choice == 5:
                CFA = OP.complementary_automaton(FA)
                print("\nThe automaton recognizing the complementary language of the current automaton is the following: ")
                CFA.display_automaton()


            # 6 Word recognition of the complementary language
            elif choice == 6:
                word = WR.read_word()
                CFA = OP.complementary_automaton(FA)
                if WR.recognize_word(word, CFA):
                    print(f"\nThe automaton recognizing the complementary language of the current automaton recognizes the word '{word}'.")
                else:
                    print(f"\nThe automaton recognizing the complementary language of the current automaton does not recognize the word '{word}'.")


        # If the user wants to exit the program
        restart = input("\nDo you want to test a different automaton? (y/n): ").strip().lower()
        if restart != 'y':
            print("\nGoodbye!")
            break


if __name__ == '__main__':
    main()
