def TernarySearch(arr,target,left,right):   
    if left <= right:
        mid1 = left + ((right - left ) // 3)   
        mid2 = right - ((right - left ) // 3)  
        if target == arr[mid1]:
            return mid1 
        elif target == arr[mid2]:
            return mid2 
        else:
            if target < arr[mid1]:
                return TernarySearch(arr,target,left,mid1-1)
            elif target > arr[mid2]:
                return TernarySearch(arr,target,mid2+1,right)
            else:
                return TernarySearch(arr,target,mid1+1,mid2-1)
    return None
def run():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 16
    a = TernarySearch(arr, target,0,len(arr)-1)
    if a is None:
        print(f"{target} is not found in the array!")
    else:
        print(f"{target} is found at index = {a}")
run()