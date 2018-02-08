class Board(object):
    def __init__(self,size):
        """Holds currently played tiles and values on special spots."""
        if size <= 0:
            raise ValueError("Board size must be greater than 0")
        self.size = size
        self.isEmpty = True
        self.board = [['.'] * self.size] * self.size


    def _checkBounds(self,wd_pos,direct):
        if wd_pos[0][0] < 0 or wd_pos[0][1] < 0 or wd_pos[0][0] >= self.size or wd_pos[0][1] >= self.size:
            raise ValueError("Input position [%i,%i] is outside of board size"%(wd_pos[0][0],wd_pos[0][1]))
        if wd_pos[-1][0] >= self.size or wd_pos[-1][1] >= self.size:
            raise ValueError("Based on input position [%i,%i] word (%i squares %s) cannot fit on board"%(wd_pos[0][0],wd_pos[0][1],len(wd_pos),direct))
        
    def addWord(self,posit,direct,word):
        if direct == 'down':
            wd_pos = [[posit[0]+ii,posit[1]] for ii in range(len(word))]
        else:
            wd_pos = [[posit[0],posit[1]+ii] for ii in range(len(word))]
        self._checkBounds(wd_pos,direct)
        if self.isEmpty:
            #need to check that the word will be added to mid pt
            mid_pos = [self.size//2]*2
            if mid_pos not in wd_pos:
                raise ValueError("First word placement must cross the center square of the board [%i,%i]"%(mid_pos[0],mid_pos[1]))
            
            for pp,cc in zip(wd_pos,word):
                self.board[pp[0]][pp[1]] = cc

                
    
    def sideLen(self):
        return self.size
