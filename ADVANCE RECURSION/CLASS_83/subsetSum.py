class Solution:
    def subsetsum(self,index,total,answer,nums):
        if(index>=len(nums)):
            answer.append(total)
            return
        curr_sum=total+nums[index]
        self.subsetsum(index+1,curr_sum,answer,nums)
        self.subsetsum(index+1,total,answer,nums)
        return answer

s=Solution()
print(s.subsetsum(0,0,[],[10,20,30]))