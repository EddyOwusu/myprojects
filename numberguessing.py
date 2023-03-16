import random

top_of_range = input("type in a number ")
guess = 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range  <= 0:
        print("type in number greater than 0")
        quit()

else:
    print("Next time type in numbers")

random_number = random.randrange(1, top_of_range)

print(f"guess a  number  betweeen 0 and {top_of_range}")

while True:
    user_guess = input("make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guess += 1
    else:    
        print("type in number greater than 0")
        continue

    if user_guess == random_number:
        print("You are right")
        break
    else:
        print("You are wrong")

print(f"you guessed {guess} times before you had it correct")

if guess >= (1/2 * user_guess):
    print("Sorry you are not lucky, you guessed more than neccessary")
    quit()
else:
    print("Good, you are very lucky, you guessed within the range")

    
        

        

