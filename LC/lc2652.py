class Solution:
    def sumOfMultiples(self, n: int) -> int:
        answer=0
        i=1
        while(3*i<=n or 5*i<=n or 7*i<=n):
            if 3*i<=n:
                answer=answer+(3*i)
            if 5*i<=n:
                answer=answer+(5*i)
            if 7*i<=n:
                answer=answer+(7*i)
            i+=1
        # i=1
        # while(5*i<=n):
        #     answer=answer+(5*i)
        #     i+=1
        # i=1
        # while(7*i<=n):
        #     answer=answer+(7*i)
        #     i+=1
        return answer
s=Solution()
print(s.sumOfMultiples(7))