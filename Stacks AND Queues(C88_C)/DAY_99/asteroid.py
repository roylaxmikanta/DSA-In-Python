class Solution:
    def asteroidCollision(self, nums):
        stack=[]
        n=len(nums)
        for i in range(0,n):
            if(nums[i]>0): 
                stack.append(nums[i])
            else:
                while(len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(nums[i])):
                    stack.pop()
                if(len(stack)!=0 and stack[-1]==abs(nums[i])):
                    stack.pop()
                elif(len(stack)==0 or stack[-1]<0):
                    stack.append(nums[i])
        return stack
s=Solution()
print(s.asteroidCollision([4,7,1,1,2,-3,-7,17,15,-16]))



#time complexity : O(2N)
#space complexity : O(N)