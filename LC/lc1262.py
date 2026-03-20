class Solution(object):
    def maxSumDivThree(self, nums):
        total=sum(nums)
        if(total%3==0):
            return total
        nums=sorted(nums)
        current=total
        for num in nums:
            current=current-num
            if(current%3==0):
                return current
        
s=Solution()
print(s.maxSumDivThree([3,6,5,1,8]))