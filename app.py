#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

# Define global variables to store the score and the round number
score = 0
round = 0

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    global score # Use the global keyword to access and modify the score variable
    global round # Use the global keyword to access and modify the round variable
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        score += 1 # Increment the score by 1 if the user wins
        return "You win!"
    else:
        return "You lose!"

def play_game():
    global round # Use the global keyword to access and modify the round variable
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    round += 1 # Increment the round by 1 after each game
    print(f"Your score is {score} out of {round} rounds.") # Display the score and the round number

def play_again():
    answer = input("Do you want to play again? (y/n): ").lower()
    while answer not in ['y', 'n']:
        answer = input("Invalid answer. Do you want to play again? (y/n): ").lower()
    return answer == 'y'

if __name__ == "__main__":
    playing = True
    while playing:
        play_game()
        playing = play_again()
