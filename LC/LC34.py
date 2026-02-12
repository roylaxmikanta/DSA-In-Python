class Solution:
    def searchRange(self, nums,target):
        high=len(nums)-1
        low=0
        result=[]
        left=True
        right=True
        while(low<=high and len(result)!=2):
            if(nums[low]==target and left==True):
                result.append(low)
                left=False
            if(nums[low]!=target and left==True):
                low+=1
            if(nums[high]==target and right==True):
                result.append(high)
                right=False
            if(nums[high]!=target and right==True):
                high-=1
        if(len(result)==0):
            return [-1,-1]
        elif(len(result)==1):
            result.append(result[0])
        return sorted(result)
s=Solution()
print(s.searchRange([5,7,7,8,8,10],8))