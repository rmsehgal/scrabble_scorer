


class Board(object):
    def __init__(self,size):
        if size <= 0:
            raise ValueError("Board size must be greater than 0")
        self.size = size
        self.board = [['.']*self.size]*self.size

    def sideLen(self):
        return self.size
