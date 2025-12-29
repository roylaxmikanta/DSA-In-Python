n=int(input("Enter a number n="))
i=int(input("Enter the bit position i to check (0-indexed)="))
# if(((n>>i)&1)==1):
#     print(True)
# else:
#     print(False)

if(n&(1<<i))!=0:
    print(True)
else:
    print(False)