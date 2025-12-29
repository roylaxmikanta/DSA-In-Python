# target =9
# nums=[5,7,6]
# def solve(index, total):
#     if(total==target):
#         print(True)
#         return True
#     elif(total>target):
#         return False
#     if(index>=len(nums)):
#         return False
#     sum=total+nums[index]
#     pick = solve(index+1,sum)
#     if(pick==True):
#         return True
#     sum=total
#     not_pick = solve(index+1,sum)
#     return False
# solve(0,0)

target = 9
nums = [5, 9, 6] 
def solve(index, total):
    if total == target:
        return True
    if total > target or index >= len(nums):
        return False
    if solve(index + 1, total + nums[index]):
        return True
    not_pick = solve(index + 1, total)
    return not_pick 
print(solve(0, 0))