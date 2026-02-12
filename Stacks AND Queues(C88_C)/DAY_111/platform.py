# class Solution:    
#     def minPlatform(self, arr, dep):
#         ans=1
#         for i in range(0,len(arr)):
#             count=1
#             for j in range(i+1,len(arr)):
#                 if(dep[j]<arr[i]):
#                     count+=1
#             ans=max(ans,count)
#         return ans


# arr=[900,940,950,1100,1500,1800]
# dep=[910,1200,1120,1130,1900,2000]
# s=Solution()
# print(s.minPlatform(arr,dep))




