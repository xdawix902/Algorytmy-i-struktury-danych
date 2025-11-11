def counting_sort_real_numbers(arr, decimal_places=2):
    """
    Sortuje liczby rzeczywiste (floaty) za pomocą algorytmu Counting Sort.

    Counting Sort normalnie działa tylko dla liczb całkowitych,
    więc w tym wariancie liczby rzeczywiste są najpierw *przeskalowywane*
    (mnożone przez 10^decimal_places), aby stały się całkowite.
    Po posortowaniu przeskalowujemy je z powrotem do postaci rzeczywistej.

    :param arr: Lista liczb rzeczywistych do posortowania (np. [3.14, 2.71, 1.41])
    :param decimal_places: Liczba miejsc po przecinku, które chcemy zachować (np. 2)
    :return: Nowa lista — liczby rzeczywiste posortowane rosnąco.
    """

    # Jeśli lista jest pusta, zwracamy pustą listę (brak danych do sortowania)
    if not arr:
        return []

    # Skalowanie liczb rzeczywistych do całkowitych
    # ------------------------------------------------
    # Przykład: dla decimal_places = 2
    # liczba 3.14 → 314
    # liczba 2.71 → 271
    #
    # Dzięki temu możemy użyć algorytmu Counting Sort,
    # który działa tylko na liczbach całkowitych.
    factor = 10 ** decimal_places   # np. 10^2 = 100
    # W Pythonie 3 to wystarczy, bo działa precyzyjne mnożenie floatów.
    # W Pythonie 2 (stare wersje) można by wymusić rzutowanie na float:
    # factor = float(10 ** decimal_places)

    # Zaokrąglamy i przekształcamy wszystkie liczby do intów
    scaled_arr = [int(round(num * factor)) for num in arr]
    # Teraz np. [3.14, 1.59, 2.65] → [314, 159, 265]

    # Znajdowanie minimum i maksimum
    # ---------------------------------
    # Dzięki temu wiemy, jaki zakres liczb występuje — potrzebny do stworzenia tablicy count.
    min_val = min(scaled_arr)
    max_val = max(scaled_arr)

    # Tworzenie tablicy zliczeń
    # ------------------------------
    # Jej długość to (max - min + 1), czyli liczba możliwych wartości w zakresie.
    # Każdy indeks odpowiada konkretnej liczbie (po przesunięciu o min_val).
    count = [0] * (max_val - min_val + 1)

    # Zliczanie wystąpień każdej liczby całkowitej (po skalowaniu)
    # ---------------------------------------------------------------
    for num in scaled_arr:
        # Używamy przesunięcia o min_val, żeby indeksy zaczynały się od 0
        count[num - min_val] += 1

    # Po tym kroku tablica `count` mówi, ile razy wystąpiła dana wartość.
    # Np. count[3] = 2 → znaczy, że liczba (min_val + 3)/factor wystąpiła dwa razy.

    # Tworzenie posortowanej listy ze zliczeń
    # -------------------------------------------
    sorted_arr = []
    for i, c in enumerate(count):
        # Każdy indeks i odpowiada wartości (i + min_val)
        # Jeśli np. count[i] = 3 → znaczy, że ta liczba występuje 3 razy.
        # Dlatego powielamy ją count[i] razy i dopisujemy do wyniku.
        sorted_arr.extend([i + min_val] * c)

    # Przywrócenie do wartości rzeczywistych
    # ------------------------------------------
    # Cofamy skalowanie — dzielimy każdą liczbę przez ten sam czynnik.
    # Np. 314 → 3.14
    result = [num / factor for num in sorted_arr]

    # Zwracamy wynikową (posortowaną) listę liczb rzeczywistych
    return result


# Przykład użycia
#if __name__ == "__main__":
arr = [3.14, 1.59, 2.65, 3.58, 2.71, 3.14, 1.41]
sorted_arr = counting_sort_real_numbers(arr, decimal_places=2)
print("Przed sortowaniem:", arr)
print("Po sortowaniu:", sorted_arr)
