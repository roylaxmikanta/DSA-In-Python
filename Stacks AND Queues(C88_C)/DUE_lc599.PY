# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
class Solution:
    def findRestaurant(self, list1, list2):
        hashmap={}
        res=[]
        min_sum=float('inf')
        for i in range(len(list1)):
            hashmap[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in hashmap:
                index_sum=hashmap[list2[j]]+j
                if index_sum<min_sum:
                    min_sum=index_sum
                    res=[list2[j]]
                elif index_sum==min_sum:
                    res.append(list2[j])
        return res
s=Solution()
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))  #ans ["Shogun"]