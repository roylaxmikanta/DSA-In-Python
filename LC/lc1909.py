class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0 
        for i in range(1,len(nums)-1):
            if(nums[i]<=nums[i-1]):
                count+=1
                if(nums[i]<=nums[i-2] and nums[i+1]<=nums[i-1]):
                    return False
        if(count>1):
            return False
        return True
s=Solution()
print(s.canBeIncreasing([1,1,2]))