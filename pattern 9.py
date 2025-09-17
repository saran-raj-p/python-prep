n = int(input("enter:"))
for i in range((2*(n-1))+1):
    for j in range((2*(n-1))+1):
        if j-i==2 or i+j==2 or i-j==2 or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
        
    
