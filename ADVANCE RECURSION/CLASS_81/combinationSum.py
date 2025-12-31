class Solution:
    def CombinationSum(self,index,total,sub,target,nums,answer):
        if(total==target):
            answer.append(sub.copy())
            return
        if(index>=len(nums)):
            return
        if total > target:
            return
        sub.append(nums[index])
        curr_sum=total+nums[index]
        self.CombinationSum(index,curr_sum,sub,target,nums,answer)
        sub.pop()
        self.CombinationSum(index+1,total,sub,target,nums,answer)
        return answer
s=Solution()
nums=[2,3,6,7]
answer=[]
print(s.CombinationSum(0,0,[], 7,nums,answer))
