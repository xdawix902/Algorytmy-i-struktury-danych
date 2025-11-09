import random
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

    while swapped:
        swapped = False
        for i in range(start, end):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        counter += 1

        end -= 1

        for i in range(end, start, -1):
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