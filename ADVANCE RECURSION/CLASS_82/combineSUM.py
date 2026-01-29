# class Solution:
#     def CombinationSum(self,index,total,sub,target,nums,answer):
#         if(total==target):
#             answer.append(sub.copy())
#             return
#         if(index>=len(nums)):
#             return
#         if total>target:
#             return
#         sub.append(nums[index])
#         curr_sum=total+nums[index]
#         self.CombinationSum(index,curr_sum,sub,target,nums,answer)
#         sub.pop()
#         self.CombinationSum(index+1,total,sub,target,nums,answer)
#         return answer
# s=Solution()
# nums=[2,3,6,7]
# answer=[]
# print(s.CombinationSum(0,0,[], 7,nums,answer))



# class Solution:
#     def combineSUM(self, index, total, sub, target, nums, answer):
#         if total == target:
#             answer.append(sub.copy())
#             return
#         if index >= len(nums):
#             return
#         if total > target:
#             return
#         sub.append(nums[index])
#         curr_sum = total + nums[index]
#         self.combineSUM(index, curr_sum, sub, target, nums, answer)
#         sub.pop()
#         self.combineSUM(index + 1, total, sub, target, nums, answer)
#         return answer
# s = Solution()
# nums = [2, 3, 6, 7]
# answer = []
# print(s.combineSUM(0, 0, [], 7, nums, answer))



class Solution:
    def combinationSum2(self, candidates, target):
        answer = []
        candidates.sort()
        self.solve(0, target, [], candidates, answer)
        return answer
    def solve(self, index, target, sub, nums, answer):
        if target == 0:
            answer.append(list(sub))
            return
        if target < 0:
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            sub.append(nums[i])
            self.solve(i + 1, target - nums[i], sub, nums, answer)
            sub.pop()
s=Solution()
nums=[10,1,2,7,6,1,5]
print(s.combinationSum2(nums,8))