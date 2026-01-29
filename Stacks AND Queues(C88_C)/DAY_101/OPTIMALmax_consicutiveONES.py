class Solution:
    def longestOnes(self, nums,k):
        maxi=0
        zeros=0
        n=len(nums)
        left=0
        right=0
        while(right<n):
            if(nums[right]==0):
                zeros+=1
            if(zeros>k):
                if(nums[left]==0):
                    zeros-=1
                left+=1
            if(zeros<=k):
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi
nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
s=Solution()
print(s.longestOnes(nums,k))








#LC ---> 1004
#time complexity : O(N)
#space complexity : O(1)