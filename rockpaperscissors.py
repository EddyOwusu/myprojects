import random

user_win = 0
computer_win = 0

options = ["rock", "scissors", "paper"]

print("Welcome to my Rock Paper Scissors Game")

while True:
    user_input = input("Choose rock, paper, scissors or q ")
    if user_input == "q":
        break


    if user_input not in options:
        print("choose one  of the options")
        continue
    
    random_number = random.randint(0,2)
    computer_input = options[random_number]
    print(f"Computer picked {computer_input}.")

    if user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_win += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_win += 1
    elif user_input == "scissor" and computer_input == "paper":
        print("You won!")
        user_win += 1
    else:
        print("computer won!")
        computer_win += 1

games_played = user_win + computer_win

print(f"You played {games_played} games")

print(f"Computer won {computer_win} times")

print(f"You won {user_win} times")

print("Good bye!")


    


