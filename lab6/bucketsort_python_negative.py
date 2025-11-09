def insertionSort(arr):
    for i in range(1,len(arr)):     
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

def bucketSort(arr, n):
    if len(arr) == 0:
        return arr
    #tworzenie pustych kubelkow
    temp = []
    for i in range(n):
        temp.append([])
         
    # wsadzanie elementow z tablicy do kubelkow
    for i in range(n):
        ti = int(n*arr[i])
        temp[ti].append(arr[i])
     
    # sortowanie kubelkow
    for i in range(n):
        temp[i] = insertionSort(temp[i])
         
    # scalanie wynikow
    index = 0
    arr.clear() #clear() dziala w pythonie 3
    #arr *= 0 #to czysci tablice w pythoni 2, bo w pythonie 2 nie dziala clear()
    for i in range(n):
        for j in range(len(temp[i])):
            arr.append(temp[i][j])
 
#funkcja do dzielenia tablicy wejsciowej na dwie podtablice
def sortMixed(arr, n):
    Neg = []
    Pos = []
     
    # przechodzenie tablicy
    for i in range(n):
        if(arr[i]<0):
        #przechowywanie wartosci ujemnych poprzez ich konwersje na wartosci dodatnie
            Neg.append(-1*arr[i])
        else:
            # przechowywanie wartosci dodatnich
            Pos.append(arr[i])
            
    #sortowanie podtablic         
    bucketSort(Neg,len(Neg))
    bucketSort(Pos,len(Pos))
    
    #ostateczny wynik jest scalany najpierw elementow Neg[]
    #ktore musza byc z powrotem przekonwertowane na wartosci ujemne
    for i in range(len(Neg)):
        arr[i]=-1*Neg[len(Neg)-1-i]
         
    # nastepnie mozna powkladac wartosci z Pos[]
    for i in range(len(Neg),n):
        arr[i]= Pos[i-len(Neg)]
 
arr = [-0.897, 0.565, 0.656, -0.1234, 0, 0.3434]
sortMixed(arr, len(arr))
print("Posortowana tablica")
print(arr)