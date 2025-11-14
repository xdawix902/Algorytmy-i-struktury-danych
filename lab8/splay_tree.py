# -*- coding: utf-8 -*-


class Node():  # kodujemy pojedynczy wezel drzewa
    def __init__(self, data=None):
        # data – przechowywana wartosc (klucz) w wezle
        self.data = data
        # left  – lewe poddrzewo
        self.left = None
        # right – prawe poddrzewo
        self.right = None
        # parent – rodzic (potrzebny do operacji splay)
        self.parent = None


class Splay():  # drzewo splay (samoczynnie "podciaga" uzywane wezly do korzenia)
    def __init__(self):
        # Na poczatku tworzymy tylko "pusty" korzen – tak jak w Twoim BST.
        # Jest to wezel z data=None, ktorego nie traktujemy jako normalny element drzewa.
        self.root = Node()

    # ======================= POMOCNICZE FUNKCJE =======================

    def _is_left_child(self, node):
        """Sprawdza, czy dany wezel jest lewym dzieckiem swojego rodzica."""
        return node.parent is not None and node.parent.left == node

    def _left_rotate(self, x):
        """
        Rotacja w lewo wokol wezla x.

            x                             y
           / \                           / \
          A   y        --->             x   C
             / \                       / \
            B   C                     A   B
        """
        y = x.right
        if y is None:
            return  # brak prawego dziecka – nie da sie zrobic rotacji

        # przenosimy lewe dziecko y jako prawe dziecko x
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        # przepinamy rodzica y
        y.parent = x.parent
        if x.parent is None:
            # x byl korzeniem – po rotacji korzeniem zostaje y
            self.root = y
        else:
            if self._is_left_child(x):
                x.parent.left = y
            else:
                x.parent.right = y

        # przestawiamy wskazniki x <-> y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        """
        Rotacja w prawo wokol wezla y.

                y                         x
               / \                       / \
              x   C      --->           A   y
             / \                           / \
            A   B                         B   C
        """
        x = y.left
        if x is None:
            return  # brak lewego dziecka – nie da sie zrobic rotacji

        # przenosimy prawe dziecko x jako lewe dziecko y
        y.left = x.right
        if x.right is not None:
            x.right.parent = y

        # przepinamy rodzica x
        x.parent = y.parent
        if y.parent is None:
            # y byl korzeniem – po rotacji korzeniem zostaje x
            self.root = x
        else:
            if self._is_left_child(y):
                y.parent.left = x
            else:
                y.parent.right = x

        # przestawiamy wskazniki x <-> y
        x.right = y
        y.parent = x

    # ======================= OPERACJA SPLAY =======================

    def _splay(self, node):
        """
        Kluczowa operacja w Splay Tree.
        "Podciaga" dany wezel (node) do korzenia poprzez sekwencje rotacji:
        - zig      – pojedyncza rotacja, gdy rodzic jest korzeniem
        - zig-zig  – dwie rotacje w tym samym kierunku
        - zig-zag  – dwie rotacje w roznych kierunkach
        """
        while node.parent is not None:
            # Jezeli rodzic jest korzeniem – przypadek ZIG
            if node.parent.parent is None:
                if self._is_left_child(node):
                    # node jest lewym dzieckiem – rotacja w prawo wokol rodzica
                    self._right_rotate(node.parent)
                else:
                    # node jest prawym dzieckiem – rotacja w lewo wokol rodzica
                    self._left_rotate(node.parent)
            else:
                # Jezeli rodzic nie jest korzeniem – przypadki ZIG-ZIG albo ZIG-ZAG
                parent = node.parent
                grand = parent.parent

                # ----- Przypadek ZIG-ZIG (ten sam kierunek) -----

                # lewo-lewo
                if self._is_left_child(node) and self._is_left_child(parent):
                    # najpierw rotacja w prawo wokol dziadka,
                    # potem rotacja w prawo wokol rodzica (ktory po 1. rotacji jest juz wyzej)
                    self._right_rotate(grand)
                    self._right_rotate(parent)

                # prawo-prawo
                elif (not self._is_left_child(node)) and (not self._is_left_child(parent)):
                    # analogicznie: dwie rotacje w lewo
                    self._left_rotate(grand)
                    self._left_rotate(parent)

                # ----- Przypadek ZIG-ZAG (rozne kierunki) -----

                # lewo-prawo
                elif self._is_left_child(node) and (not self._is_left_child(parent)):
                    # najpierw rotacja w prawo wokol rodzica,
                    # potem rotacja w lewo wokol dziadka
                    self._right_rotate(parent)
                    self._left_rotate(grand)

                # prawo-lewo
                else:
                    # najpierw rotacja w lewo wokol rodzica,
                    # potem rotacja w prawo wokol dziadka
                    self._left_rotate(parent)
                    self._right_rotate(grand)

    # ======================= WSTAWIANIE =======================

    def insert(self, data):
        """
        Publiczna metoda wstawiania – interfejs identyczny jak w BST/AVL/RBT.
        Uzycie:
            tree = Splay()
            tree.insert(klucz)

        Dodatkowo po wstawieniu wykonujemy splay na nowym wezle, czyli
        podciagamy go do korzenia.
        """
        # Specjalny przypadek: drzewo jest "puste" (korzen ma data=None) – jak w Twoim BST
        if self.root.data is None:
            self.root.data = data
            # root.parent = None juz jest, rotacji nie potrzeba
            return

        # Wstawiamy jak do zwyklego BST (bez splay), ale pilnujemy parent
        current = self.root
        parent = None

        while current is not None:
            if current.data is None:
                break
            parent = current
            if data < current.data:
                if current.left is None:
                    break
                current = current.left
            elif data > current.data:
                if current.right is None:
                    break
                current = current.right
            else:
                # Jezeli wartosc juz jest w drzewie – splay na istniejacym wezle
                self._splay(current)
                return

        # Tworzymy nowy wezel
        new_node = Node(data)
        new_node.parent = parent

        # Przypinamy jako lewe lub prawe dziecko
        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # Po wstawieniu splayujemy nowy wezel – trafia do korzenia
        self._splay(new_node)

    # ======================= WYSWIETLANIE (TAK JAK W BST) =======================

    def display(self):
        """
        Wypisuje trzy przejscia drzewa:
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


# ======================= PRZYKLADOWE UZYCIE =======================

if __name__ == "__main__":
    tree = Splay()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(8)
    tree.insert(7)
    tree.insert(99)

    tree.display()