class Solution:
    def flipAndInvertImage(self, image):
        for i in range(0,len(image)):
            image[i]=image[i][::-1]
        for i in range(0,len(image)):
            for j in range(0,len(image[0])):
                if(image[i][j]==0):
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image    
s=Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))



#better solution
class Solution:
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i] = [1 - x for x in image[i][::-1]]
        return image
s=Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))