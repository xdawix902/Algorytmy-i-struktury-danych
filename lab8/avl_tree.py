# -*- coding: utf-8 -*-


class Node():  # Kodujemy pojedynczy węzeł (node) drzewa
    def __init__(self, data=None):
        # data – przechowywana wartość (klucz) w węźle
        self.data = data
        # left  – referencja na lewe poddrzewo
        self.left = None
        # right – referencja na prawe poddrzewo
        self.right = None
        # height – wysokość węzła (potrzebna w AVL do obliczania balansu)
        # Dla pustego węzła (data=None) potraktujemy wysokość jako 0.
        self.height = 1 if data is not None else 0


class AVL():  # W jaki sposób łączymy ze sobą poszczególne węzły w drzewo AVL
    def __init__(self):
        # Na początku tworzymy tylko "pusty" korzeń – tak jak w Twojej klasie BST.
        # Będzie to pojedynczy węzeł z domyślnym data=None.
        self.root = Node()

    # --- POMOCNICZE METODY DO AVL ---

    def _height(self, vertex):
        """Zwraca wysokość węzła. Pusty węzeł ma wysokość 0."""
        if vertex is None:
            return 0
        return vertex.height

    def _get_balance(self, vertex):
        """Zwraca współczynnik zbalansowania (balance factor):
           BF = wysokość(lewego poddrzewa) - wysokość(prawego poddrzewa).
        """
        if vertex is None:
            return 0
        return self._height(vertex.left) - self._height(vertex.right)

    # --- ROTACJE ---

    def _right_rotate(self, y):
        """
        Rotacja w prawo:
                y                         x
               / \                       / \
              x   T3    --->           T1  y
             / \                           / \
            T1  T2                        T2  T3
        """
        x = y.left
        T2 = x.right

        # Wykonanie rotacji
        x.right = y
        y.left = T2

        # Aktualizacja wysokości (najpierw dzieci, potem rodzic)
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        # Zwracamy nowy korzeń poddrzewa
        return x

    def _left_rotate(self, x):
        """
        Rotacja w lewo:
            x                             y
           / \                           / \
          T1  y        --->             x   T3
             / \                       / \
            T2  T3                    T1  T2
        """
        y = x.right
        T2 = y.left

        # Wykonanie rotacji
        y.left = x
        x.right = T2

        # Aktualizacja wysokości
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        # Zwracamy nowy korzeń poddrzewa
        return y

    # --- WSTAWIANIE REKURENCYJNE (JAK W BST, ALE Z RÓWNOWAŻENIEM) ---

    def _insert(self, vertex, data):
        """
        Rekurencyjne wstawianie nowego klucza do drzewa AVL.
        1. Wstawiamy jak do zwykłego BST.
        2. Aktualizujemy wysokość bieżącego węzła.
        3. Sprawdzamy balans i w razie potrzeby wykonujemy odpowiednie rotacje.
        """

        # 1. Jeżeli doszliśmy do pustego miejsca w drzewie – tworzymy nowy węzeł
        if vertex is None:
            return Node(data)

        if data < vertex.data:
            # Idziemy do lewego poddrzewa
            vertex.left = self._insert(vertex.left, data)
        elif data > vertex.data:
            # Idziemy do prawego poddrzewa
            vertex.right = self._insert(vertex.right, data)
        else:
            # Jeśli klucz już istnieje – nic nie robimy (brak duplikatów)
            return vertex

        # 2. Aktualizacja wysokości bieżącego węzła
        vertex.height = 1 + max(self._height(vertex.left),
                                self._height(vertex.right))

        # 3. Sprawdzenie współczynnika balansu
        balance = self._get_balance(vertex)

        # --- PRZYPADKI ROTACJI ---

        # Przypadek LL (Left-Left): przechylenie w lewo, nowy element w lewym-lewym poddrzewie
        if balance > 1 and data < vertex.left.data:
            return self._right_rotate(vertex)

        # Przypadek RR (Right-Right): przechylenie w prawo, nowy element w prawym-prawym poddrzewie
        if balance < -1 and data > vertex.right.data:
            return self._left_rotate(vertex)

        # Przypadek LR (Left-Right): przechylenie w lewo, a nowy element w lewym-prawym poddrzewie
        if balance > 1 and data > vertex.left.data:
            vertex.left = self._left_rotate(vertex.left)
            return self._right_rotate(vertex)

        # Przypadek RL (Right-Left): przechylenie w prawo, a nowy element w prawym-lewym poddrzewie
        if balance < -1 and data < vertex.right.data:
            vertex.right = self._right_rotate(vertex.right)
            return self._left_rotate(vertex)

        # Jeżeli nie trzeba rotować – zwracamy niezmieniony węzeł
        return vertex

    # --- METODY PUBLICZNE  ---

    def insert(self, data):
        """
        Publiczna metoda wstawiania – interfejs identyczny jak w BST.
        Użytkownik wywołuje:
            tree.insert(klucz)
        i nie musi wiedzieć, że w środku jest AVL.
        """
        # Specjalny przypadek dla "pustego" korzenia (tak jak w Twojej klasie BST).
        if self.root.data is None:
            self.root.data = data
            self.root.height = 1
        else:
            # Jeśli korzeń ma już wartość, wstawiamy rekursywnie do drzewa AVL.
            self.root = self._insert(self.root, data)

    def display(self):
        """
        Wypisuje trzy standardowe przejścia drzewa:
        1. ROOT-LEFT-RIGHT (preorder, VLR)
        2. LEFT-ROOT-RIGHT (inorder, LVR)
        3. LEFT-RIGHT-ROOT (postorder, LRV)
        """
        result = ""

        # ROOT-LEFT-RIGHT (preorder, VLR)
        def vlr(result, vertex):
            if vertex is not None and vertex.data is not None:
                result += str(vertex.data) + "-"
                result = vlr(result, vertex.left)
                result = vlr(result, vertex.right)
            return result

        # LEFT-ROOT-RIGHT (inorder, LVR)
        def lvr(result, vertex):
            if vertex is not None and vertex.data is not None:
                result = lvr(result, vertex.left)
                result += str(vertex.data) + "-"
                result = lvr(result, vertex.right)
            return result

        # LEFT-RIGHT-ROOT (postorder, LRV)
        def lrv(result, vertex):
            if vertex is not None and vertex.data is not None:
                result = lrv(result, vertex.left)
                result = lrv(result, vertex.right)
                result += str(vertex.data) + "-"
            return result

        print(vlr(result, self.root))
        print(lvr(result, self.root))
        print(lrv(result, self.root))


tree = AVL()
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(8)
tree.insert(7)
tree.insert(99)

tree.display()