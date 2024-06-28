# Hangman Game
import random

# Step 1: consider a tuple
collections = ("Cat", "Dog", "Lion", "Chimpanzee", "Tiger", "Bird", "Horse")
print(collections)

# Step 2: Take random word from the list
word = random.choice(collections)
print(word)

# Step 3: Initialization
display = "_"*len(word)
chances = len(word)+2
count = 0

# Step 4: Iterate to match the letter and display according to position
while count < chances:
    letter = input("Enter a letter: ")

    if letter in word:
        display = " ".join(display[i] if word[i] != letter else letter for i in range(len(word)))
        print(display)
    elif letter not in word:
        print("_")
    if word == display:
        print("You won!")

    count += 1

'''1. Import Random class
   2. Consider a tuple
   3. Take a random word from the tuple
   4. Initialize chances, display and count
   5. Iterate to match the letter and display according to positions'''
