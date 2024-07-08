def BubbleSort(arr):
    n = len(arr)
    while True:
        is_swapped = False
        for i in range(0,n-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                is_swapped = True
        if not is_swapped:
            break
        n-=1
def run():
    arr = [2,5,3,1,4]
    BubbleSort(arr)
    print(f"Sorted array = {arr}")
run()
