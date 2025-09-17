n = int(input("enter:"))
i=0

while(i<n):
    space = n-i-1
    while(space>0):
        print(end=" ")
        space -=1

    star = i+1
    while(star>0):
        print("*",end=" ")
        star -=1
    print()

    i+=1
    
    
    
        
