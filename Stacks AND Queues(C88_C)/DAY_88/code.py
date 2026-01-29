class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("top from empty stack")
    def size(self):
        return len(self.stack)
# Example usage:
stack = Stack()   
stack.push(10)
stack.push(20) 
print(stack.pop())
print(stack.size())
print(stack.top())
