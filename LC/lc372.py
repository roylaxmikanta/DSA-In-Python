#Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if(a==0):
            return 0
        if(a==1):
            return 1
        if(a%1337==0):
            return 0
        if(a%1337==1):
            return 1
        a=a%1337
        result=1
        for i in range(0,len(b)):
            result=(result*pow(a,b[i],1337))%1337
            a=pow(a,10,1337)
        return result