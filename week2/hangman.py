import random

wordlist = [
    "correction",
    "childish",
    "beach",
    "python",
    "assertive",
    "interference",
    "complete",
    "share",
    "credit card",
    "rush",
    "south",
]
# selects a random word from the wordlist
word = random.choice(wordlist)
# creates the hidden word
hidden = ""
# counts the mistakes
mistakes = 0
# string of wrong letters
wrong_letters = ""
# loop to create the hidden word
for i in word.split(" "):
    hidden += len(i) * "*" + " "


def stickman():
    """Prints the stickman"""
    parts = ["O", "|", "/", "\\", "/", "\\"]
    part_list = [" ", " ", " ", " ", " ", " "]
    for count in range(mistakes):
        part_list[count] = parts[count]
    print(hidden)
    print(
        """     ___
    |   |
    |   {0}
    |  {2}{1}{3}
    |   {1}
    |  {4} {5}
    |
    Wrong guesses: {wrong}""".format(
            *part_list, wrong=wrong_letters
        )
    )


def guess():
    """Asks for a letter, checks if it is valid and if it is in the word"""
    global wrong_letters
    global mistakes
    global hidden
    letter = input("Enter a letter: ")
    while (
        wrong_letters.count(letter) != 0
        or not 0 < len(letter) < 2
        or not letter.isalpha()
    ):
        letter = input("Enter a valid letter: ")
    if word.count(letter) > 0:
        for i in range(len(word)):
            if word[i] == letter:
                hidden = hidden[:i] + letter + hidden[i + 1 :]
        if hidden.count("*") == 0:
            return True
    else:
        wrong_letters += letter
        mistakes += 1
    stickman()


def play():
    """Plays the game"""
    stickman()
    win = False
    while mistakes < 6:
        win = guess()
        if win:
            print("You win")
            break
    if mistakes > 5:
        print("You Lost")


# starts the game
play()
