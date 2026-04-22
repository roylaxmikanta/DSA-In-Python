import math
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=num
        my_set=set()
        while(n>0):
            ld=n%10
            my_set.add(ld)
            n=n//10
        count=0
        for i in range(1, int(math.sqrt(num))+1):
            if num%i==0 and i in my_set:
                count+=1
                if i!=num//i and num//i in my_set:
                    count+=1
        return count
s=Solution()
print(s.countDigits(121)) 