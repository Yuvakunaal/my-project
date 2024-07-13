def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sorted_left = MergeSort(left)
    sorted_right = MergeSort(right)
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def run():
    arr = [80,45,60,40,30,10,67,88,23]
    a = MergeSort(arr)
    print(f"Sorted array = {a}")
run()