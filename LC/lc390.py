class Solution(object):
    def lastRemaining(self, n):
        head = 1
        step = 1
        remaining = n
        left = True 
        while remaining > 1:
            if left or remaining % 2 == 1:    #have to write this line because for this conditon apply when, we have to remove first(head) element
                head += step    
            remaining //= 2
            step *= 2
            left = not left
        return head
s = Solution()
print(s.lastRemaining(9))  