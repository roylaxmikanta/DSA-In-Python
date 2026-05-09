#6. Implementation of Greedy method for TSP problem in Branch-Bound method

class Solution:
    def tsp(self, graph):
        n = len(graph)
        visited = [False] * n
        visited[0] = True
        path = [0]
        cost = 0
        current = 0
        for _ in range(n - 1):
            min_cost = float('inf')
            next_city = -1
            for city in range(n):
                if not visited[city] and graph[current][city] < min_cost:
                    min_cost = graph[current][city]
                    next_city = city
            visited[next_city] = True
            path.append(next_city)
            cost += min_cost
            current = next_city
        cost += graph[current][0]
        path.append(0)
        print("Path:", path)
        print("Cost:", cost)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
s = Solution()
s.tsp(graph)