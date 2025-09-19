def mergesort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while(i<len(left)and j<len(right)):
            if(left[i]<right[j]):
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while(i<len(left)):
            arr[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            arr[k]=right[j]
            j+=1
            k+=1



arr=[1,9,4,8,2,3,6,0,2,5,7,4,1]
mergesort(arr)
print(arr)
        
    
