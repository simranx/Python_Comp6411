import random

class StringDatabase:

    """
    @author: Simranjeet Singh

    The main motive of this class is to access and read the file given.
    Then to use the inbuilt random functionality to choose a random word from the list.
    And returning the word and sending it to the guess.py file for further use.

    """


    words = []

    def __init__(self):

        """
        Initializing the values of instance members for the new object.
        """
        with open("four_letters.txt", "r") as f:
            self.words = f.read().split()

    def select_new_word(self):

        """

        This method basically accesses the file, split the words from space and then selects a random word from it.

        :return: It returns the selectedWord which is the random word sleected from the word file.
        """

        with open("four_letters.txt", "r") as f:
            self.words = f.read().split()
        selectedWord = random.choice(self.words)
        return selectedWord
