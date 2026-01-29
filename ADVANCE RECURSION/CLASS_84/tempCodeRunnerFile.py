class Solution:
    def combinationSUM(self,index,k,target,total,subset,answer,nums):
        if(len(subset)==k and total==target):
            answer.append(subset.copy())
            return
        if len(subset) > k or total > target or index == len(nums):
            return
        sum=total+nums[index]
        subset.append(nums[index])
        self.combinationSUM(index+1,k,target,sum,subset,answer,nums)
        subset.pop()
        self.combinationSUM(index+1,k,target,total,subset,answer,nums)
        # return answer
s=Solution()
answer=[]
s.combinationSUM(0,3,9,0,[],answer,[1,2,3,4,5,6,7,8,9])
print(answer)