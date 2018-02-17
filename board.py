import enum

EMPTY_SPOT = '.'

class Directions(enum.Enum):
    DOWN = 1
    RIGHT = 2

    @classmethod
    def from_str(cls, direction_str):
        if direction_str.lower() in {'down', 'd'}:
            return cls.DOWN
        if direction_str.lower() in {'right', 'r'}:
            return cls.RIGHT
        raise ValueError('Cannot parse direction string: {}'.format(direction_str))


class Board(object):

    def __init__(self, size):
        """Holds currently played tiles and values on special spots."""
        if size <= 0:
            raise ValueError('Board size must be greater than 0')
        self.size = size
        self.is_empty = True
        self.board = [[EMPTY_SPOT for ii in range(self.size)] for ii in range(self.size)]


    def _check_bounds_place(self, wd_pos, direct):
        if self.is_empty:
            mid_pos = [self.size//2]*2
            if mid_pos not in wd_pos:
                raise ValueError('First word placement must cross the center square of the board [%i,%i]'%(mid_pos[0], mid_pos[1]))
        if wd_pos[0][0] < 0 or wd_pos[0][1] < 0 or wd_pos[0][0] >= self.size or wd_pos[0][1] >= self.size:
            raise ValueError('Input position [%i,%i] is outside of board size'%(wd_pos[0][0], wd_pos[0][1]))
        if wd_pos[-1][0] >= self.size or wd_pos[-1][1] >= self.size:
            raise ValueError('Based on input position [%i,%i] word (%i squares %s) cannot fit on board'%(wd_pos[0][0], wd_pos[0][1], len(wd_pos), direct))

    def _check_overlap(self, wd_pos, word, direct, dictionary):
        if direct == Directions.DOWN:
            neighbor_mask = [[0, -1], [0, 1]]
        else:
            neighbor_mask = [[-1, 0], [1, 0]]
        is_ol = False
        for char_point, character in zip(wd_pos, word):
            if self.board[char_point[0]][char_point[1]] != EMPTY_SPOT and self.board[char_point[0]][char_point[1]] != character:
                raise ValueError('Overlaped character is wrong')
            if self.board[char_point[0]][char_point[1]] != EMPTY_SPOT and self.board[char_point[0]][char_point[1]] == character:
                is_ol = True
            for nm in neighbor_mask:
                if self.board[char_point[0]+nm[0]][char_point[1]+nm[1]] != EMPTY_SPOT:
                    #check that word formed from this locaiton is actualy a word
                    wd_neig = self._get_neighbor_word(character, char_point, neighbor_mask)
                    if wd_neig not in dictionary:
                        raise ValueError('Neighboring word is not in dictionary: %s at %i,%i'%(wd_neig, char_point[0], char_point[1]))
                    else:
                        is_ol = True
        if not is_ol:
            raise ValueError('Word does not connect to any on the board')


    def _get_neighbor_word(self, int_char, int_point, move_mask):

        wd_pos = [[int_point[0], int_point[1]]]
        for mm in move_mask:
            char_point = [int_point[0]+mm[0], int_point[1]+mm[1]]
            while 0 <= char_point[0] < self.size and 0 <= char_point[1] < self.size and self.board[char_point[0]][char_point[1]] != EMPTY_SPOT:
                wd_pos.append(char_point)
                char_point = [char_point[0]+mm[0], char_point[1]+mm[1]]
        #since words are either on a row or colum one of the indexes of the positions
        # will be constant, so calling sort will return the correct ordering of the word even
        # if we start adding from the middle
        wd_pos.sort()
        return ''.join([self.board[char_point[0]][char_point[1]] if char_point != int_point else int_char for char_point in wd_pos])

    def add_word(self, posit, direction_str, word, dictionary):
        direct = Directions.from_str(direction_str)
        if word not in dictionary:
            raise ValueError('Input word: %s is not in the dictionary'%word)
        if direct == Directions.DOWN:
            wd_pos = [[posit[0]+ii, posit[1]] for ii in range(len(word))]
        else:
            wd_pos = [[posit[0], posit[1]+ii] for ii in range(len(word))]
        self._check_bounds_place(wd_pos, direct)
        if not self.is_empty:
            self._check_overlap(wd_pos, word, direct, dictionary)

        for char_point, character in zip(wd_pos, word):
            if self.board[char_point[0]][char_point[1]] == EMPTY_SPOT:
                self.board[char_point[0]][char_point[1]] = character
        self.is_empty = False


    def side_len(self):
        return self.size
