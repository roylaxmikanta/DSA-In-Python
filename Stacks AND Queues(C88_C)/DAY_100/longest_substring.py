class Solution:
    def lengthOfLongestSubstring(self,s):
        maxi=0
        n=len(s)
        for i in range(0,n):
            count=0
            my_set=set()
            for j in range(i,n):
                if(s[j] in my_set):
                    break
                if(s[j] not in my_set):
                    count+=1
                    my_set.add(s[j])
                if(count>maxi):
                    maxi=count
        return maxi
s=Solution()
print(s.lengthOfLongestSubstring("CADBZABCD"))



#time complexity : O(N*(N+1)/2)
#space complaxity : (N)