def BinarySearch(arr,target):
    left,right = 0,len(arr)-1
    while left <= right :
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else :
        return None
def run():
    arr = [2,3,4,5,6]
    target = 3
    a = BinarySearch(arr,target)
    if a is None:
        print(f"{target} is not found in the array!")
    else:
        print(f"{target} is found at index = {a}")
run()