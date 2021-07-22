import random

number = random.randrange(0,100)
guessedCorrectly = False

while guessedCorrectly == False:
    guessed = int(input("Guess the number between 1-100: "))
    if(number < guessed):
        print("\n Number is lower, try again")
    elif(number > guessed):
        print("\n Number is higher, try again!")
    else:
        print("You got the number!")
        guessedCorrectly = True