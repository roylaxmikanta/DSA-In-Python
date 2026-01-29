class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False               
        while n%3==0:
            n /= 3
            if(n==1):
                return True
        return n==1
s = Solution()
print(s.isPowerOfThree(45))