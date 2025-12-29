def solve(index,subset):
    nums=[3,1,2]
    if(index>=len(nums)):
        print(subset)
        return
    #include
    subset.append(nums[index])
    solve(index+1,subset)
    #exclude
    subset.pop()
    solve(index+1,subset)
result=[]
solve(0,result)