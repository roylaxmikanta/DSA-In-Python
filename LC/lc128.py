class Solution:
    def longestConsecutive(self, nums):
        nums = sorted(set(nums))
        count=1
        max_count=0
        # return nums
        for i in range(0,len(nums)-1):
            if(nums[i]==(nums[i+1]-1)):
                count+=1
            else:
                count=1
            max_count=max(max_count,count)
        return max_count
s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))