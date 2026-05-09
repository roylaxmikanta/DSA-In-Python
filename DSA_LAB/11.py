#11. Implementation of Hashing with Linear Probing
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size
    # insert function
    def insert(self, key):
        index = key % self.size
        while self.table[index] != -1:
            index = (index + 1) % self.size
        self.table[index] = key
    # displayn function
    def display(self):
        for i in range(self.size):
            print(i, "->", self.table[i])
# driver Code
h = HashTable(10)
h.insert(25)
h.insert(35)
h.insert(15)
h.insert(45)
h.display()