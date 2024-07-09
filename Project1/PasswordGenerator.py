import random
import time

list_of_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                ".", "/", "]", "[", ";", "=", "-", "+", "_", ")", "(", "*", "&",
                "^", "%", "$", "#", "@", "!", "~", "`", ")"]

number_of_passwords = int(input("How many passwords do you want to generate: "))
# password_length = int(input("How much length: "))

for i in range(0,number_of_passwords):
    password = random.sample(list_of_char, 5)
    print(password)
    time.sleep(1)
