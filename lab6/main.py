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

arr = [0.8, 0.399, 0.45, 0.87, 0.7, 0.55, 0.003, 0.15, 0.999, 0.5, 0.666, 0.3, 0.1, 0.2, 0.79, 0.7, 0.8]
bucketSort(arr)
print(arr)