n = int(input("Enter the number:"))

low = 1
high = n

while(low<=high):
    mid = (low+high)//2
    if((mid*mid)==n):
        print(mid)
        break
    elif(mid*mid<n):
        low = mid+1
    else:
        high=mid-1



        
    
