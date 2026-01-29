def findMinCoins(coins,amount):
    result=[]
    n=len(coins)
    for i in range(n-1,-1,-1):
        while(amount>=coins[i]):
            result.append(coins[i])
            amount-=coins[i]
    return result
coins=[1,2,5,10,20,50,100,200,500,2000]
amount=999
print(findMinCoins(coins,amount))





#time complxity : O(N)
#Space complxity : O(1)