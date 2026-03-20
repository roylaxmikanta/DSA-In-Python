#how to store real part and complex values in different variable of two complex numbers
# class Solution(object):
#     def complexNumberMultiply(self, num1, num2):
#         # real1=0
#         # real2=0
#         # complex1=0
#         # complex2=0
#         for i in range(0,len(num1)):
#             if(num1[i]=="+"):
#                 real1=int(num1[0:i])
#                 complex1=int(num1[i+1:len(num1)-1])
#                 break
#         for i in range(0,len(num2)):
#             if(num2[i]=="+"):
#                 real2=int(num2[0:i])
#                 complex2=int(num2[i+1:len(num2)-1])
#                 break
#         real=(real1*real2)-(complex1*complex2)
#         complex=(real1*complex2)+(real2*complex1)
#         return str(real)+"+"+str(complex)+"i"







#own
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        for i in range(0,len(num1)):
            if(num1[i]=="+"):
                real1=int(num1[:i])
                complex1=int(num1[i+1:len(num1)-1])
        for i in range(0,len(num2)):
            if(num2[i]=="+"):
                real2=int(num2[:i])
                complex2=int(num2[i+1:len(num2)-1])
        real=real1*real2 - complex1*complex2
        comp=real1*complex2 + real2*complex1
        return str(real)+"+"+str(comp)+"i"
s=Solution()
print(s.complexNumberMultiply("1+1i","1+1i"))