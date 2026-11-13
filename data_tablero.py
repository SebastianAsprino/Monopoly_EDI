"""
Lista circular simplemente enlazada para almacenar las casillas del tablero.

El tablero de Monopoly es un recorrido cerrado: después de la última casilla
se vuelve a la salida. Por eso las casillas se guardan en una lista circular,
donde el último nodo apunta de nuevo al primero (``ptr``).
"""

from __future__ import annotations

from typing import Any, Iterator, Optional


class Node:
    """Nodo de la lista circular."""

    def __init__(self, data: Any) -> None:
        """
        Crea un nodo.

        Parámetros:
            data: Dato almacenado en el nodo (por ejemplo, una casilla).
        """
        self.data = data
        self.next: Optional[Node] = None


class ListaCircular:
    """
    Lista circular simplemente enlazada.

    Atributos:
        ptr: Primer nodo de la lista, o ``None`` si está vacía. El último nodo
            siempre apunta a ``ptr``.
    """

    def __init__(self) -> None:
        """Crea una lista vacía."""
        self.ptr: Optional[Node] = None

    def __iter__(self) -> Iterator[Any]:
        """Recorre los datos una sola vuelta, empezando por ``ptr``."""
        nodo = self.ptr
        while nodo is not None:
            yield nodo.data
            nodo = nodo.next
            if nodo is self.ptr:
                break

    def __len__(self) -> int:
        """Retorna la cantidad de nodos."""
        return self.tamano_lista()

    def vacio(self) -> bool:
        """Indica si la lista está vacía."""
        return self.ptr is None

    def tamano_lista(self) -> int:
        """Retorna la cantidad de nodos de la lista."""
        return sum(1 for _ in self)

    def pantalla(self) -> None:
        """Imprime los datos de la lista en orden, separados por flechas."""
        if not self.vacio():
            print(" -> ".join(str(dato) for dato in self))

    def existe(self, data: Any) -> bool:
        """Indica si algún nodo contiene ``data``."""
        return any(dato == data for dato in self)

    def _ultimo(self) -> Node:
        """Retorna el último nodo (el que apunta a ``ptr``). La lista no debe estar vacía."""
        nodo = self.ptr
        while nodo.next is not self.ptr:
            nodo = nodo.next
        return nodo

    def _insertar_en_vacia(self, nodo: Node) -> None:
        """Convierte ``nodo`` en el único elemento de la lista."""
        self.ptr = nodo
        nodo.next = nodo

    def agregar_inicio(self, data: Any) -> None:
        """Agrega un nodo antes del primero; el nuevo nodo pasa a ser ``ptr``."""
        nodo = Node(data)
        if self.vacio():
            self._insertar_en_vacia(nodo)
            return
        ultimo = self._ultimo()
        ultimo.next = nodo
        nodo.next = self.ptr
        self.ptr = nodo

    def agregar_final(self, data: Any) -> None:
        """Agrega un nodo al final de la lista (antes de volver a ``ptr``)."""
        nodo = Node(data)
        if self.vacio():
            self._insertar_en_vacia(nodo)
            return
        ultimo = self._ultimo()
        ultimo.next = nodo
        nodo.next = self.ptr

    def agregar_posicion_especifica(self, indice: int, data: Any) -> bool:
        """
        Inserta un nodo en la posición ``indice`` (0 = inicio, ``len`` = final).

        Retorna:
            ``True`` si se insertó, ``False`` si la posición no es válida.
        """
        tamano = self.tamano_lista()
        if indice < 0 or indice > tamano:
            print("posicion no valida")
            return False
        if indice == 0:
            self.agregar_inicio(data)
        elif indice == tamano:
            self.agregar_final(data)
        else:
            anterior = self.ptr
            for _ in range(indice - 1):
                anterior = anterior.next
            nodo = Node(data)
            nodo.next = anterior.next
            anterior.next = nodo
        return True

    def eliminar_nodo(self, data: Any) -> bool:
        """
        Elimina el primer nodo que contiene ``data``.

        Retorna:
            ``True`` si se eliminó, ``False`` si el dato no estaba en la lista.
        """
        if self.vacio():
            return False

        if self.ptr.data == data:
            if self.ptr.next is self.ptr:
                # Era el único nodo: la lista queda vacía
                self.ptr = None
            else:
                ultimo = self._ultimo()
                ultimo.next = self.ptr.next
                self.ptr = self.ptr.next
            return True

        anterior = self.ptr
        actual = self.ptr.next
        while actual is not self.ptr:
            if actual.data == data:
                anterior.next = actual.next
                return True
            anterior = actual
            actual = actual.next
        return False


def main() -> None:
    """Demostración de la lista circular."""
    lista = ListaCircular()
    lista.agregar_final(2)
    lista.agregar_inicio(1)
    lista.agregar_inicio(0)
    lista.agregar_final(3)
    lista.agregar_posicion_especifica(2, 8)
    lista.pantalla()
    print("Longitud de la lista:", lista.tamano_lista())
    lista.eliminar_nodo(8)
    lista.pantalla()
    print(lista.existe(2))


if __name__ == "__main__":
    main()
