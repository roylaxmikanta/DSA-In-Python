#1  Traverse

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        self. prev = None
class DubkyLinkedList():
    def __init__(self):
        self.head = None
    def traverse(self,head):
        if head is None:
            return " list is empty"
        else:
            temp = head
            while temp is not None:
                print(temp.val, end = "   ")
                temp=temp.next
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4

dll = DubkyLinkedList()
dll.traverse(n1)