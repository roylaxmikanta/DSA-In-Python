nums=[19,4,2,11,6,5,3,10]
n=len(nums)
ans=[-1]*n
for i in range(0,n):
    for j in range(i+1,n):
        if(nums[i]<nums[j]):
            ans[i]=nums[j]
            break
print(ans)


#time complexity : O(n*(n+1)/2) ~ O(n*n)
#space complexity : O(n)---->this is our answer