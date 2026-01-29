class StackUsingDLL:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.prev = self.top
            self.top.next = new_node
            self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.prev
        if self.top:
            self.top.next = None
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev
        return elements[::-1]  # Return in stack order (bottom to top)