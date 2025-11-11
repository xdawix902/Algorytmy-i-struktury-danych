def insertionSort(arr):
    # Klasyczne sortowanie przez wstawianie (insertion sort)
    n = len(arr)
    for i in range(1, n):
        key = arr[i]       # element, który "wstawiamy" w odpowiednie miejsce na lewo
        j = i - 1
        # Przesuwamy większe elementy w prawo, aż znajdziemy miejsce dla key
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # Wstawiamy key w znalezione miejsce
        arr[j+1] = key


def bucketSort(arr, number_of_buckets):
    # Sortowanie kubełkowe (bucket sort):
    # 1) rozdzielamy elementy do kubełków według zakresów,
    # 2) każdy kubełek sortujemy (tu: insertion sort),
    # 3) scalimy kubełki z powrotem do arr.
    _arr = []                      # lista kubełków (lista list)
    max_el = max(arr)              # maksimum w danych
    min_el = min(arr)              # minimum w danych
    # Szerokość jednego kubełka (przedział wartości, który do niego trafia)
    number_range = (max_el - min_el) / number_of_buckets

    # Tworzymy puste kubełki
    for i in range(number_of_buckets):
        _arr.append([])

    # Wrzucamy elementy do odpowiednich kubełków na podstawie ich wartości
    for i in arr:
        # Wyznacz indeks kubełka po położeniu i względem min_el i szerokości kubełka
        # Uwaga: dla elementu równego max_el indeks mógłby wyjść równy number_of_buckets,
        # więc poniżej zabezpieczenie (przypisujemy do ostatniego kubełka).
        bucket_index = int((i - min_el) / number_range) if number_range != 0 else 0
        if bucket_index == number_of_buckets:
            bucket_index = number_of_buckets - 1
        _arr[bucket_index].append(i)

    # Każdy kubełek sortujemy np. insertion sortem (często szybki dla małych list)
    for i in range(number_of_buckets):
        insertionSort(_arr[i])

    # Sklejamy posortowane kubełki z powrotem do wyjściowej tablicy
    k = 0
    for i in range(number_of_buckets):
        for j in range(len(_arr[i])):
            arr[k] = _arr[i][j]
            k += 1
    return arr


def radixSort(arr):
    # Próba sortowania pozycyjnego (radix sort) – LSD (od najmniej znaczącej cyfry)
    # max1 to największy element, użyty do określenia liczby cyfr
    max1 = max(arr)
    exp = 1
    # Dopóki mamy jeszcze kolejne rzędy wielkości do obsłużenia (1, 10, 100, ...)
    while max1 / exp >= 1:
        # UŻYCIE bucketSort z argumentem exp jako "liczba kubełków"
        bucketSort(arr, exp)
        exp *= 10


# Przykład użycia
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print(arr)
