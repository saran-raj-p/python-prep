n1 = int(input("enter the number:"))
n2 =  int(input("enter the number:"))

for i in range(n1,n2+1):
    sum =0
    for j in range(1,i):
        if(i%j==0):
            sum +=j


    if(sum==i):
        print(i)
    
