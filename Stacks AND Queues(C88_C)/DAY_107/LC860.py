class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives=0
        ten=0
        n=len(bills)
        for i in range(0,n):
            if(bills[i]==5):
                fives+=1
            elif(bills[i]==10):
                if(fives>=1):
                    fives-=1
                    ten+=1
                else:
                    return False
            else:
                if(fives>=1 and ten>=1):
                    fives-=1
                    ten-=1
                elif(fives>=3):
                    fives-=3
                else:
                    return False
            
        return True
s=Solution()
print(s.lemonadeChange([5,5,10,5,10]))




#https://leetcode.com/problems/lemonade-change/description/
#time complxity : O(N)
#space complxity : O(N)