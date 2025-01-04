def fsm(nums, left=None, right=None):

    if left is None and right is None:
        (left, right) = (0,len(nums)-1)

    if left > right:
        return left
    
    mid = left + (right-left)//2

    if nums[mid] ==mid:
        return fsm(nums,mid+1,right)
    
    else:
        return fsm
    
if __name__ == '__main__':
    nums = [0,1,2,6,9,11,15]
    print("The smallest missing element is ", fsm(nums))