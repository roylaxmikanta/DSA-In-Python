# class Solution(object):
#     def subarraySum(self, nums, k):
#         n=len(nums)
#         left=0
#         right=0
#         sumi=0
#         count=0
#         while(left<n and right<n):
#             if(sumi<=k):
#                 sumi+=nums[right]
#                 if(sumi==k):
#                     count+=1
#                 right+=1
#             else:
#                 sumi-=nums[left]
#                 left+=1
#         return count

class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        sum_so_far=0
        sum_dict={0:1}
        for num in nums:
            sum_so_far+=num
            if sum_so_far-k in sum_dict:
                count+=sum_dict[sum_so_far-k]
            if sum_so_far in sum_dict:
                sum_dict[sum_so_far]+=1
            else:
                sum_dict[sum_so_far]=1
        return count

s=Solution()
print(s.subarraySum([1,2,3],3))