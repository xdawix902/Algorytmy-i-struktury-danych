class Node(): #kodujemy pojedynczy wezel
    def __init__(self, data=None): # 
#Metoda __init__ jest podobna do konstruktorów w C++ i Javie.
#Konstruktory służą do inicjalizacji stanu obiektu.
#Zadaniem konstruktorów jest inicjalizowanie (przypisywanie wartości) członkom danych klasy w momencie tworzenia obiektu tej klasy.
#Podobnie jak metody, konstruktor zawiera zbiór instrukcji (czyli poleceń), które są wykonywane w chwili tworzenia obiektu.
#Uruchamia się on natychmiast po utworzeniu instancji klasy.
#Metoda ta jest przydatna do wykonania wszelkiej inicjalizacji, jaką chcemy przeprowadzić dla naszego obiektu.

        self.data = data
        self.left = None
        self.right = None

class BST(): #w jaki sposob laczymy ze soba poszczgolne wezly
    def __init__(self):
        self.root = Node() #na poczatku tworze tylko korzen ktore jest pojedynczym wezlem z domyslnymi wartosciami
        
    def insert(self, data):
        if self.root.data == None: #jesli jeszcze niczego nie dostawilismy, tzn. korzen jest pusty
            self.root.data = data #pierwsza liczba ma trafic do korzenia
        else: #we wszystkich pozostalych przypadkach (jesli korzen juz jest zapelniony) to musimy poszukac odpowiedniego miejsca gdzie chcemy wstawic dane
            def insert_to_vertex(data, vertex): #do tego uzywamy funkcji pomocniczej wewnetrznej; 
                #robie funkcje w funkcji bo jak bede wywolywal metode na obiekcie insert to ja tylko chce przekazac dane
                if data < vertex.data:
                    if vertex.left == None:
                        vertex.left = Node(data)
                    else:
                        insert_to_vertex(data, vertex.left)
                if data > vertex.data:
                    if vertex.right == None:
                        vertex.right = Node(data)
                    else:
                        insert_to_vertex(data, vertex.right)
            insert_to_vertex(data, self.root) #wywolanie funkcji pomocniczej (pierwszy rozpatrywany wierzcholek to korzen)
    def display(self):
        result = "" #wynik to zmienna do której będę zbierał po kolei wszystkie dane z węzłów
                    #w zależnosci od tego ktore przechodzenie bedziemy realizowali to w tym węźle zaczniemy
                    #zabierzemy jego wartosc, wstawimy do wyniku i będziemy dostawiali nastepne
        def vlr(result, vertex):#kazda z metod przechodzenia zrealizujemy przy pomocy konkretnej funkcji; 
                                #to beda funkcje wewnetrzne dla metody display
            if vertex: #sprawdzamy czy w ogole ten wierzcholek istnieje, czy to nie jest juz None (czy nie doszlismy na krawedz)
                if vertex.data: #czy cos jest w nim w srodku
                    result += str(vertex.data) + "-" #zamieniam klucz wezla na stringa i wrzucam do result (wartosci beda oddzielone od siebie -)
                    result = vlr(result,vertex.left)
                    result = vlr(result,vertex.right)
            return result
        
        def lvr(result, vertex):
            if vertex:
                if vertex.data:
                    result = lvr(result, vertex.left)
                    result += str(vertex.data) + "-"
                    result = lvr(result, vertex.right)
            return result
        def lrv(result, vertex):
            if vertex:
                if vertex.data:
                    result = lrv(result, vertex.left)
                    result = lrv(result, vertex.right)
                    result += str(vertex.data) + "-"
            return result
        print(vlr(result, self.root))
        print(lvr(result, self.root))
        print(lrv(result, self.root))
tree = BST()
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(8)
tree.insert(7)
tree.insert(99)

tree.display()