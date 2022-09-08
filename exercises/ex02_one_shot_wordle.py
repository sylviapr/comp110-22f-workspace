"""An expansion of our previous exercise, Chardle!"""

__author__ = "730575415"

secret_word: str = "python"
word_length: int = len(secret_word)

# Set up the secret word and the secret word's length.

guess: str = str(input(f"What is your {word_length}-letter guess? "))
while len(guess) != len(secret_word):
    guess = input(f"That was not {word_length} letters! Try again: ")

# Set up the prompt for user to enter a guess that must be the same length as the secret word.

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Initialized the variables for the emojis that will appear in the output.

index_checking: int = 0
emoji_result: str = ""

# Set up the variable to count what index the program is checking and the variable that will print as our emoji result once the while loop completes.

while index_checking < len(secret_word):
    # Set up a while loop so that each index of the user's guess is checked for both matching its corresponding index in the secret word and for possible matches with characters in other indices of the secret word.
    if guess[index_checking] == secret_word[index_checking]:
        emoji_result = emoji_result + GREEN_BOX
        # If the character in the index being checked in the guess matches the corresponding index in the secret word, a green box is added to the emoji output.
    else: 
        char_exists: bool = False
        alt_indices: int = 0 
        while char_exists is False and index_checking < len(secret_word) and alt_indices < len(secret_word):
            if secret_word[alt_indices] == guess[index_checking]:
                char_exists = True
                emoji_result = emoji_result + YELLOW_BOX
                # If the character in the guess index being checked doesn't match its secret word counterpart but does appear in the secret word in a different index, a yellow box is added.
            else:
                alt_indices = alt_indices + 1    
        if char_exists is False:
            emoji_result = emoji_result + WHITE_BOX
            # And finally, if the character in the index being checked doesn't appear in the secret word at all, a white box is added to the emoji output.

    index_checking = index_checking + 1

# The emoji output will be one string that is a series of emoji boxes concatenated based on the conditions above.

print(emoji_result)

# The emoji output is printed for the user to see.

if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite! Play again soon! ")

# And finally, the user gets either a celebration message if they guessed correctly, or encouragement to try again if they didn't.