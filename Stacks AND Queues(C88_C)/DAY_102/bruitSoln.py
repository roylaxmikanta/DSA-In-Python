class Solution:
    def totalFruit(self, nums):
        max_len=0
        for i in range(0,len(nums)):
            my_set=set()
            for j in range(i,len(nums)):
                my_set.add(nums[j])
                if(len(my_set)<=2):
                    max_len=max(max_len,j-i+1)
                if(len(my_set)>2):
                    break
        return max_len
s=Solution()
print(s.totalFruit([1,2,3,2,2]))
#time complexity : O(N*N)
#space complaxity: O(1)-----> this is a digit which is my answer
