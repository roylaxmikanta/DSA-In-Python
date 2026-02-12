class Solution:
    def minimumTotal(self, triangle):
        # total=0
        # row=0
        # while(row<len(triangle)):
        #     mini=triangle[row][0]
        #     for col in range(0,len(triangle[row])):
        #         mini=min(mini,triangle[row][col])
        #     total+=mini
        #     row+=1
        # return total
        for row in range(len(triangle)-2,-1,-1):
            for col in range(0,row+1):
                triangle[row][col]+=min(triangle[row+1][col],triangle[row+1][col+1])
        return triangle[0][0]
    
        

s=Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))