# ---------------------------------------------------------------------------------------------------------------
# Name:        Operations-on-Finite-Automata
# Author:      ...
# Purpose:     Project word recognition file - reading of a word and indication of if is recognized or not
# Created:     01/03/2025
# ---------------------------------------------------------------------------------------------------------------
# IMPORTATIONS OF MODULES


'''
 * @brief : Reads a string/word from the user and stores it
 * @param word : string/word given by the user
 * @return :
'''
def read_word (word):
    pass


'''
 * @brief : Verifies if an automaton A recognizes an input word.  
 * @param word : string/word given by the user
 * @param A : automaton that try to recognize a word
 * @return a boolean  with 1: the word is recognized, 0 else
 '''
def recognize_word (word, A):
    for initial_state in A.initial_states:

        state = initial_state
        for letter in word:
            if (state, letter) in A.transitions:
                state = A.transitions[(state, letter)]
            else:
                break
        if state in A.terminal_states:
            return True

    return False


def recognize_word_recursive(word, A):
    for I in A.initial_states:
        if temp_word_recognition(A, word, I, -1):
            return True
    return False


def temp_word_recognition(A, word, state, id):
    if id >= len(word) - 1:
        if state in A.terminal_states:
            return True

    else:

        if (state, word[id + 1]) and (state, "ε") not in A.transitions:
            return False

        for next_state in A.transitions[state, "ε"]:
            if temp_word_recognition(A, word, next_state, id):
                return True

        for next_state in A.transitions[state, word[id + 1]]:
            if temp_word_recognition(A, word, next_state, id + 1):
                return True


    return False