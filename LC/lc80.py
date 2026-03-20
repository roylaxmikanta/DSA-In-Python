class Solution:
    def removeDuplicates(self, nums):
        # i=2
        # place=2
        # while(i<len(nums) and place<len(nums)):
        #     if(nums[i-2]!=nums[i]):
        #         nums[place]=nums[i]
        #         place+=1
        #     i+=1
        # return place

        # # i=0
        # # for j in range(len(nums)):
        # #     if(i<2 or nums[j]!=nums[i-2]):
        # #         nums[i]=nums[j]
        # #         i+=1
        # # return i

s=Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))