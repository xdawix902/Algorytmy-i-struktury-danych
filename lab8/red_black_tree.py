# -*- coding: utf-8 -*-


class Node:  # pojedynczy węzeł drzewa Red-Black
    def __init__(self, data=None):
        # data – przechowywana wartość (klucz) w węźle
        self.data = data

        # wskaźniki na dzieci
        self.left = None
        self.right = None

        # wskaźnik na rodzica – potrzebny przy naprawianiu własności RBT
        self.parent = None

        # kolor węzła: "R" (red) albo "B" (black)
        # Domyślnie nowy węzeł (z danymi) będzie czerwony.
        # Gdy data=None, potraktujemy taki węzeł jak "pusty" i kolor nie ma większego znaczenia.
        self.color = "R"


class RBT:  # Red-Black Tree
    def __init__(self):
        # Na początku tworzymy "pusty" korzeń – tak jak w Twoim BST/AVL.
        # Będzie to węzeł z data=None, którego NIE traktujemy jako normalnego elementu drzewa.
        self.root = Node()
        self.root.color = "B"  # korzeń jako czarny (nawet pusty)

    # --- ROTACJE (BARDZO WAŻNE W RBT) ---

    def _left_rotate(self, x):
        """
        Rotacja w lewo wokół węzła x.

            x                             y
           / \                           / \
          A   y        --->             x   C
             / \                       / \
            B   C                     A   B

        Gdzie A, B, C to (potencjalnie) całe poddrzewa.
        """
        y = x.right
        if y is None:
            # brak prawego dziecka – nie da się rotować
            return

        # przenosimy lewe dziecko y jako prawe dziecko x
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        # przepinamy rodzica y
        y.parent = x.parent
        if x.parent is None:
            # x był korzeniem – po rotacji korzeniem zostaje y
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # przestawiamy wskaźniki x <-> y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        """
        Rotacja w prawo wokół węzła y.

                y                         x
               / \                       / \
              x   C      --->           A   y
             / \                           / \
            A   B                         B   C
        """
        x = y.left
        if x is None:
            # brak lewego dziecka – nie da się rotować
            return

        # przenosimy prawe dziecko x jako lewe dziecko y
        y.left = x.right
        if x.right is not None:
            x.right.parent = y

        # przepinamy rodzica x
        x.parent = y.parent
        if y.parent is None:
            # y był korzeniem – po rotacji korzeniem zostaje x
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        # przestawiamy wskaźniki x <-> y
        x.right = y
        y.parent = x

    # --- WSTAWIANIE JAK DO ZWYKŁEGO BST (BEZ KOLORÓW) ---

    def _bst_insert(self, data):
        """
        Proste wstawianie jak do zwykłego BST.
        Zwraca nowo utworzony węzeł (czerwony), który następnie
        będziemy "naprawiać" zgodnie z regułami Red-Black.
        """

        # Jeżeli korzeń jest "pusty" (data=None), to po prostu wpisujemy tam dane.
        if self.root.data is None:
            self.root.data = data
            self.root.color = "B"  # korzeń zawsze czarny
            return self.root

        # W przeciwnym razie szukamy miejsca w drzewie jak w BST.
        current = self.root
        parent = None

        while current is not None and current.data is not None:
            parent = current
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                # zakładamy brak duplikatów – nie wstawiamy powtórek
                return current

        # Tworzymy nowy węzeł (standardowo czerwony)
        new_node = Node(data)
        new_node.color = "R"
        new_node.parent = parent

        # Podpinamy go jako lewe albo prawe dziecko
        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        return new_node

    # --- NAPRAWA WŁASNOŚCI DRZEWA RED-BLACK PO WSTAWIENIU ---

    def _fix_insert(self, node):
        """
        Naprawia własności drzewa czerwono-czarnego po wstawieniu nowego czerwonego węzła.

        Główne przypadki (symetryczne dla "wujka" po lewej/prawej stronie):
        1) Rodzic i wujek są czerwoni → przemalowanie (recoloring).
        2) Wujek czarny, a nowy węzeł jest "wewnętrznym" dzieckiem → rotacja,
           aby sprowadzić do przypadku 3.
        3) Wujek czarny, a nowy węzeł jest "zewnętrznym" dzieckiem → rotacja + recolor.
        """
        # Dopóki rodzic jest czerwony (a więc narusza regułę:
        # "czerwony węzeł nie może mieć czerwonego rodzica")
        while node != self.root and node.parent.color == "R":
            # Sprawdzamy, czy rodzic jest lewym czy prawym dzieckiem dziadka
            if node.parent == node.parent.parent.left:
                # Wujek to prawe dziecko dziadka
                uncle = node.parent.parent.right

                # --- Przypadek 1: wujek jest czerwony – RECOLORING ---
                if uncle is not None and uncle.color == "R":
                    # Przemalowujemy rodzica i wujka na czarno,
                    # dziadka na czerwono, i przesuwamy się w górę.
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    # Wujek jest czarny lub nie istnieje

                    # --- Przypadek 2: node jest prawym dzieckiem (układ lewo-prawo) ---
                    if node == node.parent.right:
                        # Rotujemy w lewo wokół rodzica, żeby przejść do układu lewo-lewo
                        node = node.parent
                        self._left_rotate(node)

                    # --- Przypadek 3: node jest lewym dzieckiem (układ lewo-lewo) ---
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self._right_rotate(node.parent.parent)

            else:
                # Druga strona – rodzic jest prawym dzieckiem dziadka
                uncle = node.parent.parent.left

                # --- Przypadek 1 (symetryczny): wujek czerwony ---
                if uncle is not None and uncle.color == "R":
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    # --- Przypadek 2 (symetryczny): układ prawo-lewo ---
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)

                    # --- Przypadek 3 (symetryczny): układ prawo-prawo ---
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self._left_rotate(node.parent.parent)

        # Na końcu pilnujemy, żeby korzeń zawsze był czarny
        self.root.color = "B"

    # --- METODY PUBLICZNE: INTERFEJS TAKI SAM JAK W BST/AVL ---

    def insert(self, data):
        """
        Publiczna metoda wstawiania.
        Użytkownik wywołuje:

            tree = RBT()
            tree.insert(klucz)

        i nie musi wiedzieć, że "w środku" działa złożony mechanizm RBT.
        """
        # Najpierw wstawiamy element jak do zwykłego BST (zwraca nowy węzeł)
        new_node = self._bst_insert(data)

        # Jeżeli to był pierwszy węzeł (korzeń), nic więcej nie trzeba robić
        if new_node == self.root:
            self.root.color = "B"  # korzeń czarny
            return

        # W przeciwnym razie naprawiamy własności drzewa czerwono-czarnego
        self._fix_insert(new_node)

    def display(self):
        """
        Wypisuje trzy przejścia (tak jak w Twoim BST/AVL):
        1. ROOT-LEFT-RIGHT (preorder, VLR)
        2. LEFT-ROOT-RIGHT (inorder, LVR)
        3. LEFT-RIGHT-ROOT (postorder, LRV)

        Używamy tego samego formatu z "-" pomiędzy wartościami.
        """
        result = ""

        # ROOT-LEFT-RIGHT (preorder, VLR)
        def vlr(result, vertex):
            # Sprawdzamy, czy węzeł istnieje i ma realne dane
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


# --- PRZYKŁADOWE UŻYCIE ---

if __name__ == "__main__":
    tree = RBT()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(8)
    tree.insert(7)
    tree.insert(99)

    tree.display()