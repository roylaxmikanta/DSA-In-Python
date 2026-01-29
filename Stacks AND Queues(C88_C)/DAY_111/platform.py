# class Solution:    
#     def minPlatform(self, arr, dep):
#         ans=1
#         for i in range(0,len(arr)):
#             count=1
#             for j in range(i+1,len(arr)):
#                 if(arr[i]<dep[j]):
#                     count+=1
#             ans=max(ans,count)
#         print(ans)
# s=Solution()
# arr=[900,940,950,1100,1500,1800]
# dep=[910,1200,1120,1130,1900,2000]
# s.minPlatform(arr,dep)











# class Solution:    
#     def minPlatform(self, arr, dep):
#         arr.sort()
#         dep.sort()
#         n=len(arr)
#         i=1
#         j=0
#         platform=1
#         result=1
#         while(i<n and j<n):
#             if(arr[i]<=dep[j]):
#                 platform+=1
#                 i+=1
#             else:
#                 platform-=1
#                 j+=1
#             result=max(result,platform)
#         print(result)
# s=Solution()
# arr=[900,940,950,1100,1500,1800]
# dep=[910,1200,1120,1130,1900,2000]
# s.minPlatform(arr,dep)