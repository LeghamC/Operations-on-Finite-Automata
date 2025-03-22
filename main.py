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
        user_automaton = int(input("Enter the number corresponding to the automaton you want to manipulate or type -1 to exit: "))

        # If the user wants to exit
        if user_automaton == -1:
            print("You chose to exit the program. Goodbye! :)")
            break

        # else the user did not exit and we star loading the automaton on which he wants to work with
        FA = A.FiniteAutomaton()
        FA.read_automaton_from_file(f"Automatons/automaton_{user_automaton}.txt")
        FA.display_automaton()

        # We ask the user what operation he wants to do on the automaton
        while True:
            print("\nSelect the operation you want to do on the automaton:")
            print("1. Standardize the automaton")
            print("2. Determinize and complete the automaton")
            print("3. Minimize the automaton")
            print("4. Word recognition")
            print("5. Get the automaton recognizing the complementary language of the current automaton")
            print("0. Back to the main menu")

        choice = int(input("Enter the number corresponding to the operation you want to do: "))

        # 0. Back to the main menu
        if choice == 0:
            break

        # 1. Standardization
        elif choice == 1:
            if PC.is_standard(FA):
                print("The automaton is already standard.")
            else:
                FA = OP.standardize(FA)
                print("The standardized version of the automaton if the following: ")
                FA.display_automaton()


        # 2. Determinization and completion
        elif choice == 2:

            # We stock the conditions of determinism of the automaton (respected or not)
            deterministic_conditions = PC.is_deterministic(FA)

            # if the automaton is already deterministic
            if all(condition == 1 for condition in deterministic_conditions):
                complete = PC.is_complete(FA)
                # we check if it is complete
                if properties_check.is_complete(FA):
                    print("The automaton is already deterministic and complete.")
                    return FA
                # else we complete it
                else:
                    completion(FA)
                    print("The automaton was already deterministic but not complete. Hence, we completed it.")
                    return FA


            if PC.is_deterministic(FA):
                print("The automaton is already deterministic.")
            else:
                FA = OP.determinize_and_complete(FA)
                print("The deterministic and completed version of the automaton is the following: ")
                FA.display_automaton()
                pass
