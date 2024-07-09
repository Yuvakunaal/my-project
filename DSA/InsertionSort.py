def InsertionSort(arr): 
    N = len(arr) 
    for i in range(1, N): 
        target = arr[i]
        j = i - 1 
        while j >= 0 and target < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = target
def run():
    arr = [80,45,60,40,30,10,67,88,23]
    InsertionSort(arr)
    print(arr)
run()
