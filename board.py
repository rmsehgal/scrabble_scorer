


class Board(object):
    def __init__(self,size):
        self.size = size
        self.board = [['.']*self.size]*self.size

    def sideLen(self):
        return self.size
