class Solution:
    def searchMatrix(self, matrix, target):
        # i=0
        # while(i<len(matrix)):
        #     j=0
        #     while(j<len(matrix[0])):
        #         if(matrix[i][j]==target):
        #             return True
        #         j+=1
        #     i+=1
        # return False

        #optimal solution   
        low=0
        high=len(matrix)*len(matrix[0])-1
        while(low<=high):
            mid=(low+high)//2
            if(matrix[mid//len(matrix[0])][mid%len(matrix[0])]==target):
                return True
            elif(matrix[mid//len(matrix[0])][mid%len(matrix[0])]>target):
                high=mid-1
            else:
                low=mid+1
        return False


s=Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],19))