"""
Dictionary class which holds all valid words
"""


class Dictionary(object): # pylint: disable=too-few-public-methods
    """
    Dictionary class which holds all valid words
    Will eventually support fast prefix and postfix searches,
    currently just supports word lookup
    """
    def __init__(self, word_list):
        """
        Input:
              word_list: python list containing all words in di
        """
        self.word_list = word_list

    def __contains__(self, word):
        """
        magic function to allow for calls like- word in Dictionary
        """
        return word in self.word_list

