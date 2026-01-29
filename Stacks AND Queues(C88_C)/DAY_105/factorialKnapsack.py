class Solution:
    def fractionalKnapsack(self, arr, weight):
        n=len(arr)
        for i in range(0,n):
            for j in range(i+1,n):
                if((arr[i][0])/(arr[i][1])<(arr[j][0])/(arr[j][1])):
                    arr[i],arr[j]=arr[j],arr[i]
        total=0
        index=0
        while(weight>=0):
            temp_weight=weight-arr[index][1]
            if(temp_weight<0):
                break
            else:
                weight-=arr[index][1]
            total+=arr[index][0]
            index+=1
        if(weight!=0):
            total+=(((arr[index][0])/(arr[index][1]))*weight)
        return total
s=Solution()
print(s.fractionalKnapsack([(100,20),(60,10),(100,50),(200,50)],90))

#time complexity : O(N^2) for sorting + O(N) for iterating through the weights
#space complexity : O(1)    
#https://www.geeksforgeeks.org/fractional-knapsack-problem/