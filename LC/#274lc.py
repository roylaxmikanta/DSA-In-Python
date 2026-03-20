# class Solution:
#     def hIndex(self, citations):
#         citations=sorted(citations)
#         hash_map={}
#         for num in citations:
#             if num not in hash_map:
#                 hash_map[num]=1
#             else:
#                 hash_map[num]+=1
#         # return hash_map
#         remaining=len(citations)
#         for key in hash_map:
#             if(key<1):
#                 remaining-=hash_map[key]
#             else:
#                 break
#         # return remaining
#         for i in range(1,citations[-1]+1):
#             if(remaining<i):
#                 return i-1
#             else:
#                 if(i in hash_map):
#                     remaining-=hash_map[i]
# s=Solution()
# print(s.hIndex([1,3,1]))    




#optimal
class Solution:
    def hIndex(self, citations):
        citations=sorted(citations)
        remaining=len(citations)
        for i in range(0,len(citations)):
            h=remaining-i
            if(citations[i]>=h):
                return h
        return 0  
s=Solution()
print(s.hIndex([1,3,1])) 