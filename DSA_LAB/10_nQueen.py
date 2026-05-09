#10. Implementation of n-Queen’s problem using Backtracking approach

class Solution:
    def solve(self,col,broad,answer,leftrow,upperDiagonal,lowerDiagonal,n):
        if(col==n):
            answer.append(broad[:])
            return
        for row in range(n):
            if(leftrow[row]==0 and lowerDiagonal[row+col]==0 and upperDiagonal[n-1+col - row]==0):
                broad[row]=broad[row][:col]+"Q"+broad[row][col+1:]
                leftrow[row]=1
                lowerDiagonal[row+col]=1
                upperDiagonal[n-1+col - row]=1
                self.solve(col+1,broad,answer,leftrow,upperDiagonal,lowerDiagonal,n)
                broad[row]=broad[row][:col]+"."+broad[row][col+1:]
                leftrow[row]=0
                lowerDiagonal[row+col]=0
                upperDiagonal[n-1+col - row]=0
        
    def solveNQueens(self,n):
        answer=[]
        broad=["."*n for _ in range(n)]
        leftrow=[0]*n
        upperDiagonal=[0]*(2*n-1)
        lowerDiagonal=[0]*(2*n-1)
        self.solve(0,broad, answer,leftrow,upperDiagonal,lowerDiagonal,n)
        return answer
s=Solution()    
print(s.solveNQueens(4) )