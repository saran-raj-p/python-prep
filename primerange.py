start = int(input("enter the starting value:"))
end = int(input("enter the ending value:"))
for i in range(start,end+1):
    count = 0
    for j in range(2,i):
        if i%j==0:
            count += 1
        
    if count <= 1:
        print(i)
