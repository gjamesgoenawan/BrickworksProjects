from time import sleep
from os import system
import random

player_count = 2

def clear():
    system("cls") 

def is_solved(hidden_word):
    if '□' in hidden_word: return False
    else: return True

def reveal_word(f, actual_word, hidden_word):
    for i in range (0,len(actual_word)):
        if actual_word[i] == f:
            hidden_word[i] = f
    return hidden_word

def format_word(pulled_word):
    actual_word = []
    hidden_word = []
    for i in pulled_word:
        actual_word.append(i)

    for i in actual_word:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            hidden_word.append('□')
        else:
            hidden_word.append(i)
    return actual_word, hidden_word

def print_word(word):
    for i in word:
        print(i, end="")
    print("") 

def next_player(currentplayer, maxplayer):
    return (currentplayer + 1 if currentplayer<maxplayer else 1)

word_list = open("word_list.txt", "r").readlines()



while True:
    currentplayer = 1
    random_index = random.randint(0, len(word_list)-1)
    pulled_word = word_list[random_index].strip().upper()
    done = False
    actual_word, hidden_word = format_word(pulled_word)
    while done == False:
        while True:
            clear()
            print("It's player "+ str(currentplayer) +"'s Turn!\n")
            print_word(hidden_word)
            choice = input("\n1)Guess A Letter\n2)Guess The Phrase\n>")
            if choice == "1" or choice == "2":
                break
            else:
                print("Please input 1 or 2")
                sleep(2)
                
        if choice.strip() == "1":
            clear()
            print_word(hidden_word)
            guess = input("\nPlayer "+ str(currentplayer) + ": Guess A Letter>").upper()
            if guess in actual_word:
                print("\nCorrect!")
                hidden_word = reveal_word(guess, actual_word, hidden_word)
            else:
                print("\nIncorrect! Your Turn Is Over!")
                currentplayer = next_player(currentplayer, player_count)
            done = is_solved(hidden_word)

        else:
            clear()
            print_word(hidden_word)
            guess = input("\nPlayer "+ str(currentplayer) + ": Guess The Phrase>").upper()
            if guess.strip() == pulled_word:
                print("\nCorrect!")
                done = True
            else:
                print("\nIncorrect! Your Turn Is Over!")   
                currentplayer = next_player(currentplayer, player_count) 
        sleep(2)
        
    print("Congratulations! Player " + str(currentplayer) +" Win!")
    done = False
    sleep(2)
        
        



