class StackQueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    def is_empty(self):
        return not self.st1

    def push(self,x):                               #time complexity:O(N+N=2N)
        while(self.st1):                        
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while(self.st2):
            self.st1.append(self.st2.pop())
        return self.st1
    def pop(self):                                  #time complexity:O(1)
        if(not self.st1):
            return "it is empty"
        else:
            return self.st1.pop()
    def peek(self):                                 #time complexity:O(1)
        if(not self.st1):
            print("It is empty")
            return
        return self.st1[-1]
