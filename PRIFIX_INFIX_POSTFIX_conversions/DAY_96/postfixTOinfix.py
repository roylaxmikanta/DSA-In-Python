class Solution:
    def PostfixToInfix(self, exp):
        stack = []
        for ch in exp:
            if("a"<=ch<="z" or "A"<=ch<="Z" or "0"<=ch<="9"):
            # if ch.isalnum():
                stack.append(ch)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                new_expr = '(' + op1 + ch + op2 + ')'
                stack.append(new_expr)
        return stack[0]
s = Solution()
k = s.PostfixToInfix("ABC^*D/") 
print(k)

#time complexity: O(n)
#space complexity: O(n)