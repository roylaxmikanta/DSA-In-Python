class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        answer=0
        # for i in range(n):
        #     nums = [nums[-1]] + nums[:-1]
        #     total=0
        #     for i in range(0,n):
        #         total=total+i*nums[i]
        #     answer=max(answer,total)
        # return answer
        total_sum = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        max_value = F
        for i in range(n - 1, 0, -1):
            F = F + total_sum - n * nums[i]
            max_value = max(max_value, F)
        return max_value
s=Solution()
print(s.maxRotateFunction([4,3,2,6]))






# arr = [1, 2, 3, 4, 5]
# n = len(arr)
# for i in range(n):
#     arr = [arr[-1]] + arr[:-1]   # rotate right by 1
#     print(arr)