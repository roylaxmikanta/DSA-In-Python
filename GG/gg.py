class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        window_xor = 0
        for i in range(k):
            window_xor ^= arr[i]
        max_xor = window_xor
        for i in range(k, n):
            window_xor ^= arr[i - k]
            window_xor ^= arr[i] 
            max_xor = max(max_xor, window_xor)
        
        return max_xor
s = Solution()
arr = [1, 2, 3, 4, 5]
k = 3
print(s.maxSubarrayXOR(arr, k))