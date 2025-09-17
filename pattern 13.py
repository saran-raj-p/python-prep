n = int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(i-k,end=" ")
    for l in range(2,i+1):
        print(l,end=" ")

    print()
        
