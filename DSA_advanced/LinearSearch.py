def LinearSearch(arr,target):
    for i in arr:
        if i == target:
            return arr.index(i)
    return None
def run():
    arr = [2,4,6,8]
    target = 6
    a = LinearSearch(arr,target)
    if a is None:
        print(f"{target} is not found in the array!")
    else:
        print(f"{target} is found at index = {a}")
run()
