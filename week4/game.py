from random import choice


class Game:
    """
    A class to represent a Rock-Paper-Scissors game.
    It handles user input, computer choice, and determining the game result.
    """

    def __init__(self):
        """
        Initializes a new game by getting the user's item and the computer's item.
        """
        self.user = self.get_user_item()
        self.comp = self.get_computer_item()

    @staticmethod
    def get_user_item():
        """
        Gets the user's choice of item (rock, paper, or scissors).
        It prompts the user for input and validates it.
        Returns:
            str: The user's choice ('r', 'p', or 's').
        """
        user = input("Select (r)ock, (p)aper, (s)cissors: ")
        while user not in list("rps"):
            user = input("Please enter a valid input: ")
        return user

    @staticmethod
    def get_computer_item():
        """
        Gets the computer's choice of item (rock, paper, or scissors).
        The computer randomly chooses one of the three options.
        Returns:
            str: The computer's choice ('r', 'p', or 's').
        """
        return choice(["p", "r", "s"])

    def get_game_result(self):
        """
        Determines the result of the game based on the user's and computer's choices.
        Returns:
            str: The result of the game ('Win', 'Loss', or 'Draw').
        """
        if (
            self.user == "p"
            and self.comp == "r"
            or self.user == "r"
            and self.comp == "s"
            or self.user == "s"
            and self.comp == "p"
        ):
            return "Win"
        elif self.user == self.comp:
            return "Draw"
        return "Loss"

    def play(self):
        """
        Plays a single round of the Rock-Paper-Scissors game.
        It prints the user's choice, the computer's choice, and the game result.
        Returns:
            str: The result of the game ('Win', 'Loss', or 'Draw').
        """
        print(
            f"You chose: {self.user}. The computer chose: {self.comp}. Result: {self.get_game_result()}"
        )
        return self.get_game_result()
