class Solution:
    def solveNQueens(self, n):
        answer=[]
        broad=["."* n for _ in range(n)]
        self.solve(0,broad,answer,n)
        return answer
    def isSafe(self,row,col,board,n):
        duprow=row
        dupcol=col
        while(row>=0 and col>=0):
            if(board[row][col]=="Q"):
                return False
            row-=1
            col-=1

        row=duprow
        col=dupcol
        while(col>=0):
            if(board[row][col]=="Q"):
                return False
            col-=1
        
        row=duprow
        col=dupcol
        while(col>=0 and row<n):
            if(board[row][col]=="Q"):
                return False
            row+=1
            col-=1
        return True
    def solve(self,col,broad,answer,n):
        if(col==n):
            answer.append(list(broad))
            return
        for row in range(n):
            if(self.isSafe(row,col,broad,n)):
                broad[row]=broad[row][:col]+"Q"+broad[row][col+1:]
                self.solve(col+1,broad,answer,n)
                broad[row]=broad[row][:col]+"."+broad[row][col+1:]

s=Solution()
print(s.solveNQueens(4))  

#time complaxity : O(n! *n)
#space complaxity :O(n^2)


