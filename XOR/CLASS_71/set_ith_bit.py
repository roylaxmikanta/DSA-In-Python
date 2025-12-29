n=int(input("Enter a number n="))
i=int(input("Enter the bit position i to check (0-indexed)="))
print(n|(1<<i))