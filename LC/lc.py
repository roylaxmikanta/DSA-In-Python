class Solution:
    def addToArrayForm(self, num, k):
        total = 0
        for i in range(0,len(num)):
            total=total+(10**(len(num)-1-i))*num[i]
        total=total+k
        return total
        answer = []
        while(total>0):
            ld=total%10
            answer.append(ld)
            total=total//10
        return answer[::-1]
s=Solution()
print(s.addToArrayForm([1,2,0,0], 34))