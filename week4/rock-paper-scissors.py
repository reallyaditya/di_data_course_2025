from game import Game


def get_user_menu_choice():
    """
    Presents the user with a menu of options and returns their choice.
    The options are to play a new game, show the scoreboard, or quit.
    """
    choice = input(
        """Menu:
    (1) Play a new game
    (2) Show scores
     #  Press Enter to leave
     :  """
    )
    while choice not in ["1", "2", ""]:
        choice = input("Enter a valid choice: ")
    return choice


def print_results(results):
    """
    Prints the game results (wins, losses, draws) to the console.
    Args:
        results (dict): A dictionary containing the number of wins, losses, and draws.
    """
    print(
        f"""Game Results:
    You won {results['Win']} times
    You lost {results['Loss']} times
    You drew {results['Draw']} times"""
    )


def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    It displays the menu, gets user input, plays the game,
    updates the scoreboard, and prints the results.
    """
    scoreboard = {"Win": 0, "Loss": 0, "Draw": 0}
    choice = get_user_menu_choice()
    while choice != "":
        if choice == "1":
            new_game = Game()
            scoreboard[new_game.play()] += 1
        else:
            print_results(scoreboard)
        choice = get_user_menu_choice()
    print("Hope you had fun!")


# Run the main function when the script is executed
main()
