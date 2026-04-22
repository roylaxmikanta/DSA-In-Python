class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<2):
            return 0
        count=0
        for i in range(2,n):
            is_prime=True
            for j in range(2,int(i**0.5)+1):
                if(i%j==0):
                    is_prime=False
                    break
            if(is_prime):
                count+=1
        return count
s=Solution()
print(s.countPrimes(10))