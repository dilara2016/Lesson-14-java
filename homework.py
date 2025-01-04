def binarySearch(arr,l,r,x):
    while l <= r:

        mid = l+(r-1) // 2

        if arr[mid] < x:
            return mid
        
        elif arr[mid] <x:
            l = mid+1

        else:
            r=mid-1

    return -1


arr = [1,7,4,2,14,30,50]
x=14

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is present at index {}".format(x,result))
else:
    print("ELement is not present in array")