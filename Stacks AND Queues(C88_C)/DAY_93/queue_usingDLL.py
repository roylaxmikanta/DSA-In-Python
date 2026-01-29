class QueueUsingDLL:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        temp = self.front
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    def rear(self):
        if self.is_empty():
            raise IndexError("Rear from empty queue")
        return self.rear.data