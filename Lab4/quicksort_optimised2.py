# coding=utf-8
#pivot - miejsce podziału tablicy, element pierwszy, ostatni, mediana lub losowy
import random

def insertionSort(arr):
    if len(arr) == 1:
        return arr
    for j in range(1, len(arr)):
        key = arr[j]
        i=j-1
        while i>=0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j], = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if abs(high - low) <= 10:
        insertionSort(arr[low:high])
    if low < high:
        pi = partition(arr, low, high)
        if (len(arr)-pi) > len(arr)//2:
            quickSort(arr, low, pi-1)
            quickSort(arr, pi + 1, high)
        else:
            quickSort(arr, pi + 1, high)
            quickSort(arr, low, pi - 1)

arr = []
for i in range(1, 2000):
    arr.append(random.randint(1,2000))

#arr = [12,41,15,52,11,14,36,18]
n = len(arr)
quickSort(arr,0, n-1)
#insertionSort(arr)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])