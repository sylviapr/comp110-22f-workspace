"""A fun game that picks a random integer between 1 and 100 and has the user try to guess it."""

__author__ = "730575415"

from random import randint
points: int = 0
player: str = ""
adventure_points: int = 0
menu_choice: int = 0
COWBOY_EMOJI: str = "\U0001F920"


def main() -> None:
    """The main function that allows this file to be run as a module."""
    greet()
    global points
    points = 0
    i: int = 0
    menu_choice = int(input("What would you like to do next? \n Note: you need to reset your guess count after every attempt at the number guessing game \n Enter 1 to start our Number Guessing Game \n Enter 2 to reset your number of guesses \n Enter 3 to exit the game \n "))
    assert menu_choice == 1 or menu_choice == 2 or menu_choice == 3
    while i < 100 and menu_choice != 3:
        if menu_choice == 1:
            number_game()
            i += 1
            menu_choice = int(input("What would you like to do next? \n Note: you need to reset your guess count after every attempt at the number guessing game \n Enter 1 to start our Number Guessing Game \n Enter 2 to reset your total number of guesses for this session \n Enter 3 to exit the game \n "))
            assert menu_choice == 1 or menu_choice == 2 or menu_choice == 3
        if menu_choice == 2:
            points = reset_guess(points)
            print(f"You have {points} points. ")
            i += 1
            menu_choice = int(input("What would you like to do next? \n Note: you need to reset your guess count after every attempt at the number guessing game \n Enter 1 to start our Number Guessing Game \n Enter 2 to reset your total number of guesses for this session \n Enter 3 to exit the game \n "))
            assert menu_choice == 1 or menu_choice == 2 or menu_choice == 3
    if menu_choice == 3 and i < 100:
        print(f"Goodbye, {player}! You made a total of {adventure_points} guesses during this session. Thanks for playing!")
    if i >= 100:
        print(f"Wow, {player} you've been playing for a long time! Why don't you go take a break? See you again soon! ")


def greet() -> None:
    """The function that presents a greeting and asks the player to give their name, which will be assigned to the global variable player."""
    global player
    player = str(input(f"Howdy! {COWBOY_EMOJI} Welcome to our number guessing game! What is your name? "))
    print(f"Nice to meet you, {player}! In this game, the computer will pick a random integer between 1 and 100, and your job is to guess what it is based on the computer's hints. Your points will go up for every guess you make, so a lower score is better. ")


def number_game() -> None:
    """The actual game. The computer picks a random integer between 1 and 100, and the player has to guess what it is."""
    secret_number: int = randint(1, 100)
    global points
    global adventure_points
    guess: int = int(input(f"Okay {player}, I'm thinking of an integer between 1 and 100. What is it? "))
    if guess == secret_number:
        points += 1
        adventure_points += 1
        print(f"Wow, you guessed the number on your first try! Great job, {player}! ")
    else:
        while guess != secret_number:
            if guess > secret_number:
                print("Lower")
                points += 1
                adventure_points += 1
                guess = int(input("What is your new guess? "))
            if guess < secret_number:
                print("Higher")
                points += 1
                adventure_points += 1
                guess = int(input("What is your new guess? "))
        print(f"Correct, you got the number in {points} guesses! Good job {player}! ")


def reset_guess(pts: int) -> int:
    """Gives the player the option of resetting their guess counter, which is stored in the variable points."""
    menu_choice: int = int(input(f"{player}, are you sure you want to reset your guess count for this session? \n Enter 1 for yes \n Enter 2 for no "))
    assert menu_choice == 1 or menu_choice == 2
    if menu_choice == 1:
        print(f"Okay {player}, your total guess count has been reset. ")
        return 0
    if menu_choice == 2:
        print("Returning to the main menu")
        return pts
    return pts


if __name__ == "__main__":
    main()