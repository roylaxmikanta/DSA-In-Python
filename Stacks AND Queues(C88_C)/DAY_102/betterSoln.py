class Solution:
    def totalFruit(self, nums):
        max_len=0
        right=0
        left=0
        my_dict={}
        n=len(nums)
        while(right<n):
            my_dict[nums[right]]=my_dict.get(nums[right],0)+1
            while(len(my_dict)>2):
                my_dict[nums[left]]-=1
                if(my_dict[nums[left]]==0):
                    del my_dict[nums[left]]
                left+=1
            if(len(my_dict)<=2):
                max_len=max(max_len,right-left+1)
            right+=1
        return max_len
s=Solution()
print(s.totalFruit([1,2,3,2,2]))