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
    def infixToPostfix(self, exp):
        stack = []
        result = ''
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
                while (stack and self.precedence(ch) <= self.precedence(stack[-1])):
                    result += stack.pop()
                stack.append(ch)
        while stack:
            result += stack.pop()
        return result
s = Solution()
k = s.infixToPostfix("A*(B^C)/D")
print(k)

#time complexity: O(n)+O(n)=O(n)
#space complexity: O(n)+O(n)