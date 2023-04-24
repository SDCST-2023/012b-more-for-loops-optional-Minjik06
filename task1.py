#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random
ran=random.randint(1,100)
for i in range(10):
    a=int(input("Enter a Number between 0~99: "))
    if a==ran:
        print("You correct")
        exit()
    elif a<ran:
        print("Your answer is lower")
    else:
        print("Your answer is bigger")
print("the user has lost")