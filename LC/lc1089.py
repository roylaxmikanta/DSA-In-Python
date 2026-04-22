class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        answer=[]
        i=0
        while(len(answer)!=len(arr)):
            if(arr[i]==0):
                answer.append(0)
                answer.append(0)
                i+=1
            else:
                answer.append(arr[i])
                i+=1
        return answer

s=Solution()
print(s.duplicateZeros([1,0,2,3,0,4,5,0]))