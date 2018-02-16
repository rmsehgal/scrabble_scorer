class Board(object):
    def __init__(self,size):
        """Holds currently played tiles and values on special spots."""
        if size <= 0:
            raise ValueError("Board size must be greater than 0")
        self.size = size
        self.isEmpty = True
        self.board = [['.' for ii in range(self.size)] for ii in range(self.size)]


    def _checkBoundsPlace(self,wd_pos,direct):
        if self.isEmpty:
            mid_pos = [self.size//2]*2
            if mid_pos not in wd_pos:
                raise ValueError("First word placement must cross the center square of the board [%i,%i]"%(mid_pos[0],mid_pos[1]))
        if wd_pos[0][0] < 0 or wd_pos[0][1] < 0 or wd_pos[0][0] >= self.size or wd_pos[0][1] >= self.size:
            raise ValueError("Input position [%i,%i] is outside of board size"%(wd_pos[0][0],wd_pos[0][1]))
        if wd_pos[-1][0] >= self.size or wd_pos[-1][1] >= self.size:
            raise ValueError("Based on input position [%i,%i] word (%i squares %s) cannot fit on board"%(wd_pos[0][0],wd_pos[0][1],len(wd_pos),direct))

    def _checkOverlap(self,wd_pos,word,direct,dictionary):
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
                    wd_neig = self._getNeighborWord(cc,pp,neighbor_mask)
                    if wd_neig not in dictionary:
                        raise ValueError('Neighboring word is not in dictionary: %s at %i,%i'%(wd_neig,pp[0],pp[1]))
                    else:
                        isOL = True
        if not isOL:
            raise ValueError("Word does not connect to any on the board")

    
    def _getNeighborWord(self,int_char,int_point,move_mask):

        wd_pos = [[int_point[0],int_point[1]]]
        for mm in move_mask:
            pp = [int_point[0]+mm[0],int_point[1]+mm[1]]
            while 0<=pp[0]<self.size and 0<=pp[1]<self.size and self.board[pp[0]][pp[1]] != '.':
                wd_pos.append(pp)
                pp = [pp[0]+mm[0],pp[1]+mm[1]]
        #since words are either on a row or colum one of the indexes of the positions
        # will be constant, so calling sort will return the correct ordering of the word even
        # if we start adding from the middle
        wd_pos.sort()
        return ''.join([self.board[pp[0]][pp[1]] if pp != int_point else int_char for pp in wd_pos])
        
    def addWord(self,posit,direct,word,dictionary):
        if direct not in ['down','right','d','r']:
            raise ValueError('Direction must be one of down, d, right, or r input: %s'%direct)
        if word not in dictionary:
            raise ValueError('Input word: %s is not in the dictionary'%word)
        if direct == 'down' or direct == 'd':
            wd_pos = [[posit[0]+ii,posit[1]] for ii in range(len(word))]
        else:
            wd_pos = [[posit[0],posit[1]+ii] for ii in range(len(word))]
        self._checkBoundsPlace(wd_pos,direct)
        if not self.isEmpty:
            self._checkOverlap(wd_pos,word,direct,dictionary)

        for pp,cc in zip(wd_pos,word):
            if self.board[pp[0]][pp[1]] == '.':
                self.board[pp[0]][pp[1]] = cc
        self.isEmpty = False
    
    
    def sideLen(self):
        return self.size
