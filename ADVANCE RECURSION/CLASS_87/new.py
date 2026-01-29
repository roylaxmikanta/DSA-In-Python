class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]
        
        if maze[0][0] == 1:
            self.findPathHelper(0, 0, maze, n, ans, "", vis)
        
        return ans

    def findPathHelper(self, i, j, a, n, ans, move, vis):
        # Base case: reached destination
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return

        # Mark current cell as visited
        vis[i][j] = 1

        # Down
        if i + 1 < n and not vis[i+1][j] and a[i+1][j] == 1:
            self.findPathHelper(i + 1, j, a, n, ans, move + "D", vis)

        # Left
        if j - 1 >= 0 and not vis[i][j-1] and a[i][j-1] == 1:
            self.findPathHelper(i, j - 1, a, n, ans, move + "L", vis)

        # Right
        if j + 1 < n and not vis[i][j+1] and a[i][j+1] == 1:
            self.findPathHelper(i, j + 1, a, n, ans, move + "R", vis)

        # Up
        if i - 1 >= 0 and not vis[i-1][j] and a[i-1][j] == 1:
            self.findPathHelper(i - 1, j, a, n, ans, move + "U", vis)

        # Backtrack
        vis[i][j] = 0
s = Solution()
result = s.ratInMaze([
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0], 
    [0, 1, 1, 1]
])
print("[" + ", ".join(result) + "]")