class Solution:
    def removeElement(self, nums, val):
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
s = Solution()
k = s.removeElement([3,2,2,3], 3)
print(k)
