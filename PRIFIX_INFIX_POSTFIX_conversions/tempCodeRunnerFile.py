class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        write_index = 0
        i = 0
        while i < n:
            nums[write_index] = nums[i]
            write_index += 1
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            i = j
        return write_index
s = Solution()
k = s.removeDuplicates([1,1,2])
print(k)