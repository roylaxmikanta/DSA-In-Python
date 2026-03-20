class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        d1=((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)
        d2=((p2[0]-p3[0])**2)+((p2[1]-p3[1])**2)
        d3=((p3[0]-p4[0])**2)+((p3[1]-p4[1])**2)
        d4=((p1[0]-p4[0])**2)+((p1[1]-p4[1])**2)
        d5=((p1[0]-p3[0])**2)+((p1[1]-p3[1])**2)
        d6=((p2[0]-p4[0])**2)+((p2[1]-p4[1])**2)
        my_set=[d1,d2,d3,d4,d5,d6]
        my_set=sorted(my_set)
        if(my_set[0]==my_set[1] and my_set[2]==my_set[1] and my_set[2]==my_set[3] and my_set[4]==my_set[5]):
            return True
        return False
s=Solution()
print(s.validSquare([0,0],[1,1],[1,0],[0,1]))