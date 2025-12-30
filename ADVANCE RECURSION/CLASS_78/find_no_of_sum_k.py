def solve(index,total):
    target =3
    nums=[1,2,3,1]
    if(total==target):
        return 1
    elif(total>target):
        return 0
    if(index>=len(nums)):
        return 0
    sum=total+nums[index]
    pick = solve(index+1,sum)
    sum=total
    not_pick = solve(index+1,sum)
    return pick + not_pick
print(solve(0,0))