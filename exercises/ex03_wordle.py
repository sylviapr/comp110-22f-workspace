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
        idx = idx+1
    return(emoji_result)

def input_guess(exp_length: int) -> str:
    print 
