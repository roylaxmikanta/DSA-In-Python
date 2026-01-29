class Solution:
    def jump(self, nums):
        jum=0
        left=0
        right=0
        while(right<len(nums)-1):
            fearthest=0
            for i in range(left,right+1):
                fearthest=max(fearthest,i+nums[i])
            left=right+1
            jum+=1
            right=fearthest
        return jum
s=Solution()
print(s.jump([2,3,1,4,1,1,1,2]))







#time complexity : O(N)
#space complexity : O(1)