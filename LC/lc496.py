# arr = [10, 20, 30, 20, 50]
# index = arr.index(20)
# print(index)

class Solution:
    def nextGreaterElement(self, nums1,nums2):
        for i in range(0,len(nums1)):
            index = nums2.index(nums1[i])
            if(index==len(nums2)-1):
                nums1[i]=-1
                break
            else:
                while(index<len(nums2)):
                    if(nums1[i]<nums2[index]):
                        nums1[i]=nums2[index]
                        break
                    elif(index==len(nums2)-1):
                        nums1[i]=-1
                    index+=1
        return nums1
s=Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))