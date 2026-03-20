class Solution(object):
    def longestCommonPrefix(self, strs):
        answer=""
        for i in range(0,len(strs[0])):
            j=1
            while(j<len(strs)):
                if(i>=len(strs[j]) or strs[0][i]!=strs[j][i]):
                    return answer
                elif(j==len(strs)-1 and strs[0][i]==strs[j][i]):
                    answer+=strs[0][i]
                j+=1
        return answer
s=Solution()
print(s.longestCommonPrefix(["flowe","flow","flight"]))