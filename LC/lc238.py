class Solution:
    def productExceptSelf(self, nums):
        left=[1]
        sumi=1
        for i in range(1,len(nums)):
            sumi=sumi*nums[i-1]
            left.append(sumi)
        right=[1]
        sumi=1
        for i in range(len(nums)-2,-1,-1):
            sumi=sumi*nums[i+1]
            right.append(sumi)
        right=right[::-1]
        answer=[]
        for i in range(0,len(right)):
            answer.append((right[i])*(left[i]))
        return answer