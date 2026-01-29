# 203. Remove Linked List Elements leedcode problem
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if head is None:
#             return None
#         head.next = self.removeElements(head.next, val)
#         return head.next if head.val == val else head
# # LEET CODE SOLUTION


# class Solution:
#     class Node():
#         def __init__(self,val):
#             self.val = val
#             self.next = None
#     def removeElements(self, head, val):
#         if head is None:
#             return None
#         head.next = self.removeElements(head.next, val)  
#         if head.val == val:
#             return head.next  
#         else:
#             return head      
# s = Solution()
# nodeA = Node(1)
# nodeB = Node(2)
# nodeC = Node(3)
# nodeD = Node(4)
# nodeA.next = nodeB
# nodeB.next = nodeC
# nodeC.next = nodeD
# nodeD.next = nodeB
# print(s.removeElements(nodeA, 2))


#i need solution for this problem of leedcode question no 203
# LEET CODE SOLUTION
class Solution:
    class Node():
        def __init__(self,val):
            self.val = val
            self.next = None
    def removeElements(self, head, val):
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)  
        if head.val == val:
            return head.next  
        else:
            return head
s = Solution()  
nodeA = Solution.Node(1)
nodeB = Solution.Node(2)    
nodeC = Solution.Node(3)
nodeD = Solution.Node(4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None
print(s.removeElements(nodeA, 2))