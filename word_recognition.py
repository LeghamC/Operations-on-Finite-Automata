# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project word recognition file - reading of a word and indication of if is recognized or not
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES


'''
 * @brief : Reads a string/word from the user and stores it
 * @param word :
 * @return : string given by the user
'''
def read_word ():
    word = input("Enter a word you want to read : ")
    return word


'''
 * @brief : Verifies if an automaton A recognizes an input word.  
 * @param word : string/word given by the user
 * @param A : automaton that try to recognize a word
 * @return a boolean  with 1: the word is recognized, 0 else
 '''

def recognize_word(word, A):
    for I in A.initial_states:
        if temp_word_recognition(A, word, I, -1):
            return True
    return False


def temp_word_recognition(A, word, state, id):
    if id >= len(word) - 1:
        if state in A.terminal_states:
            return True



    if (state, "ε") in A.transitions:
        for next_state in A.transitions[state, "ε"]:
            if temp_word_recognition(A, word, next_state, id):
                return True

    if (state, word[id + 1]) in A.transitions:
        for next_state in A.transitions[state, word[id + 1]]:
            if temp_word_recognition(A, word, next_state, id + 1):
                return True

    return False