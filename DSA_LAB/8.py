# 8. Implementation of 0/1 Knapsack problem using Dynamic approach

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                take = values[i - 1] + \
                       dp[i - 1][w - weights[i - 1]]
                not_take = dp[i - 1][w]
                dp[i][w] = max(take, not_take)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8
answer = knapsack(weights, values, capacity)
print("Maximum Profit =", answer)