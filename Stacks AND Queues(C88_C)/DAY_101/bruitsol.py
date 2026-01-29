nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
maxi=0
n=len(nums)
for i in range(0,n):
    zeros=0
    for j in range(i,n):
        if(nums[j]==0):
            zeros+=1
        if(zeros<=k):
            maxi=max(maxi,j-i+1)
print(maxi)

#time complexity : O(N*N)
#space complexity : O(1)