# Operations-on-Finite-Automata
Project of Finite Automata and Regular Expressions, P2-S4


## Introduction 



## Usage

This program allows you to load a finite automaton from an existing file and perform various operations in it.

### Selecting your automaton
At the beginning, you will be asked to enter the number of an automaton (between 1 and 44) or choose to exit. If you decide to continue, the wanted automaton wil be displayed so you can have a look at it before choosing the operation you want to perform.

### Choosing on Operation
Once you choosed your automaton, you can perform one of the following operations: 
  1. Standardization
  2. Determinization and completion
  3. Minimization
  4. Word recognition
  5. Complementary language
You can either enter the number corresponding to th operation you want to perform or return to the maine menu at any time

## Features
### Standardization
This function standardizes a non-standard funtcion and display it. If the automaton is already in standard form, the program will inform the user.

### Determinization and Completion
This part of the code aims to determinize and complete the automaton. If the choosen automaton is deterministic, it will then check if it also complete. If it is the case, it will notify the user. Otherwise, it will complete the automaton. If the automaton is not deterministic, it will be both determinized *and* completed. After these operations, the resulting automaton will be displayed.

### Minimization
The program will check if the given automaton is minimized and notify the user if it already is. If not, it will minimize the automaton and display the updated version

### Word Recognition
If this operation is choosen, the user will be asked to enter a word. The program will then diplay whether the word is recognized by the automaton or not.


## Authors
Lélia GHEZALI, Killian KOULOURATH, Noah JEANDEAU, Idrissa BARRY, Yannis BENHAMED-AUBRY

