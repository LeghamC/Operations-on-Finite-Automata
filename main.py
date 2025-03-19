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

end = False

while end == False :
    user_automaton = input("Enter the number corresponding to the automaton you want to manipulate: ")


    FA = a.FiniteAutomaton()
    FA.read_automaton_from_file(f"Automatons/automaton_{user_automaton}.txt")
    FA.display_automaton()

    #STANDARDIZATION ON DEMAND
    if op.is_standard(FA) == True :
        stop = input("The automaton is already standard. Do you want to continue and determinize it ? \n If you want to continue press y. If you want to exit press n : ")
        if stop == 'n' or stop == 'N' :
            end = True
    else :
        want_standard = input("The automaton is not standard. Do you want to standardize it ? Press y for yes, n for no :")
        if want_standard == 'y' or want_standard == 'Y':
            print("Here is your standardized automaton :")
            FA = op.standardization(FA)
            FA.display_automaton()
            stop = input(
                "Do you want to continue and determinize it ? \n If you want to continue press y. If you want to exit press n : ")
            if stop == 'n' or stop == 'N':
                end = True

        else :
            stop = input("Do you want to continue and determinize it ? \n If you want to continue press y. If you want to exit press n : ")
            if stop == 'n' or stop == 'N':
                end = True

        # DETERMINIZATION AND COMPLETION
        if isinstance(FA, a.FiniteAutomaton) ==






    pass








