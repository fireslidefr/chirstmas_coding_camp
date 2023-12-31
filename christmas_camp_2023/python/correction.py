#!/usr/bin/env python3

import os # for the clear() function
import random

clear = lambda: os.system('clear') # can clear the window using clear()

# try si le str est un int ou non
def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# affiche le mot secret
def show_secret_word(secret_word, life):
    print("The secret word is :")
    end_value = " "
    for i in range(len(secret_word)):
        if (i == len(secret_word) - 1):
            end_value = "\n"
        print(secret_word[i], end = end_value)
    print("number of tries left :", life)

# verifie la win
def check_win(secret_word):
    for letter in secret_word:
        if (letter == "_"):
                return False
    return True

# vérifie les arguments, init = first time, update = every loop
def check_args(args, state, letters_count):
    if (state == "init"):
        if (len(args) != 2):
            return False
        elif (not is_int(args[0]) or not is_int(args[1])):
            return False
        else :
            return True
    elif (state == "update"):
        if (len(args) < 1):
            return False
        elif (len(args) == 1):
            if (args[0] != "no"):
                return False
        else:
            if (args[0] != "yes"):
                return False
            else :
                for i in range(1, len(args)):
                    if (not is_int(args[i])):
                        return False
                    elif (int(args[i]) > letters_count):
                        return False
        return True

# initialisation de variables
args = []
letters_count = 0
secret_word = []
life = 0
is_end = False
alphabet = 'abcdefghijklmnop'

# game
while(not check_args(args, "init", 0)):
    clear()
    print("veuillez entrer le nombre de lettre dans votre mot suivi du nombre de vies que la machine aura")
    args = input().split()
letters_count = int(args[0])
secret_word = ["_" for i in range(letters_count)]
life = int(args[1])

# update
while (not is_end):
    clear()
    # en cas de loose
    if (life <= 0):
        print("I lost my bad")
        is_end = True
    # en cas de win
    elif (check_win(secret_word)):
        print("I won !!!")
        is_end = True
    elif (len(alphabet) == 0):
        print("I have no more letters in my alphabet, are you sure you answered right ?")
        is_end = True
    # sinon reprise du jeu
    else :
        letter = random.choice(alphabet)
        alphabet = alphabet.replace(letter, '')
        while (not check_args(args, "update", letters_count)):
            clear()
            show_secret_word(secret_word, life)
            print("\nIs the letter :", letter, "in there ?")
            args = input().split()
        if (args[0] == "no"):
            life -= 1
        elif (args[0] == "yes"):
            for i in range(1, len(args)):
                secret_word[int(args[i]) - 1] = letter
    args = []
