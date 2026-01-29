class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next   
        return head
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def print_list(node):
    while node:
        print(node.val, end="--")
        node = node.next
    print("None")   
s = Solution()
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
new_head = s.deleteDuplicates(head)
print_list(new_head)