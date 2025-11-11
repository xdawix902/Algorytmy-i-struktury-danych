import random
import time


def heapifyMax(arr: list[int], n:int, i: int):
    largest: int = i

    l: int = 2*i +1
    r: int = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapifyMax(arr, n, largest)

def heapifyMin(arr: list[int], n:int, i: int):
    largest: int = i

    l: int = 2*i +1
    r: int = 2*i + 2

    if l < n and arr[largest] > arr[l]:
        largest = l
    if r < n and arr[largest] > arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapifyMax(arr, n, largest)

def heapsortMax(arr: list[int]):
    n: int = len(arr)
    for i in range(n//2-1,-1,-1):
        heapifyMax(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapifyMax(arr, i, 0)
#
# arr = [4, 10, 3, 5, 1]
# n = len(arr)
# heapsortMax(arr)
# for i in range(n):
#     print("%d " % arr[i])

def heapsortMin(arr: list[int]):
    n: int = len(arr)
    for i in range(n//2-1,-1,-1):
        heapifyMin(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapifyMin(arr, i, 0)

N = 30000
arr = [random.randint(-100, 100) for _ in range(N)]

n = len(arr)
start = time.perf_counter()
heapsortMax(arr)
elapsed_ms = (time.perf_counter() - start) * 1000.0

for i in range(n):
    print("%d " % arr[i])
print(f"elapsed: {elapsed_ms:.3f} ms")

