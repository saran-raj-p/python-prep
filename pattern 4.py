n = 4
for i in range(1,n+1):
    for j in range(1,(2*n)):
        if(j==n+i-1 or i==n or j==n-i+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
