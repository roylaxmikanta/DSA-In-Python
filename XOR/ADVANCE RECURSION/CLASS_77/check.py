def solve(index, total, sub):
    target =9
    nums=[5,9,4]
    result=[]
    if(total==target):
        result.append(sub.copy())
        return True
    elif(total>target):
        return False
    if(index>=len(nums)):
        return False
    sub.append(nums[index])
    sum=total+nums[index]
    pick = solve(index+1,sum,sub)
    if(pick==True):
        return True
    e=sub.pop()
    sum=total
    not_pick = solve(index+1,sum,sub)
    return not_pick
print(solve(0,0,[]))









# Move these outside so they are accessible everywhere
# nums = [5, 8, 6]
# target = 9
# def solve(index, total, sub):
#     if total == target:
#         return True
#     elif total > target:
#         return False
#     if index >= len(nums):
#         return False
#     sub.append(nums[index])
#     if solve(index + 1, total + nums[index], sub) == True:
#         return True
#     sub.pop() 
#     if solve(index + 1, total, sub) == True:
#         return True
#     return False
# solve(0, 0, [])