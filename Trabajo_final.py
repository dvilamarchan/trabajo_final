# Clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# Clase Árbol Binario
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    # Recorrido Inorder
    def inorder(self, nodo):
        if nodo:
            self.inorder(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorder(nodo.derecho)

    # Recorrido Preorder
    def preorder(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorder(nodo.izquierdo)
            self.preorder(nodo.derecho)

    # Recorrido Posorder
    def posorder(self, nodo):
        if nodo:
            self.posorder(nodo.izquierdo)
            self.posorder(nodo.derecho)
            print(nodo.valor, end=" ")


# Programa principal
arbol = ArbolBinario()
datos = [50, 30, 70, 20, 40, 60, 80]

for dato in datos:
    arbol.insertar(dato)

print("Recorrido Inorder:")
arbol.inorder(arbol.raiz)

print("\nRecorrido Preorder:")
arbol.preorder(arbol.raiz)

print("\nRecorrido Posorder:")
arbol.posorder(arbol.raiz)
