#insert kth index
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        self. prev = None
class DubkyLinkedList():
    def __init__(self):
        self.head = None
    def insert_kth(self,val,position):
        new_node = Node(val)
        if(position == 0):
            self.insert_1st(val)
            return
        temp = self.head
        count = 0
        while temp is not None and count<position-1:
            temp = temp.next
            count += 1
        if temp is not None:
            return " position out of  boundary"
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
#time complexity : O(N)
#space complaxity : (N)