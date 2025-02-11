def binarySearch(arr,l,r,x):
    if r >=1:
        mid=l+(r-1)//2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binarySearch(arr,l,mid-1, x)
        
        else:
            return binarySearch(arr,mid+1,r,x)
        
    else:
        return -1
    

arr = [2,3,4,10,40]
x = 10

result = binarySearch(arr,0,len(arr)-1, x)

if result != 1:
    print("Element {} is present at index {}".format(x,result))
else:
    print("Element is not present at array")