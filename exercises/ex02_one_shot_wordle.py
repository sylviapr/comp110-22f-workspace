"""An expansion of our previous exercise, Chardle!"""

__author__ = "730575415"

secret_word: str = "python"
word_length: int = len(secret_word)

guess: str = str(input(f"What is your {word_length}-letter guess? "))
while len(guess) != len(secret_word):
    guess = input(f"That was not {word_length} letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite! Play again soon! ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_checking: int = 0
emoji_result: str = ""

while index_checking < len(secret_word):
    if guess[index_checking] == secret_word[index_checking]:
        emoji_result = emoji_result + GREEN_BOX
    else: 
        emoji_result = emoji_result + WHITE_BOX
    index_checking = index_checking + 1

print(emoji_result)



#length of index checking? How to get loop going there
