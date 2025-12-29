def solve(index, total, sub):
    target =9
    nums=[5,9,4]
    result=[]
    if(total==target):
        result.append(sub.copy())
        return print(result)
    elif(total>target):
        return
    if(index>=len(nums)):
        return
    sub.append(nums[index])
    sum=total+nums[index]
    solve(index+1,sum,sub)
    e=sub.pop()
    sum-=e
    solve(index+1,sum,sub)
    # return result

solve(0,0,[])

























# def solve(index, total, sub):
#     target = 9
#     nums = [5, 9, 4]
#     result = []
#     if total == target:
#         result.append(sub.copy())
#         print(result)
#         return
#     elif total > target:
#         return
#     if index >= len(nums):
#         return
#     sub.append(nums[index])
#     sum = total + nums[index]
#     solve(index + 1, sum, sub)
#     e = sub.pop()
#     sum -= e
#     solve(index + 1, sum, sub)
# solve(0, 0, [])