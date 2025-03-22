# Operations-on-Finite-Automata
Project of Finite Automata and Regular Expressions, P2-S4


## Introduction 
  This project aims to apply our knowledge of finite automata to create a program that allows users to perform various operations on a given automaton. As students, we designed this tool to standardize, determinize, minimize, and recognize words to better understand the key concepts in automata theory.

## Usage

This program allows you to load a finite automaton from an existing file and perform various operations on it.

### Selecting your automaton
At the beginning, you will be asked to enter the number of an automaton (between 1 and 44) or choose to exit. If you decide to continue, the wanted automaton will be displayed so you can have a look at it before choosing the operation you want to perform.

### Choosing on Operation
Once you choosed your automaton, you can perform one of the following operations: 
  1. Standardization
  2. Determinization and Completion
     1. For Synchronous Automaton
     2. For Asynchronous Automaton
  6. Minimization
  7. Word Recognition
  8. Complementary Language
     a. Get the Automaton
     b. Word Recognition of the Complementary Language

You can either enter the number corresponding to the operation you want to perform or return to the main menu at any time

## Features

### Display Automaton
This feature allows to have a look to the automaton at each stage of its transformation. 
![image](https://github.com/user-attachments/assets/884dc197-1a8d-478b-8bf9-f3227ab41a3c)

The S column represents the states. The arrows indicates whether a state is an initial state (->), a terminal state (<-) or both (<->). We also have as many columns as there are letters in the alphabet, where we put the next state for each transition.

### Standardization
This function standardizes a non-standard function and display it. If the automaton is already in standard form, the program will inform the user. 

### Determinization and Completion
This part of the code aims to determinize and complete the automaton. If the choosen automaton is deterministic, it will then check if it also complete. If it is the case, it will notify the user. Otherwise, it will complete the automaton. If the automaton is not deterministic, it will be both determinized *and* completed. After these operations, the resulting automaton will be displayed.

### Minimization
The program will check if the given automaton is minimized and notify the user if it already is. If not, it will minimize the automaton and display the updated version

### Word Recognition
If this operation is choosen, the user will be asked to enter a word. The program will then diplay whether the word is recognized by the automaton or not.
**Remark:** If you want to enter ε (the empty word) you just need to press enter. 


### Complementary Language
Similarly to word recognition, the user will enter a word, but this time the program will check if the word is recognized by the complementary language. In other words, it performs the opposite of word recognition. For example, if the word recognition returns that the word is accepted, the complementary language will return that the word is not accepted.




## Authors
Lélia GHEZALI, Killian KOULOURATH, Noah JEANDEAU, Idrissa BARRY, Yannis BENHAMED-AUBRY

