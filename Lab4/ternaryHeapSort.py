def ternaryHeapify(arr: list[int], n: int, i: int):
    largest: int = i
    left: int = 3*i + 1
    middle: int = 3*i + 2
    right: int = 3*i+3

    if left < n and arr[left] > arr[largest]:
        largest = left
    if middle < n and arr[middle] > arr[largest]:
        largest = middle
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        ternaryHeapify(arr, n, largest)

def ternaryHeapSort(arr: list[int]):
    n: int = len(arr)
    for i in range(n//3-1, -1, -1):
        ternaryHeapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i],arr[0] = arr[0],arr[i]
        ternaryHeapify(arr, i, 0)

arr = [12,11,13,5,6,7]
ternaryHeapSort(arr)
print("posortowane", arr)