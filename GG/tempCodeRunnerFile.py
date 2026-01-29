class Solution:
    def countDistinct(self, arr, k):
        # Code here
        result=[]
        temp=0
        while(temp!=len(arr)+1-k):
            has_list={}
            count=0
            for i in range(k):
                if(arr[i+temp] not in has_list):
                    has_list[arr[i+temp]] = True
                    count += 1
            result.append(count)
            temp+=1
        return result
s=Solution()
s.countDistinct([1,2,1,3,4,2,3],4)