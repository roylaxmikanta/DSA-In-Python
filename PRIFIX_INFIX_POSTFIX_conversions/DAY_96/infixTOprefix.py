class Solution:
    def precedence(self, ch):
        if ch == '+' or ch == '-':
            return 1
        elif ch == '*' or ch == '/':
            return 2
        elif ch == '^':
            return 3
        else:
            return 0
    def infixToPrefix(self, exp):
        # Reverse the expression
        exp = exp[::-1]
        # Replace ( with ) and vice versa
        exp=exp.replace('(','temp').replace(')','(').replace('temp',')')
        stack = []
        result =[]
        for ch in exp:
            if("a"<=ch<="z" or "A"<=ch<="Z" or "0"<=ch<="9"):
                result.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while (stack and self.precedence(ch) < self.precedence(stack[-1])):   #this is the only change from postfix to prefix
                    result.append(stack.pop())
                stack.append(ch)
        while stack:
            result.append(stack.pop())
        # Reverse result to get prefix
        return ''.join(result[::-1])
s= Solution()
k= s.infixToPrefix("A*(B^C)/D")
print(k)

#time complexity: O(6n) ~ O(n)
#space complexity: O(n)+O(n)