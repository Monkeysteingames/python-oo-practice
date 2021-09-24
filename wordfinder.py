"""Word Finder: finds random words from a dictionary."""
from random import randint
from random import choice as rnd_choice


class WordFinder:
    """
    A class used to find a random word from a file

    Attributes
    -------------
    file_loc: str
        this is the local dir on the machine we're using
        that stores the grouping of words we're choosing
        from

    >>> wf = WordFinder("test.txt")
    3 words read

    >>> wf.random() in ["apple", "banana", "orange"]
    True
    """

    def __init__(self, file_loc):
        self.file_loc = file_loc
        self.words = self.read_file_make_words_list()
        print(f"{len(self.words)} words read")

    def read_file_make_words_list(self):
        """
        opens and reads file ->
        retrieves words from each line and creates a list 
        separated by each new line
        """
        f = open(self.file_loc, 'r')
        words_str = f.read(randint(1, 100))
        return list(words_str.split("\n"))

    def random(self):
        """
        returns a string of a random word from our words list
        created in the init
        """
        return rnd_choice(self.words)
