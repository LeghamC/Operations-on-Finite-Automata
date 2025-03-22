# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project main file - Manipulations of automata
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES
import automata as a
import operations as op
import properties_check as pc
import word_recognition as wr
import general_functions as gf

# TODO : complete merge all functions
# TODO : Delete all the non-used part of the menu
# TODO : Adapt the menu with your function's specifities
if __name__ == '__main__':
    end = False
    while end == False:
        gf.display_menu()
        user_automaton = int(input("Enter the number corresponding to the automaton you want to manipulate or type -1 to "
                                   "exit: "))
        if user_automaton == -1:
            end = True
        else:
            FA = a.FiniteAutomaton()
            FA.read_automaton_from_file(f"Automatons/automaton_{user_automaton}.txt")
            FA.display_automaton()

            #STANDARDIZATION ON DEMAND
            if pc.is_standard(FA) == True:
                stop = input(
                    "The automaton is already standard. Do you want to continue and determinize it ? \nIf you want "
                    "to continue press y. If you want to exit press n : ")
                if stop == 'n' or stop == 'N':
                    end = True
            else:
                want_standard = input("The automaton is not standard. Do you want to standardize it ? Press y for yes, "
                                      "n for no :")
                if want_standard == 'y' or want_standard == 'Y':
                    print("Here is your standardized automaton :")
                    FA = op.standardization(FA)
                    print("Here is your automata : ")
                    FA.display_automaton()
                    stop = input("Do you want to continue and determinize it ? \nIf you want to continue press y. If you want to exit press n : ")
                    if stop == 'n' or stop == 'N':
                        end = True

                else:
                    stop = input(
                        "Do you want to continue and determinize it ? \n If you want to continue press y. If you want to exit press n : ")
                    if stop == 'n' or stop == 'N':
                        end = True

                # DETERMINIZATION AND COMPLETION
                CDFA = a.FiniteAutomaton()


                if pc.is_an_automaton(FA) == True:
                    CDFA = FA
                elif pc.is_deterministic(FA) == True:
                    if pc.is_complete(FA) == True:
                        CDFA = FA
                    else:
                        op.completion(FA)
                else:
                    CDFA = op.determinization_and_completion_of_automaton(FA)
                CDFA.display_automaton()
                stop = input(
                    "Do you want to continue and minimize it ? \n If you want to continue press y. If you want to exit press n : ")
                if stop == 'n' or stop == 'N':
                    end = True

                #MINIMIZATION

                print("Here is your minimized automaton : ")
                MCDFA = op.minimization(CDFA)
                MCDFA.display_automaton()
                stop = input(
                    "Do you want to continue test de word recognition ? \n If you want to continue press y. If you want to exit press n : ")
                if stop == 'n' or stop == 'N':
                    end = True

                #WORD RECONGNITION

                word = wr.read_word(word)
                while word != '.':
                    wr.recognize_word(word, MCDFA.alphabet)
                    wr.read_word(word)
                top = input(
                    "Do you want to continue test complementary language ? \n If you want to continue press y. If you want to exit press n : ")
                if stop == 'n' or stop == 'N':
                    end = True

                #COMPLEMENTARY LANGUAGE

                AComp = op.complementary_automaton(FA)
                AComp.display_automaton()
                word = wr.read_word(word)
                while word != '.':
                    wr.recognize_word(word, MCDFA.alphabet)
                    wr.read_word(word)

                top = input("Should we test a different automaton ? If you want to restart press y else press n :")
                if stop == 'n' or stop == 'N':
                    end = True
                else:
                    print(f"Your last automaton was the number {user_automaton}")

        pass