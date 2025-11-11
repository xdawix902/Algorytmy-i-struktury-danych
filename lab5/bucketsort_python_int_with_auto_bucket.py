import math

def insertionSort(arr):
    for i in range(1,len(arr)):     
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

def bucketSort(arr):
    if len(arr) == 0:
        return arr
    
    # Odnalezienie minimalnej i maksymalnej wartość w zbiorze danych
    max_ele = max(arr)
    min_ele = min(arr)
  
    #liczymy ilosc kubelkow
    noOfBuckets = int(math.ceil(len(arr) ** (1/2))) #Używamy pierwiastka z liczby elementów jako liczby wiader; ceil - zaokraglenie w gore
    # liczymy rozmiar kubelkow
    rnge = (max_ele - min_ele) / noOfBuckets if max_ele != min_ele else 1 # zakres dla każdego wiadra
  
    temp = []
  
    # stworz puste kubelki
    for i in range(noOfBuckets):
        temp.append([])
  
    # Umieszczanie elementow tablicy w dedykowanych kubelkach
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)
  
        # dolacz elemnty graniczne do nizszej tablicy
        if(diff == 0 and arr[i] != min_ele):
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

def betterSort(arr):
    negative = []
    positive = []

    for i in arr:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

    negative = bucketSort(negative)
    positive = bucketSort(positive)

    return negative+positive

  
arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
bucketSort(arr)
print("Tablica posortowana: ", arr)

floats = [
    -12.5, 3.14, 0.001, -0.75, 8.6, -2.3, 45.0, -9.81, 1.618, -3.333,
    7.25, -0.0042, 100.5, -56.78, 2.718, -14.0, 0.5, -0.125, 9.0, -22.2,
    33.33, -1.414, 0.007, -8.0, 4.2, -17.6, 0.09, -0.99, 6.66, -25.5
]

print()
print(betterSort(floats))
