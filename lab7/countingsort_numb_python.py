 def countingSort(array):
    # Długość tablicy wejściowej
    size = len(array)

    # Tworzymy pustą tablicę wynikową, w której umieścimy posortowane elementy
    output = [0] * size

    # Inicjujemy tablicę liczników (count)
    # Zakładamy, że wartości w array mieszczą się w zakresie 0–9
    count = [0] * 10

    # 1ZLICZANIE WYSTĄPIEŃ
    # Dla każdego elementu w tablicy wejściowej zwiększamy licznik o 1
    # Przykład: jeśli array[i] = 3 → count[3] += 1
    for i in range(0, size):
        count[array[i]] += 1

    # Po tym kroku tablica count zawiera liczbę wystąpień każdej wartości.
    # np. count[2] = 3 oznacza, że liczba „2” występuje 3 razy w array.

    # KUMULACJA (SUMY PREFIKSOWE)
    # Teraz przekształcamy tablicę count w tablicę skumulowaną,
    # tak aby count[i] przechowywało łączną liczbę elementów <= i.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Dzięki temu wiemy, na której pozycji w tablicy wynikowej
    # kończy się dana wartość.
    # Np. jeśli count[3] = 5 → oznacza to, że liczby ≤ 3
    # zajmują w posortowanej tablicy pierwsze 5 pozycji.

    # TWORZENIE TABLICY WYJŚCIOWEJ (OD KOŃCA)
    # Przechodzimy po tablicy wejściowej od końca, aby zachować stabilność sortowania.
    i = size - 1
    while i >= 0:
        # count[array[i]] mówi, na której pozycji (1-indeksowanej)
        # ma znaleźć się ostatnie wystąpienie tej wartości.
        # Dlatego wstawiamy element na pozycję count[array[i]] - 1 w output.
        output[count[array[i]] - 1] = array[i]

        # Zmniejszamy licznik, bo jedno wystąpienie tej liczby już wykorzystaliśmy.
        count[array[i]] -= 1

        # Przechodzimy do poprzedniego elementu
        i -= 1

    # KOPIOWANIE WYNIKU DO TABLICY WEJŚCIOWEJ
    # Na końcu kopiujemy elementy z tablicy wynikowej z powrotem do oryginalnej tablicy.
    for i in range(0, size):
        array[i] = output[i]

arr = [4, 2, 2, 8, 3, 3, 1]
countingSort(arr)
print("Tablica posortowana rosnąco:")
print(arr)