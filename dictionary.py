


class Dictionary(object):
    def __init__(self,wordList):
        self.wordList = wordList

    def __contains__(self,word):
        return word in self.wordList
