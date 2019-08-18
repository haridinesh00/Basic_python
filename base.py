import os
import time
from diceroller import dice
import guess
import hangman
import currencyconvertor
import passwordgenerator
import tictactoe
import minesweeper

while True:
    os.system("clear")
    try:
        choice = int(input(("""Enter your choice:\n1.Dice Roller\n2.Guess the number game\n3.Hangman Game\n4.Currency convertor\n5.Random Password Generator\n6.Tic Tac Toe\n7.Minesweeper\n""")))
    except:
        print("Wrong input")
        time.sleep(0.2)
        continue
    os.system("clear")
    if choice == 1:
        dice()
        break
    elif choice == 2:
        guess()
    elif choice == 3:
        hangman()
    elif choice == 4:
        inrconvertor()
    elif choice == 5:
        passwordgenerator()
    elif choice == 6:
        tictactoe()
    elif choice == 7:
        minesweeper()
    else:
        print("Wrong Choice")
        time.sleep(0.3)
