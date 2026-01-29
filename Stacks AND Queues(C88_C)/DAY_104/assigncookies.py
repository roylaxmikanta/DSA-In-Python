class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        m=len(g)
        n=len(s)
        left=right=0
        count=0
        while(left<n and right<m):
            if(g[left]<=s[right]):
                count+=1
                left+=1
                right+=1
            else:
                right+=1
        return count

        
s=Solution()
print(s.findContentChildren([1,2,8,6,4],[2,3,1,2,4,7]))   #ans 2




#time complaxity : O(Nlog(N))+O(Mlog(M)) for shorting + O(M) becausde this must be itrated
#https://leetcode.com/problems/assign-cookies/