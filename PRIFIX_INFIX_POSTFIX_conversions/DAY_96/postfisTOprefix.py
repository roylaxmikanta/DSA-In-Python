class Solution:
    def PostfixToPrefix(self, exp):
        stack = []
        for ch in exp:
            if("a"<=ch<="z" or "A"<=ch<="Z" or "0"<=ch<="9"):
                stack.append(ch)
            else:   
                op2 = stack.pop()
                op1 = stack.pop()
                new_expr = ch + op1 + op2
                stack.append(new_expr)  
        return stack[0]
s = Solution()  
k = s.PostfixToPrefix("ABC^*D/")
print(k)


#time complexity: O(n)
#space complexity: O(n)