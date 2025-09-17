n = int(input("enter:"))
for i in range(n):
    for j in range(i,i+i+1):
        print(chr(65+j),end=" ")
        
    print()
