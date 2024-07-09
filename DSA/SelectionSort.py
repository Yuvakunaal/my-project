def SelectionSort(arr):
    N = len(arr)
    for i in range(0,N-1):  
        min_index = i 
        for j in range(i+1,N):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:  
            arr[i],arr[min_index] = arr[min_index],arr[i]
def run():
    arr = [80,45,60,40,30,10,67,88,23]
    SelectionSort(arr)
    print(arr)
run()