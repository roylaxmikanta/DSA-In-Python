class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}
        for i in range(0,len(nums)):
            if(nums[i] not in hash_map):
                hash_map[nums[i]]=1
            else:
                hash_map[nums[i]]+=1
        items = list(hash_map.items())
        my_set=set()
        answer=items[len(items)-1][0]
        for key, value in items[::-1]:
            if(value not in my_set):
                my_set.add(value)
                answer=key
        return answer

s=Solution()
print(s.firstUniqueFreq([20,20,10,30,30,30]))