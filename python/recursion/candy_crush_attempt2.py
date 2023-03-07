"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.


STEPS/thoughts: 

1. need to traverse and identify all numbers to crush 
    get three or more continuous candies with sliding window system

    make a 'seen' matrix

2. Then crush them and drop them 
    - fill tops with 0's 
    - drop or 'crush' null rows with values on top 

3. check if stable, 
    if not, redo! 
    if stable - RETURN

"""

class Solution:    
    """
    [0, 0, 810, 710, 610]

    
    """
    def candyCrush(self, board):
        n_rows = len(board)
        n_cols = len(board[0])
        flagged = [[False]*n_cols for row in range(n_rows)]
        curr_seq = [] # will be list of coordinates
        stable = False
        # need to go through every one of these coordinates since they can fail to be in one 
        # connected string but may be connected to a different one

        # EDGE CASE - if they are already in a curr_seq, then they can be taken out of seen already
        # GET CONNECTED CANDIES
        while stable == False:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    curr_seq = self.traverseBoard(i, j, curr_seq, flagged, board)
                    
                    if len(curr_seq) == 0:
                        stable = True
                        return board
                    else:
                        if len(curr_seq) >= 3:
                            for row, col in curr_seq:
                                flagged[row][col] = True                
                    curr_seq = []
            
            print(f'flagged')
            print(flagged)
            if self.checkStability(flagged):
                stable = True
                return board
            board = self.removeCandies(board, flagged)
        return board
    
    def checkStability(self, f):
        for i in len(range(f)):
            for j in len(range(f[0])):
                if f[i][j] == True:
                    return False
        # if all false return true
        return True

    def removeCandies(board, flagged):
        for col in range(len(flagged[0])):
            for row in range(len(flagged)):
                if board[row][col]:
                    board[row][col] = 0

            i = 0
            for j in range(len(flagged)):
                if board[j][col] != 0:
                    board[j][col], board[i][col] = board[i][col], board[j][col]
                    i += 1
        return board
                
    
    def isValid(self, board, row, col):
        """ check if row/col are in bounds"""
        if row < len(board) and row >= 0 and col >= 0 and col < len(board[0]):
            return True
        return False
    
    def getNeighbors(self, row, col):
        neighbors = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
        return neighbors        

    def traverseBoard(self, row, col,  curr_seq, flagged, board):
        if not self.isValid( board, row, col):
            return curr_seq
        if row >= len(board) or col >= len(board[0]):
            return curr_seq
        if flagged[row][col] != False:
            return curr_seq
        
        # traverse neighbors to check for stuff.
        neighbors = self.getNeighbors(row, col)
        for n in neighbors:
            next_row = n[0]
            next_col = n[1]
            if self.isValid( board, next_row, next_col) and board[row][col] == board[next_row][next_col] and [next_row, next_col] not in curr_seq:
                curr_seq.append([next_row, next_col])
                curr_seq = self.traverseBoard(next_row, next_col, curr_seq, flagged, board)
        return curr_seq

def crush_only(board, tracker):
    """ tracker = 1 indicates to crush this item
                = 0 do not crush
    """
    for col in range(len(board[0])):
        bottom_idx = len(board) - 1

        for row in range(len(board)-1, -1, -1):
            if tracker[row][col] == 0:                
                board[bottom_idx][col] = board[row][col]
                bottom_idx -= 1
        
        for row_ in range(bottom_idx, -1, -1):
            board[row_][col] = 0


    return board

board = [
[1, 3, 5, 5, 2], 
[3, 4, 3, 3, 1], 
[3, 2, 4, 5, 2], 
[2, 4, 4, 5, 5], 
[1, 4, 4, 1, 1]
]

tracker = [
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], 
[0, 0, 1, 1, 0], 
[0, 1, 1, 1, 1], 
[0, 1, 1, 0, 0]]

expected_output = [
[1, 0, 0, 0, 0], 
[3, 0, 0, 0, 2], 
[3, 3, 0, 5, 1], 
[2, 4, 5, 3, 2], 
[1, 2, 3, 1, 1]]

[[1, 3, 5, 5, 2], 
 [3, 4, 3, 3, 1], 
 [3, 2, 4, 5, 2], 
 [2, 0, 0, 5, 5], 
 [1, 0, 0, 1, 1]]

print(crush_only(board, tracker) == expected_output)

# board1 = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
# expected1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

# print(Solution().candyCrush(board1) == expected1)

# board2 = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
# expected2 = [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]

# print(Solution().candyCrush(board2) == expected2)
