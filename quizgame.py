print("Welcome to Ed's Quiz Game")
playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    print("See you next time")
    quit()
    
print("Great! lets play")
score = 0

answer = input("What does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("What does GPU Stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("What does RAM Stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("What does PSU Stand for? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect")

print("Congratulation! you are done")
print(f"You scored {score} out of 4 for this quiz")
print(f"You scored {(score/4) * 100} percent")