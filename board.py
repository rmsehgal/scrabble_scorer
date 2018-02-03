


class Board(object):
    _size = 15

    def __init__(self):
        self.board = [['.']*self._size]*self._size

    def __len__(self):
        return self._size
