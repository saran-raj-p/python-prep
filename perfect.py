def perfect(num):
    a = []
    for i in range(1,(num//2)+1):
        if(num%i==0):
            a.append(i)

    sum =0;
    for i in a:
        sum +=i

    if(sum==num):
        return True
    else:
        return False



n = int(input("Enter the number:"))
print(perfect(n))
