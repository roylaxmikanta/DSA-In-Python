class Solution:
    def solve(self,index,total,brackets,result):
        if(index>=len(brackets)):
            if(total==0):
                result.append("".join(brackets))
            return
        if(total>len(brackets)//2):
            return
        if(total<0):
            return
        brackets[index]="("
        sum=total+1
        self.solve(index+1,sum,brackets,result)
        brackets[index]=")"
        sum=total-1
        self.solve(index+1,sum,brackets,result)
        # return result
    
    def generateBinary(self, n):
        numbers = [""] * (2*n)
        result = []
        self.solve(0, 0, numbers, result)
        return result


# numbers=["0"]*3
# result=[]
s=Solution()
# print(s.solve(0, True, numbers, result))
print(s.generateBinary(12))