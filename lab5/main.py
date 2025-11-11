from typing import List


def insertionSort(arr: list[float]) -> list[float]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bucketSort(arr: list[float], num_buckets: int = 10) -> list[float]:
    n = len(arr)
    if n <= 1:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    if min_val == max_val:
        return arr  # wszystkie elementy są równe

    # Utworzenie pustych koszyków
    buckets: list[list[float]] = [[] for _ in range(num_buckets)]

    # Rozrzucenie elementów do koszyków (skalowanie do [0, num_buckets - 1])
    span = max_val - min_val
    for x in arr:
        idx = int((x - min_val) / span * (num_buckets - 1))
        buckets[idx].append(x)

    # Posortuj każdy koszyk insertion sortem
    for i in range(num_buckets):
        insertionSort(buckets[i])

    # Złóż wynik z powrotem do arr (in-place)
    k = 0
    for i in range(num_buckets):
        for x in buckets[i]:
            arr[k] = x
            k += 1

    return arr


arr = [
    0.8,
    0.399,
    0.45,
    0.87,
    0.7,
    0.55,
    0.003,
    0.15,
    0.999,
    0.5,
    0.666,
    0.3,
    0.1,
    0.2,
    0.79,
    0.7,
    0.8,
]

bucketSort(arr)
print(arr)
