# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def __init__(self):
        self.head = None
    def deleteNode(self, val):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr=self.head
        if curr is None:
            return "List is empty"
        if(curr.next is not None):
            if(curr.val==val):
                self.head=curr.next
                return
            found=False
            while(curr is not None):
                if(curr.val==val):
                    found=True
                    break
                privious=curr
                curr=curr.next
            if(found==True):
                privious.next=curr.next
                del curr
            else :
                return "Node not found"

#here itrate elements
    def traversal(self):
        if (self.head is None):
            print("singly link list is empty ")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end='\t')
                curr=curr.next
    #return result
n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)
n1.next=n2
n2.next=n3
n3.next=n4
s=Solution()
s.head=n1
print(s.deleteNode(2))        
s.traversal()