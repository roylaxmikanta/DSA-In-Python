class Solution:
    def majorityElement(self, nums):
        nums=sorted(nums)
        # return nums
        max_count=0
        max_count_element=nums[0]
        i=0
        while(i<len(nums)):
            count=1
            while(i<len(nums)-1 and nums[i]==nums[i+1]):
                count+=1
                i+=1
            if(count>max_count):
                max_count=count
                max_count_element=nums[i]
            i+=1
        return max_count_element
s=Solution()
print(s.majorityElement([10,9,9,9,10]))