class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}
        for num in nums:
            if(num in hash_map):
                hash_map[num]+=1
            else:
                hash_map[num]=1
        for key in hash_map:            
            if(hash_map[key]==1):
                return key
s=Solution()
print(s.singleNumber([0,1,0,1,0,1,99]))