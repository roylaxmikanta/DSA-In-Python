class Solution:
    def isHappy(self, n):
        my_set=set()
        new=n
        while(new!=1):
            total=0
            while(new>0):
                ld=new%10
                total+=(ld*ld)
                new=new//10
            if(total in my_set):
                return False
            my_set.add(total)
            new=total
        return True
s=Solution()
print(s.isHappy(19))
