import random # "random" library contains the functions related to random number generation.

MIN_NUMBER = 1
MAX_NUMBER = 100

guess_count = 0    
min_guess_count = MAX_NUMBER - MIN_NUMBER + 1  

while True:  # It is requested to enter the loop at least once, but because the condition cannot be written to the end of the loop in Python, an infinite loop was made.
    number = random.randint(MIN_NUMBER, MAX_NUMBER)  # randint(min,max) function returns a random integer between min and max.

    guess = int(input("Enter your guess:"))
    guess_count += 1

    while number != guess:
        if guess < number:
            print("UP!")
        else:
            print("DOWN!")

        guess = int(input("Enter your guess:"))
        guess_count = 1

    if guess_count < min_guess_count:    #YANLIŞ
        min_guess_count = guess_count

    print("CONGRATULATIONS! You guessed the number correctly.")
    print(f"You found the number randomly chosen by the computer in {guess_count} guesses.")

    replay = input("Do you want to play again(y/Y/n/N)?")
    while replay not in ['y', 'Y', 'n', 'N']:  # The in operator searches for a specific element in a list.  #YANLIŞ
        replay = input("Do you want to play again(y/Y/n/N)?")

    if replay == 'n' or replay == 'N':
        print("BYE")
        break

print(f"Minimum number of guesses:{min_guess_count}")