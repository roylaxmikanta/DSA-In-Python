#1. Implementation of binary search method in Divide and Conquer Approach

class Solution:
    def binary_search(self, arr, low, high, target):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.binary_search(arr, low, mid - 1, target)
        else:
            return self.binary_search(arr, mid + 1, high, target)
# Driver Code
arr = [10, 20, 30, 40, 50, 60]
s = Solution()
print(s.binary_search(arr, 0, len(arr)-1, 40))