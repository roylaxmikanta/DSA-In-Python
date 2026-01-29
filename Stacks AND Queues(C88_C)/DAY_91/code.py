from collections import deque
class stackUsingDeque:
    def __init__(self):
        self.container=deque()
        self.queue=self.container
    def push(self,val):
        self.queue.append(val)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        else:
            return "Stack is empty"
    
    def top(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return "Stack is empty"
    def pick(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return "Stack is empty"
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
# Example usage:
stack=stackUsingDeque()
stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.size())
print(stack.top())
