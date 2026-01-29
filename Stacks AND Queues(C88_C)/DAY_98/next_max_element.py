class Solution:
    def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(2*n-1,-1,-1):
            while(len(stack)!=0 and stack[-1]<=nums[i%n]):
                stack.pop()
            if(i<n):
                if(len(stack)!=0):
                    ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans
    
s=Solution()
print(s.nextGreaterElements([1,2,3,4,3]))


#time complexity : O(2n)
#space complexity : O(n)