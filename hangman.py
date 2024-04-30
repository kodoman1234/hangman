#!/usr/bin/env python3
name = input("enter your name: ")
print(f"Hi {name}!, Welcome to Hangman Game!, lets start to play.")

secret_word = "Metallica"
guess_string = ""
lives = 10

try:
    while lives > 0:

        character_left = 0

        for character in secret_word:
            
            if character in guess_string:
                print(character)
            else:
                print("-")
                character_left += 1

        if character_left == 0:
            print("Congratulations, You won!")
            break
        

        guess = input("Guess a letter: ")
        if guess != "m":
            guess_string += guess

        if guess not in secret_word:
            lives -= 1
            print("Wrong guess!:(")
            print(f"You have {lives} left.")
            if lives == 0:
                print("Game is over. You lost.")  
except KeyboardInterrupt:
    print("You're leaving the game!.")