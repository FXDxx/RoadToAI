# Guess Game
import random
print("Welcome to the Number Guessing")
print("You have 7 chances to guess the right number")

# Step 1:
lower_bound = int(input("Enter minimum number of Range: "))
upper_bound = int(input("Enter maximum number of Range: "))

# Step 2: Generate random number
random_num = random.randint(lower_bound, upper_bound)

i = 1
chances = 7
# Step 3: loop to iterate through guesses
while i <= chances:
    i += 1
    number = int(input("Enter a number between 1 and 100: "))
    if number > random_num:
        print("Too high...Try again")
    elif number < random_num:
        print("Too low..Try again")
    if number == random_num:
        print("Congratulations! You guessed correctly")
        break
    elif i > chances:
        print("Sorry.. you ran out of guesses.. Better luck next time")
        break

'''1. Random class in imported
   2. lower and upper bound of the range are selected
   3. random number is generated from the given range through predefined function (random.rand.int)
   4. count and chances for the guess are initialized
   5. loop is used to iterate through the guesses until user runs out of guesses or the user guess the right number.'''