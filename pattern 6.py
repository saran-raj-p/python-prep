n = int(input("enter the number:"))
for i in range(n):
    for j in range(1,n+1-i):
        print(j,end="")
    print()


for i in range(n):
    for j in range(1,n+1-i):
        print(n-i,end="")
    print()
        
