class Solution(object):
    def solve(self, board):
        if(len(board)<2 or len(board[0])<2):
            return board
        row=len(board)
        col=len(board[0])
        for i in range(0,row):
            for j in range(0,col):
                if((i!=0 and i!=row-1 and board[i][j]=="O" and j!=0 and j!=row-1 and board[i][j]=="O")):
                    board[i][j]="X"
        return board

s=Solution()
print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))


#not solved