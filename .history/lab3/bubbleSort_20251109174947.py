def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 32, 52, 16, 13]
bubbleSort(arr)
print(arr)