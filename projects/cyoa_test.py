"""A fun BuzzFeed-style quiz to determine how Southern someone is."""


player: str = ""
menu_choice: int = 0

def main() -> None:
    """The main function."""
    points: int = 0
    greet()
    # Put the option picking in main
    menu_choice = input(f"Nice to meet you, {player}! What would you like to do next? \n Enter 1 to start our Southern Phrases Quiz \n Enter 2 to start our Southern Foods Quiz \n Enter 3 to exit the game \n ")
    while menu_choice != 1 and menu_choice != 2 and menu_choice != 3:
        print("Bless your heart, that's not a valid input! Can you please try again? ")
        menu_choice = input("What would you like to do next? \n Enter 1 to start our Southern Phrases Quiz \n Enter 2 to start our Southern Foods Quiz \n Enter 3 to exit the game \n ")
 
    if menu_choice == 1:
        phrases_quiz()
    
    if menu_choice == 2:
        foods_quiz()
    
    if menu_choice == 3:
        return("Thanks for playing! Y'all come back now, y'hear?")

    # if menu_choice != 1 and menu_choice != 2 and menu_choice != 3:
    #     print("Bless your heart, that's not a valid input! Can you please try again? ")
    #     menu_choice = input("What would you like to do next? \n Enter 1 to start our Southern Phrases Quiz \n Enter 2 to start our Southern Foods Quiz \n Enter 3 to exit the game \n ")


def greet() -> None:
    global player
    player = str(input("Howdy! Welcome to our quiz to determine how Southern you are! What's your name? "))
    return(f"Nice to meet you, {player}! You're fixin to have a whole lotta fun! ")

def phrases_quiz() -> None:
    print("phrases quiz")



def foods_quiz() -> None:
    print("foods quiz")


    





if __name__ == "__main__":
    main()