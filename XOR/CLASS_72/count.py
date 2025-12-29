start=int(input("Enter a number start="))
goal=int(input("Enter a number n="))
ans = start ^ goal
count=0
for i in range(0,32):
    if(ans&(1<<i)!=0):
        count+=1
print(count)