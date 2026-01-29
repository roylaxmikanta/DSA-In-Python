class Solution:
    def canJump(self, nums):
        max_index=0
        for i in range(0,len(nums)):
            if(i>max_index):
                return False
            max_index=max(max_index,i+nums[i])
        return True
s=Solution()
print(s.canJump([3,2,1,2,1,5]))