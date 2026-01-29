class Solution(object):
    def maxScore(self, nums, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        if(k==n):
            return sum(nums)
        if(k>n):
            return "This is not possible"
        left_sum=0
        for i in range(0,k):
            left_sum+=nums[i]
        maxi=left_sum
        right_ind=n-1
        right_sum=0
        for i in range(k-1,-1,-1):
            left_sum-=nums[i]
            right_sum+=nums[right_ind]
            maxi=max(maxi,right_sum+left_sum)
            right_ind-=1
        return maxi             
s=Solution()
print(s.maxScore([1,2,3,4,5,6,1],3))

#time complexity : O(N)+O(N)
#space complexity : O(1)


#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/