#count primes less than n
class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        count=0
        for i in range(2, n):
            for j in range(2,i):
                if i % j == 0:
                    break
                else:
                    count += 1
                    break
        return count    
s = Solution()
print(s.countPrimes(10))
            