class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)==1):
            return nums
        result=[]
        self.backTrack(0,nums,result)
        return result
    def backTrack(self,start,nums,result):
        n=len(nums)
        if(start==n):
            result.append(nums[:])
        for i in range(start,n):
            nums[i],nums[start]=nums[start],nums[i]
            self.backTrack(start+1,nums,result)
            nums[i],nums[start]=nums[start],nums[i]

s=Solution()
print(s.permute([1,2,3]))