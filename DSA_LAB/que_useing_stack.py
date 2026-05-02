class myQueue:

    def __init__(self):
        # Initialize your data members
        self.items = []
        

    def enqueue(self, x):
        # Implement the enqueue operation
        self.items.append(x)
        
    def dequeue(self):
        # Implement the dequeue operation
        return self.items.pop(0)

    def front(self):
        # Return the front element of the queue
        return self.items[0]

    def size(self):
        # Return the current size of the queue
        return len(self.items)