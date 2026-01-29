class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue.size())
print(queue.front())
queue.dequeue()
queue.dequeue()
print(queue.front())
print(queue.rear())
print(queue.is_empty())