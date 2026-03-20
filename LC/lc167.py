class Solution:
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while(left<right):
            total=numbers[left]+numbers[right]
            if(total==target):
                return [left+1,right+1]
            elif(total<target):
                left+=1
            else:
                right+=1
s=Solution()
print(s.twoSum([2,3,4],6))