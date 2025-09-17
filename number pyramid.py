n = int(input("enter:"))
k=1
for i in range(1, (n//2)+1):   
    for j in range(1, i):  
        print(k, end=" ")
        k += 1
    print() 
