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
    def __init__(self, board):
        self.original_board = board
        self.n_rows = len(board)
        self.n_cols = len(board[0])

    def isStable(self, board):
        """ """

    def is_same(self, board, row, col, v, seen):
        # first check bounds 
        if row < 0 or row >= len(board):
            return
        if col < 0 or col >= len(board[0]):
            return
        
        # then sameness
        if board[row][col] == v:
            # keep iterating? 
            # seen[row][col] = 
        # if true update seen
        return

    def find_candy_strings(self, board, row, col, seen):
        if len(board) == 0:
            return
        if row < 0 or row >= len(board):
            return
        if col < 0 or col >= len(board[0]):
            return
        if seen[row][col] < 0:
            return
    
        # check all four directions for sameness 
        curr_val = board[row][col]
        self.is_same(board, row+1, col, curr_val, seen)
        self.is_same(board, row-1, col, curr_val, seen)
        self.is_same(board, row, col+1, curr_val, seen)
        self.is_same(board, row, col-1, curr_val, seen)
        
        if board[row][col]:
            
            

        return stable, board 
    
    def candyCrush(self, board):
        seen =  board # [[False]*self.n_cols for row in range(self.n_rows)]
        result = board

        stable = False
        # 1. find all candy strings 
        while True:
            stable, result = self.find_candy_strings(board, seen, result)
            # 2. crush all candy strings 
            if stable:
                return
            self.crush(result, seen)
            board = result
            
    def crush(self, matrix, seen):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        


        # crush by column! 

        # for row in matrix:




    # make a seen matrix 
    # 

board1 = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
expected1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

print(Solution().candyCrush(board1) == expected1)

# board2 = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
# expected2 = [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]

# print(Solution().candyCrush(board2) == expected2)
