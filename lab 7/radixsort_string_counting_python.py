def radix_sort_strings(strings):
    """
    Sortuje listę stringów za pomocą algorytmu Radix Sort.
    
    :param strings: Lista stringów do posortowania.
    :return: Posortowana lista stringów.
    """
    if not strings:
        return strings

    # Znajdź maksymalną długość stringa
    max_length = len(max(strings, key=len))

    # Wyrównaj stringi, dodając spacje na końcu
    padded_strings = [s.ljust(max_length) for s in strings]

    # Sortuj zaczynając od ostatniego znaku
    for position in range(max_length - 1, -1, -1):
        padded_strings = counting_sort_by_char(padded_strings, position)

    # Usuń dodatkowe spacje
    return [s.rstrip() for s in padded_strings]

def counting_sort_by_char(strings, position):
    """
    Pomocnicza funkcja sortująca stringi według konkretnej pozycji (znaku).

    :param strings: Lista stringów.
    :param position: Indeks pozycji znaku, według którego ma być sortowanie.
    :return: Posortowana lista stringów.
    """
    # Zakładamy, że korzystamy z ASCII (256 możliwych znaków)
    count = [0] * 256
    output = ["" for _ in strings]

    # Zliczanie wystąpień znaków w danej pozycji
    for s in strings:
        count[ord(s[position])] += 1

    # Akumulacja liczników
    for i in range(1, 256):
        count[i] += count[i - 1]

    # Sortowanie stringów według bieżącej pozycji
    for s in reversed(strings):
        char = s[position]
        output[count[ord(char)] - 1] = s
        count[ord(char)] -= 1

    return output

# Przykład użycia
if __name__ == "__main__":
    strings = ["apple", "banana", "grape", "kiwi", "cherry", "mango"]
    sorted_strings = radix_sort_strings(strings)
    print("Posortowane stringi:", sorted_strings)