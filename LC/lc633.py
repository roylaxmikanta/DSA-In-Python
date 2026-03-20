# class Solution(object):
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#         n=int(c**(0.5))
#         for i in range(1,n):
#             for j in range(1,n):
#                 if(i**2+j**2==c):
#                     return True
#         return False
# s=Solution()
# print(s.judgeSquareSum(25))







#optimal solution
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left=0
        right=int(c**(0.5))
        while(left<=right):
            current=left**2+right**2
            if(current==c):
                return True
            elif(current<c):
                left+=1
            else:
                right-=1
        return False     
s=Solution()
print(s.judgeSquareSum(25))