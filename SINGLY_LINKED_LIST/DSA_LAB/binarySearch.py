def binary_Search(nums,low,high,k):
    if(low<=high):
        mid=(low+high)//2
        if(nums[mid]==k):
            return mid
        if(nums[mid]<k):
            return binary_Search(nums,mid+1,high,k)
        if(nums[mid]>k):
            return binary_Search(nums,low,mid-1,k)
    return -1

nums=[1,2,3,4,5,6,7]
print(binary_Search(nums,0,len(nums)-1,5))

