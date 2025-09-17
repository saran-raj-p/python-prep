n = int(input("enter the number:"))
k = n*3
t=k

for i in range(n):
    count=n-1
    current=0
    t = k-i
    for j in range(i+1):
        
        if j==0:
            print(k-i,end=" ")
            
        else:
            
            current = t-count
            print(current,end=" ")
            t=current
            count -=1
            
            
            
    print()
