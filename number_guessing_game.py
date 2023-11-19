# Problem:
# Write an algorithm and a program for playing the guessing game of a randomly chosen number
# by the computer. The computer will choose a random number between [1-100] and the user
# will try to find this number with the least number of guesses. For this, after each guess
# the user enters, the computer should direct the user with the "UP" and "DOWN" messages.
# When the user finds the number, the message "CONGRATULATIONS" should be printed and
# it should be stated how many guesses the user made.


#Algorithm:
# MIN_NUMBER=1
# MAX_NUMBER=100
# 
# number=random.randint(MIN_NUMBER,MAX_NUMBER) # randint(min,max) function returns a random integer between min and max.
# 
# guess=input()
# guess_count=1
# 
# while (number!=guess):
#     if guess<number:
#         print("UP!")
#     else:
#         print("DOWN!")
# 
#     guess=input()
#     guess_count+=1
# 
# print("CONGRATULATIONS!")
# print(guess_count)


#Program:
import random # "random" library contains the functions related to random number generation.

MIN_NUMBER=1
MAX_NUMBER=100

number=random.randint(MIN_NUMBER,MAX_NUMBER) # randint(min,max) function returns a random integer between min and max.

guess=int(input("Enter a number between [1-100]:"))
guess_count=1

while (number!=guess):
    if guess<number:
        print("UP!")
    else:
        print("DOWN!")

    guess=int(input("Enter a number between [1-100]:"))
    guess_count+=1

print("CONGRATULATIONS! You guessed the number correctly.")
print(f"You found the number randomly chosen by the computer in {guess_count} guesses.")
