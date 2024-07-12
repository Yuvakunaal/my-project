def partition(arr,left,right): 
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
def QuickSort(arr,left,right):
    if left < right: 
        pivot_index = partition(arr, left, right) #fix, find, sort the pivot
        QuickSort(arr,left,pivot_index-1) #sort left list 
        QuickSort(arr,pivot_index+1,right) #sort right list 
def run():
    arr = [80,45,60,40,30,10,67,88,23]
    QuickSort(arr,0,len(arr)-1)
    print(f"Sorted array = {arr}")
run()