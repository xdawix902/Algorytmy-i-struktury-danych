import random


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bucketSort(arr, noOfBuckets):
    if len(arr) == 0:
        return arr

    # Odnalezienie minimalnej i maksymalnej wartosc w zbiorze danych
    max_ele = max(arr)
    min_ele = min(arr)

    # rozmiar kubelkow
    rnge = (max_ele - min_ele) / noOfBuckets if max_ele != min_ele else 1  # zakres dla kazdego wiadra

    temp = []

    # stworz puste kubelki
    for i in range(noOfBuckets):
        temp.append([])

    # Umieszczanie elementow tablicy w dedykowanych kubelkach
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)

        # dolacz elemnty graniczne do nizszej tablicy
        if (diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])

        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])

    # posortuj poszczegolne kubelka z wykorzystaniem insertionsort
    for i in range(noOfBuckets):
        temp[i] = insertionSort(temp[i])

    # polacz poszczegolne wyniki
    k = 0
    for i in range(noOfBuckets):
        for j in range(len(temp[i])):
            arr[k] = temp[i][j]
            k += 1
    return arr


arr = []
for i in range(50):
    arr.append(random.uniform(-1,1))

noOfBuckets = 5
bucketSort(arr, noOfBuckets)
print("Tablica posortowana: ", arr)

# range=(max-min)/n
# bucketIndex=(arr[i]-min)/range