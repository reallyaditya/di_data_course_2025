from anagram_checker import AnagramChecker


def show_menu():
    """
    Displays the menu and gets the user's choice.

    :return: The user's choice (a word or an empty string to exit).
    """
    choice = (
        input(
            """Menu:
    # Type a word
    # Or press Enter to leave
     :  """
        )
        .strip()
        .lower()
    )
    # Keep asking until the user enters a valid word or presses Enter
    while not choice.isalpha() and choice != "":
        choice = input("Enter a valid single word: ")
    return choice


def word_anagrams(word):
    """
    Finds and prints the anagrams of a given word.

    :param word: The word to find anagrams for.
    """
    word = AnagramChecker(word)
    print(
        f"""
YOUR WORD: {word.word}
this is a valid English word
Anagrams for your word: {word.valid_anagram_list()}"""
    )


def main():
    """
    Main function to run the anagram finder.
    """
    user = show_menu()
    word_anagrams(user)


main()
