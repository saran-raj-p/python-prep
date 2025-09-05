n = int(input("enter the number:"))
sum = ""

x = n
while(x>0):
    r = x%2
    sum = str(r)+sum
    x //=2

print(sum)
