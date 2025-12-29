#append at the last
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        self. prev = None

class DubkyLinkedList():
    def __init__(self):
        self.head = None
    def append_last(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            
dll = DubkyLinkedList()
dll.append_last(100)


#time complaxity : O(N)
#space complaxity : O(1)