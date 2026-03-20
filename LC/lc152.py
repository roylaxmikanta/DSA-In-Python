class Solution:
    def maxProduct(self, nums):
        maxi=float("-inf")
        product=nums[0]
        i=1
        while(i<len(nums)):
            product=product*nums[i]
            maxi=max(maxi,product)
            if(nums[i]==0):
                product=1
                maxi=max(maxi,0)
            # print(maxi)
            if(i==len(nums)-1):
                j=0
                while(j<=i):
                    if(nums[j]!=0):
                        product=product//nums[j]
                    maxi=max(maxi,product,nums[j])
                    j+=1
            i+=1
        return maxi
s=Solution()
print(s.maxProduct([1,0,-1,2,3,-5,-2]))