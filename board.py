class Board(object):
    def __init__(self,size):
        """Holds currently played tiles and values on special spots."""
        if size <= 0:
            raise ValueError("Board size must be greater than 0")
        self.size = size
        self.isEmpty = True
        self.board = [['.'] * self.size] * self.size


    def _checkBoundsPlace(self,wd_pos,direct):
        if self.isEmpty:
            mid_pos = [self.size//2]*2
            if mid_pos not in wd_pos:
                raise ValueError("First word placement must cross the center square of the board [%i,%i]"%(mid_pos[0],mid_pos[1]))
        if wd_pos[0][0] < 0 or wd_pos[0][1] < 0 or wd_pos[0][0] >= self.size or wd_pos[0][1] >= self.size:
            raise ValueError("Input position [%i,%i] is outside of board size"%(wd_pos[0][0],wd_pos[0][1]))
        if wd_pos[-1][0] >= self.size or wd_pos[-1][1] >= self.size:
            raise ValueError("Based on input position [%i,%i] word (%i squares %s) cannot fit on board"%(wd_pos[0][0],wd_pos[0][1],len(wd_pos),direct))

    def _checkOverlap(self,wd_pos,word,direct):
        if direct == 'down' or direct == 'd':
            neighbor_mask = [[0,-1],[0,1]]
        else:
            neighbor_mask = [[-1,0],[1,0]]
        isOL = False
        for pp,cc in zip(wd_pos,word):
            if self.board[pp[0]][pp[1]] != '.' and self.board[pp[0]][pp[1]] != cc:
                raise ValueError("Overlaped character is wrong")
            if self.board[pp[0]][pp[1]] != '.' and self.board[pp[0]][pp[1]] == cc:
                isOL = True
            for nm in neighbor_mask:
                if self.board[pp[0]+nm[0]][pp[1]+nm[1]] != '.':
                    #check that word formed from this locaiton is actualy a word
                    isOL = self._checkNeighborWord()
        return isOL
    
    def _checkNeighborWord(self):
        return True
        
    def addWord(self,posit,direct,word,dictionary):
        if direct not in ['down','up','d','u']:
            raise ValueError('Direction must be one of down, d, up, or u input: %s'%direct)
        if direct == 'down' or direct == 'd':
            wd_pos = [[posit[0]+ii,posit[1]] for ii in range(len(word))]
        else:
            wd_pos = [[posit[0],posit[1]+ii] for ii in range(len(word))]
        self._checkBoundsPlace(wd_pos,direct)
        if not self.isEmpty:
            self._checkOverlap(wd_pos,word,direct)
        for pp,cc in zip(wd_pos,word):
            if self.board[pp[0]][pp[1]] != '.':
                self.board[pp[0]][pp[1]] = cc
    
    
    
    def sideLen(self):
        return self.size
