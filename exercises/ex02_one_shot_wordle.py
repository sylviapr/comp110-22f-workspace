"""An expansion of our previous exercise, Chardle!"""

__author__ = "730575415"

secret_word: str = "python"

guess: str = str(input("What is your 6-letter guess? "))
while len(guess) != len(secret_word):
    guess = input("That was not 6 letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite! Play again soon! ")
# Problem: "Additionally, be sure you are using 
# f-String templates rather than concatenation 
# for this output." How?


