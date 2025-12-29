nums= [1,2,3]
n=len(nums)
total_subsets=1<<n  #2^n find 
# print(total_subsets)
result=[]
for num in range(0,total_subsets):
    lists=[]
    for i in range(0,n):
        if(num&(1<<i)!=0):
            lists.append(nums[i])
    result.append(lists)
print(result)
