import random
<<<<<<< HEAD
from multiprocessing.util import sub_warning
from time import perf_counter_ns


def bubble_sort(arr: list[int]) -> int:

    swaps: int = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (arr[i] > arr[j]):
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t

                swaps += 1

    return swaps

def bubble_sort_cw(arr: list[int]) -> list[int]:

    #                [porównania, zamiany, milisekundy]
    ret: list[int] = [0,          0,        0]

    currenct_time: int = perf_counter_ns()

    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(len(arr) - i - 1):
            ret[0] += 1
            if arr[j] > arr[j+1]:
                ret[1] += 1
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
            if swapped == True:
                break

    ret[2] = -currenct_time + perf_counter_ns();
    return ret

def pullback(arr: list[int], i: int) -> int:

    swaps: int = 0

    while arr[i] < arr[i-1] and i > 0:
        t = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = t

        i -= 1

        swaps += 1

    return swaps

def insertion_sort(arr: list[int]) -> int:
    swaps: int = 0

    for i in range(1, len(arr)):
        swaps += pullback(arr, i)

    return swaps

def selection_sort(arr: list[int]) -> list[int]:

    #                [porównania, zamiany, milisekundy]
    ret: list[int] = [0,          0,        0]

    currenct_time: int = perf_counter_ns()

    for i in range(len(arr)):
        minidx: int = i

        for j in range(i, len(arr)):
            ret[0] += 1
            if arr[j] < arr[minidx]:
                ret[1] += 1
                minidx = j

        t: int = arr[i]
        arr[i] = arr[minidx]
        arr[minidx] = t

    ret[2] = -currenct_time + perf_counter_ns();
    return ret

def bidisort(arr: list[int]) -> int:
    n: int = len(arr)
    start: int = 0
    end: int = n-1
    swapped: bool = True

    swaps: int = 0
=======
import time


def bubbleSort(arr):
    n = len(arr)
    porownanie = 0
    zamiana = 0
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            porownanie += 1
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                zamiana+=1
                swapped = True
        if(swapped == False):
            break
    print(porownanie, zamiana)

def bidiSort(arr):
    n = len(arr)
    start = 0
    end = n-1
    swapped = True
    counter = 0
>>>>>>> da3ba907d4a70f343d70302bc7e2eb9dc082649b

    while swapped:
        swapped = False
        for i in range(start, end):
<<<<<<< HEAD
            if arr[i] > arr[i+1]:
=======
            if(arr[i] > arr[i+1]):
>>>>>>> da3ba907d4a70f343d70302bc7e2eb9dc082649b
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
<<<<<<< HEAD
=======
        counter += 1
>>>>>>> da3ba907d4a70f343d70302bc7e2eb9dc082649b

        end -= 1

        for i in range(end, start, -1):
<<<<<<< HEAD
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True
        start += 1
        swaps += 1

    return swaps

def pick_sort(arr: list[int]) -> list[int]:
    if len(arr) > 30:
        return selection_sort(arr)
    else:
        return bubble_sort_cw(arr)

arr: list[int] = [0, -1, 10, 2, 6, 9, -3]

a = list(arr)
print(a)
print("bubble sort:", bubble_sort(a))
print(a)

a = list(arr)
print(a)
print("insertion sort:", insertion_sort(a))
print(a)

a = list(arr)
print(a)
print("selection sort:", selection_sort(a))
print(a)

a = list(arr)
print(a)
# print("bidi sort:", bidisort(a))
print("bidi sort:", bidisort([3, 2, 5, 1, 4, 6]))
print(a)

def test():
    arr_len: int = random.randint(1, 100)

    arr: list[int] = [random.random() for _ in range(arr_len)]

    bubble: list[int] = bubble_sort_cw(arr)
    selection: list[int] = selection_sort(arr)
    pick: list[int] = pick_sort(arr)

    print("dla listy (długość =", len(arr), "):", arr)
    print("bubble sort:\n", "\tporownania:", bubble[0], "\n\tzamiany:", bubble[1], "\n\tmilisekundy:", bubble[2])
    print("selection sort:\n", "\tporownania:", selection[0], "\n\tzamiany:", selection[1], "\n\tmilisekundy:", selection[2])
    print("pick sort:\n", "\tporownania:", pick[0], "\n\tzamiany:", pick[1], "\n\tmilisekundy:", pick[2])
    print()


test()
=======
            if(arr[i-1] > arr[i]):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        start += 1
        counter == 1
    print(counter)
    return arr

def selectionSort(arr):
    current_time = time.perf_counter_ns()
    porownanie = 0
    zamiana = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            porownanie+=1
            if(arr[min_idx] > arr[j]):
                min_idx = j
        zamiana += 1
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
    print(porownanie, zamiana, current_time-time.perf_counter_ns())

"""arr = [64,26,13,21,12]
selectionSort(arr)
print("posortowana tablica")
for i in range(len(arr)):
    print(arr[i])"""

def zadanie1(arr):
    bubbleSort(arr)
    selectionSort(arr)

    if(len(arr) < 30):
        bubbleSort(arr)
    else:
        selectionSort(arr)


arr1=[]
arr2=[]
arr3=[]

random.seed(24)
for i in range(random.randint(1,100)):
    curr = random.randint(1,100)
    arr1.append(curr)
    arr2.append(curr)
    arr3.append(curr)

#zadanie1(arr1)

print(arr1)
selectionSort(arr1)
print(arr1)
>>>>>>> da3ba907d4a70f343d70302bc7e2eb9dc082649b
