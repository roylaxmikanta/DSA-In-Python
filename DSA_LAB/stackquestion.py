class TwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    # Function to push an integer into stack 1
    def push1(self, x):
        # code here
        self.stack1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        # code here
        self.stack2.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        # code here
        if self.stack1:
            return self.stack1.pop()
        return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        # code here
        if self.stack2:
            return self.stack2.pop()
        return -1