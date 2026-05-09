#4. Implementation of Queue in BFS traversal for TSP problem in Branch-Bound method

from collections import deque
class Solution:
    def bfs(self, graph, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
s = Solution()
s.bfs(graph, 0)