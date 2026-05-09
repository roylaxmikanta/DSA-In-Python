#3. Conversion of Infix operation to Postfix operation in Stack using Linked List and Arrays

class Solution:
    def precedence(self, ch):
        if ch == '+' or ch == '-':
            return 1
        elif ch == '*' or ch == '/':
            return 2
        elif ch == '^':
            return 3
        return 0
    def infix_to_postfix(self, exp):
        stack = []
        result = ""
        for ch in exp:
            if ch.isalnum():
                result += ch
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            else:
                while (stack and
                       self.precedence(stack[-1]) >= self.precedence(ch)):
                    result += stack.pop()
                stack.append(ch)
        while stack:
            result += stack.pop()
        return result
exp = "A+B*(C-D)"
s = Solution()
print(s.infix_to_postfix(exp))