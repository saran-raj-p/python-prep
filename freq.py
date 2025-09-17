max=-1
l=[1,2,3,3,3,2,1,4,5,5,4,6]
for i in l:
    if(i>max):
        max=i
count =[]
for i in range(max+1):
    count.append(0)

for i in l:
    count[i] +=1

for i in range(len(count)):
    print(f"{i}:{count[i]}")
