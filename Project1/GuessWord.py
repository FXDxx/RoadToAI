# Guess word game
import os
import random

'''def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear') '''

'''
# Guess the word/letter from given string
input_String = "Hello, my name is Faizan"
print(input_String)

guesses = 3
count = 1

while count <= guesses:
    count += 1
    word = input("Enter the letter: ")
    
    if word in input_String:
        print("Congratulations!")
        break
    elif word not in input_String:
        print("Try again..")
    if count > guesses:
        print("you failed..")
        break

'''

# Guess the word from the given list
print("Welcome to Word Guess Game")
name = input("What is your name? ")
print("Here",name,"input the word to match the given String/List")
# os.system("cls")
# Step 1: list is initialized
given_str = ["Apple", "Banana", "Cherry", "Mango", "Pineapple", "Guava", "Strawberry"]
# Step 2: random value is selected
guess_list = random.choice(given_str)
print(given_str)
# Step 3: initialization
count = 1
numberOfGuesses = 8
# Step 4: iterate through the process
while count <= numberOfGuesses:
    count += 1
    guess_word = input("Enter the word: ")

    if guess_word in guess_list:
        print("Congratulations!..You've guessed correctly.")
        break
    elif guess_word not in guess_list:
        print("Try again..")
    if count > numberOfGuesses:
        # os.system("cls")
        print("You failed..")
        break

'''1. Random class in imported
   2. Input list is taken
   3. random.choice() function is used to get random value from the list
   4. count and guesses are initialized
   5. loop is used to iterate unless count reaches the maximum number of guesses
   6. If count exceeds then print you failed'''
