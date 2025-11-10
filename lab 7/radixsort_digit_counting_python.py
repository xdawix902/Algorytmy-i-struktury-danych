def countingSort(arr, exp1):
 
    n = len(arr)
 
    # definiujemy tymczasowa tablice wyjsciowa (wyzerowana)
    output = [0] * (n)
 
    # inicjalizacja tablicy zliczajacej 
    # dla algorytmu sortowania przez zliczanie (wyzerowana)
    # mamy tu 10 licznikow, bo zliczamy cyfry z zakresu 0-9
    count = [0] * (10)
 
    # przechowaj ilosc wystepowania poszczegolnych elementow w tablicy count    
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # zamien count[i] tak aby count[i] teraz zawieral faktyczna
    # pozycje danej cyfry w tablicyt wyjsciowej
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # zbuduj tablice wyjsciowa
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # kopiowanie output[] do arr[],
    # tak, aby arr teraz przechowywala posortowane elementy
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
def radixSort(arr):
 
    # znajdz wartosc maksymalna w arr
    # aby wiedziec ile cyfr bedzie sortowanych
    max1 = max(arr)
    
    # dokonaj sortowania przez zliczanie
    # zamiast przekazywac numer cyfry, przekazujemy exp
    # exp to 10^i, gdzie i to numer aktualnej cyfry 
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
 
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i])