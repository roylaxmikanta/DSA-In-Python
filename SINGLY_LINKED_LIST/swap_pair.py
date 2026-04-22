class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if(head is None or head.next is None):
            return head
        slow=head
        fast=head.next
        dummy=ListNode(0)
        curr=dummy
        while(fast is not None and fast.next is not None):
            curr.next=fast
            curr=curr.next
            curr.next=slow
            curr=curr.next
            fast=fast.next.next
            slow.next=fast
        return dummy.next
s=Solution()
head=ListNode(1)
head.next=ListNode(2)  
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
result=s.swapPairs(head)
print(result.val)