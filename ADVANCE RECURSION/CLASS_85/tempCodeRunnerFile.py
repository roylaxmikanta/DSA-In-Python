class Solution:
    
    def exist(self, index, digits, subset):
        if index >= len(digits):
            self.result.append("".join(subset))
            return 

        for ch in self.char_map[digits[index]]:
            subset.append(ch)
            self.exist(index + 1, digits, subset)
            subset.pop()
    def solve(self, digits):
        self.char_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        self.result = []
        self.exist(0, digits, [])
        return self.result

s = Solution()
print(s.solve("46"))