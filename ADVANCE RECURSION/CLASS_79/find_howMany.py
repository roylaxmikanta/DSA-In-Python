class Solution:
    def solve(self,index,tf,numbers,result):
        if(index>=len(numbers)):
            result.append("".join(numbers)) #for joining three number of strings
            return
        numbers[index]="0"
        self.solve(index+1,True,numbers,result)
        if(tf==True):
            numbers[index]="1"
            self.solve(index+1,False,numbers,result)
            numbers[index]="0"
        # return result
    
    def generateBinary(self, n):
        numbers = ["0"] * n
        result = []
        self.solve(0, True, numbers, result)
        return result


# numbers=["0"]*3
# result=[]
s=Solution()
# print(s.solve(0, True, numbers, result))
print(s.generateBinary(4))