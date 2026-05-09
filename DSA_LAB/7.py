# 7. Implementation of Fractional Knapsack problem using Greedy approach

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
def fractional_knapsack(capacity, items):
    # Sort items by value/weight ratio
    items.sort(key=lambda item: item.value / item.weight,
            reverse=True)
    total_profit = 0
    for item in items:
        if item.weight <= capacity:
            capacity = capacity - item.weight
            total_profit = total_profit + item.value
        else:
            fraction = capacity / item.weight
            total_profit = total_profit + (item.value * fraction)
            break
    return total_profit
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]
capacity = 50
answer = fractional_knapsack(capacity, items)
print("Maximum Profit =", answer)