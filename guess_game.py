# Write a program in your favorite programming language to try to guess a number you have chosen from 0-99. 
# The program should print out the number it is guessing, and then you should tell it whether 
# the guess is too high, too low, or correct. 

def guess_game():
    print("Think of a number between 0 and 99")
    print("I will try to guess it")
    low = 0
    high = 99
    while True:
        guess = (low + high) // 2
        print(f"My guess is {guess}")
        response = input("Is this guess too high, too low, or correct? ")
        if response == "correct":
            print("I guessed it!")
            break
        elif response == "too high":
            high = guess - 1
        elif response == "too low":
            low = guess + 1
        else:
            print("Invalid response, please enter too high, too low, or correct")


guess_game()

