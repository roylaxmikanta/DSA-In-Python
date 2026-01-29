class Solution:
    def prefixTOinfix(self, exp):
        stack = []
        # Reverse the prefix expression
        exp = exp[::-1]
        for ch in exp:
            if("a"<=ch<="z" or "A"<=ch<="Z" or "0"<=ch<="9"):
                stack.append(ch)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                new_expr = '(' + op1 + ch + op2 + ')'
                stack.append(new_expr)
        return stack[0]
s = Solution()
k = s.prefixTOinfix("/*A^BCD")  
print(k)


#time complexity: O(n)
#space complexity: O(n)