class Board(object):
    """Holds currently played tiles and values on special spots."""
    def __init__(self, size):
        self.size = size
        self.board = [['.'] * self.size] * self.size




    def sideLen(self):
        return self.size
