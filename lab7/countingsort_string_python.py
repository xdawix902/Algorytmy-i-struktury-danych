def countSort(arr):
  
    # posortowane wyjscie
    output = [0 for i in range(len(arr))]
  
    # stworzenie tablicy licznikow i zainicjalizowanie jej jako 0
    count = [0 for i in range(256)]
  
    # do przechowywania odpowiedzi
    # string jest niezmienny
    ans = ["" for _ in arr]
  
    # przechowyanie liczby zliczonych znakow
    for i in arr:
        count[ord(i)] += 1 #ord to funkcja ktora zwraca integery, 
                            #reprezentujace znak w Unicode
                            #przykladowe wykorzystanie: character = 'P'
                            # unicode_char = ord(character)
                            # print(unicode_char)
                            # to daje 80
                            
  
    # zmien count[i] tak aby count[i] teraz przechowywal
    # pozycje tego znaku w tablicy odpowiedzi 
    for i in range(256):
        count[i] += count[i-1]
  
    # zbuduj tablice odpowiedzi
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
  
    # skopiuj tablice wyjsciowa do arr,
    # teraz arr przechowuje posortowane znaki
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans 

arr = "dupsko"
#arr = "0122345"
ans = countSort(arr)
print("posortowana tablica % s" %("".join(ans))) # The join() method takes all items in an iterable and joins them into one string.
                        #A string must be specified as the separator: string.join(iterable)
                        # np. myDict = {"name": "John", "country": "Norway"}
                        # mySeparator = "TEST"
                        # x = mySeparator.join(myDict)
                        # print(x)