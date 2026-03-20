class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        result = set(nums[0])
        for i in range(1, len(nums)):
            result.intersection_update(nums[i])
        return list(result)
s=Solution()
print(s.intersection([[1,2,3],[3,4,5,6],[3,7,8,9]]))