#5. Implementation of DFS using Stack for n-Queen’s problem in Backtracking

class Solution:
    def is_safe(self, board, row, col, n):
        for i in range(col):
            if board[row][i] == 1:
                return False
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        i = row
        j = col
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True
    def solve(self, board, col, n):
        if col >= n:
            for row in board:
                print(row)
            print()
            return
        for i in range(n):
            if self.is_safe(board, i, col, n):
                board[i][col] = 1
                self.solve(board, col + 1, n)
                board[i][col] = 0
n = 4
board = [[0]*n for _ in range(n)]
s = Solution()
s.solve(board, 0, n)