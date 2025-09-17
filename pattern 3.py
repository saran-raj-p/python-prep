n = 5
for i in range(n):
    for j in range(n):
        if(j==i or j==n-1 or i==0):
            print("*",end="")
        else:
            print(" ",end="")
    
    print()

for i in range(n):
    for j in range(i+1):
        if(j==0 or i==j or i==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    
    print()
