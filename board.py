class Board(object):
    def __init__(self,size):
    """Holds currently played tiles and values on special spots."""
        if size <= 0:
            raise ValueError("Board size must be greater than 0")
        self.size = size
        self.board = [['.'] * self.size] * self.size




    def sideLen(self):
        return self.size
