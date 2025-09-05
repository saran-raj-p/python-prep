#sort alphabetic order
word = "he is a boy"
arr = word.split(" ")

i=0;

while(i<len(arr)-1):
    j=i+1;
    while(j<len(arr)):
        if(arr[i][0]>arr[j][0]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        j +=1

    i += 1


print(arr)
