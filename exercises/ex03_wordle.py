"""A complete Wordle game with multiple guesses!"""

__author__ = "730575415"


def contains_char(search_through: str, search_for: str) -> bool:
    """Returns True if the one-character second input is found anywhere in the first input, returns False otherwise."""
    assert len(search_for) == 1
    i: int = 0
    while i < len(search_through):
        if search_through[i] != search_for:
            i = i + 1
            if i == len(search_through):
                return False
        else:
            return True
    return True
    # This function is used for determining if a given character ever occurs in a given word. This will be used in our emojified function to determine what emojis should correspond to specific characters in a guess.
    # If the given character that we're searching for is found at any index in the word we're searching through, the function returns True. 
    # If the character is not found in the word being searched through, the function returns False.


def emojified(guess: str, secret: str) -> str:
    """When given two strings of the same length, returns emoji feedback that signals how closely the user's guess matches the secret word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_result: str = ""
    idx: int = 0
    while idx < len(secret):
        if contains_char(secret, guess[idx]) is True and secret[idx] == guess[idx]:
            emoji_result = emoji_result + GREEN_BOX
        else:
            if contains_char(secret, guess[idx]) is True:
                emoji_result = emoji_result + YELLOW_BOX
            if contains_char(secret, guess[idx]) is False:
                emoji_result = emoji_result + WHITE_BOX
        idx = idx + 1
    return (emoji_result)
    # This function gives our user the visual emoji feedback that is a key feature of Wordle.
    # First, the function asserts that the length of the user's guess is the same length as the secret word.
    # Then, it uses the contains_char function to search each index of the guess for matches with each index of the secret word.
    # If an index in the guess matches the same index of the secret word, a green emoji is added to our emoji result.
    # If the character of an index in the guess appears in the secret word but at a different index, a yellow emoji is added.
    # And if the character of an index in the guess never appears in the secret word, a white box is added.
    # The final result is a string of colored emoji boxes that tells the user how closely their guess matches the secret word.


def input_guess(exp_length: int) -> str:
    """Asks for a string and loops until a string of the specified length is entered."""
    guess: str = str(input(f"Enter a {exp_length} character word: "))
    while exp_length != len(guess):
        guess = input(f"That wasn't {exp_length} chars! Try again: ")
    return (guess)
    # This function simply asks the user for an input of a certain length and loops until the user provides the correct number of characters.


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    secret_len: int = len(secret_word)
    turn_count: int = 1
    guess: str = ""
    while turn_count < 7 and guess != secret_word:
        print("=== Turn " + str(turn_count) + "/6 ===")
        guess = str((input_guess(secret_len)))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            return print(f"You won in {turn_count}/6 turns!")
        turn_count = turn_count + 1
    return print("X/6 - Sorry, try again tomorrow!")
    # This function cmobines all of our previous functions into one. 
    # First, variables are established for the secret word, the secret's length, the number of turns the player has taken, and the player's guess.
    # Then, a loop begins. The player sees their turn count and enters a guess word. If the guess word is not the requested length, the input_guess function loops until the player gives a guess that is of the correct length.
    # Once the player enters a guess that is the right length, the emojified function provides emoji feedback.
    # If the player guessed the secret word correctly, they receive a message of congratulations below the all-green emoji feedback and the function ends.
    # If the player guessed incorrectly but still has turns left, they see the turn count and are prompted to enter another guess after receiving emoji feedback.
    # And if the player guessed incorrectly on their last turn, they get a message to try again later below their emojis.


if __name__ == "__main__":
    main()