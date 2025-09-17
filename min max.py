a=[6,2,7,8,13,5,12]
max=a[len(a)-1]
min=a[0]
for i in a:
    if(i>max):
        max = i

    if(i<min):
        min = i

print(f"min:{min},max:{max}")
