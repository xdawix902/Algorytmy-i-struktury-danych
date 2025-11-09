import random


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def bucketSort(arr):
    if(len(arr)) == 0:
        return arr
    temp = []
    noOfBuckets = 10

    for i in range(noOfBuckets):
        temp.append([])

    for j in arr:
        bucketIndex = int(noOfBuckets*j)
        temp[bucketIndex].append(j)

    for i in range(noOfBuckets):
        temp[i] = insertionSort(temp[i])
    k = 0
    for i in range(noOfBuckets):
        for j in range(len(temp[i])):
            arr[k] = temp[i][j]
            k+= 1
    return arr



arr1 = []
arr2 = []
arr3 = []

random.seed(67)
for i in range(50):
    losowe = random.randint(1,100)
    arr1.append(losowe)
    arr2.append(losowe)
    arr3.append(losowe)
bucketSort(arr1)
print(arr1)

