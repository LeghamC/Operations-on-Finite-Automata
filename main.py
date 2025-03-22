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
                    FA = OP.standardization(FA)
                    print("\nThe standardized version of the automaton if the following: ")
                    FA.display_automaton()


            # 2. Determinization and completion
            elif choice == 2:

                # We stock the conditions of determinism of the automaton (respected or not)
                deterministic_conditions = PC.is_deterministic(FA)

                # if the automaton contains an epsilon transition
                if deterministic_conditions[2] == 0:
                    print("The automaton is not deterministic as it contains an epsilon (ε) transition and it cannot be determinized by this method.\n"
                          "You need to use the determinization_asynchronous (3) method to determinize an automaton containing epsilon labels.")

                # if the automaton is already deterministic
                if all(condition == 1 for condition in deterministic_conditions):
                    complete = PC.is_complete(FA)
                    if complete == 1:
                        print("\nThe automaton is already deterministic and complete.")
                        FA.display_automaton()

                    # if the automaton is deterministic but not complete
                    else:
                        OP.completion(FA)
                        print("\nThe automaton was already deterministic but not complete. Hence, we completed it.")
                        FA.display_automaton()

                # else the automaton was not deterministic, and we determinize it
                else:
                    CDFA = A.FiniteAutomaton()
                    CDFA = OP.determinization_and_completion_automaton(FA)

                    # We now have the determinizaed automaton but we need to check if it complete

                    if PC.is_complete(CDFA):
                        if PC.is_complete(CDFA):
                            print("\nThe automaton has been determininized and was already complete after determinization.")
                            CDFA.display_automaton()

                    else:
                        OP.completion(CDFA)
                        print("\nThe automaton has been determininized and as it was not complete, we completed it.")
                        CDFA.display_automaton()

            # 3. Determinization_asynchronous
            elif choice == 3:

                deterministic_conditions = PC.is_deterministic(FA)

                # if the automaton does not contain an epsilon transition
                if deterministic_conditions[2] == 1:
                    print(
                        "The automaton does not contain an epsilon (ε) transition hence it should not be determinized by this method.\n"
                        "You need to use the determinization_and_completion_automaton (2) method to determinize an automaton containing epsilon labels.")

                else:
                    CDFA = OP.determinization_asynchronous(FA)
                    print("\nThe determinized asynchronous automaton is the following: ")
                    CDFA.display_automaton()



            # 4. Minimization
            # We must have a deterministic and complete automaton to minimize it

            elif choice == 4:

                # We check if the automaton is deterministic and complete
                deterministic_conditions = PC.is_deterministic(FA)
                complete = PC.is_complete(FA)


                # If the automaton is already deterministic and complete, we minimize it
                if all(condition == 1 for condition in deterministic_conditions) and complete == 1:
                    MCDFA = OP.minimization2(FA)
                    MCDFA.display_automaton()

                elif all(condition == 1 for condition in deterministic_conditions) and complete == 0:
                    print("\nThe automaton you entered was deterministic but not complete."
                          "Hence, we completed it before minimizing it."
                          "\nThe minimized automaton is the following: ")
                    CDFA = OP.determinization_and_completion_automaton(FA)
                    MCDFA = OP.minimization2(CDFA)
                    MCDFA.display_automaton()

                else:
                    print("\nThe automaton you entered was not deterministic. Hence, we determinized and if needed completed"
                          "it before minimizing it."
                          "\n The minimized automaton is the following: ")
                    CDFA = OP.determinization_and_completion_automaton(FA)
                    MCDFA = OP.minimization2(CDFA)
                    MCDFA.display_automaton()

            # 5. Word recognition
            elif choice == 5:
                word = WR.read_word()
                if WR.recognize_word(FA, word):
                    print(f"\nThe automaton recognizes the word '{word}'.")
                else:
                    print(f"\nThe automaton does not recognize the word '{word}'.")

            # 6. Complementary language
            elif choice == 6:
                CFA = OP.complementary_automaton(FA)
                print("\nThe automaton recognizing the complementary language of the current automaton is the following: ")
                CFA.display_automaton()


        # If the user wants to exit the program
        restart = input("\nDo you want to test a different automaton? (y/n): ").strip().lower()
        if restart != 'y':
            print("\nGoodbye!")
            break


if __name__ == '__main__':
    main()

