# class Solution:
#     def search(self, nums,target):
#         low=0
#         high=len(nums)-1
#         self.inSearch(nums,target,low,high)
#     def inSearch(nums,target,low,high):
#         mid=(low+high)//2
#         if(low > high): 
#             return -1
#         if(nums[mid]==target):
#             return mid
#         if(nums[mid]>target and nums[-1]<target):
#             inSearch(nums,target,low,mid-1)
#         elif(nums[mid]<target and nums[0]>target):
#             self.inSearch(nums,target,low,mid-1)
#         else:
#             self.inSearch(nums,target,mid+1,high)
#         return mid


# s=Solution()
# print(s.search([4,5,6,7,0,1,2],0))