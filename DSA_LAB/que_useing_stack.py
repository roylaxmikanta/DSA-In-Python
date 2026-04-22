class myQueue:

    def __init__(self):
        # Initialize your data members
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        # Implement the enqueue operation
        self.stack1.append(x)

    def dequeue(self):
        # Implement the dequeue operation
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def front(self):
        # Return the front element of the queue
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def size(self):
        # Return the current size of the queue
        return len(self.stack1) + len(self.stack2)