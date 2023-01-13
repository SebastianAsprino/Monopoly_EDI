class Node:
    ## crear nodo
	def __init__(self, data):
		## dato en el nodo
		self.data = data

		## siguiente espacio en memoria
		self.next = None
class LinkedList:
    
    def __init__(self):
        self.PTR = None
    
    def vacio(self):
        ## revisa si la lista circular esta vacia
        return self.PTR is None

    def tamaño_lista(self):
        ## saer tamaño de la lista
        nodito = self.PTR
        contador = 0
        ##revisa si el nodo siguiente al actual es el principal
        while nodito is not None:
            contador += 1
            if nodito.next == self.PTR:
                break
            else:
                nodito = nodito.next
        return contador
    
    def pantalla(self):
        ## recorrer la lista circular
        if self.vacio():
            return
        nodito = self.PTR
        print(nodito.data)
        while nodito.next != self.PTR:
            nodito = nodito.next
            print(nodito.data, end='->')
    
    def agregar_PTR(self, data):
        ## agregar un nodo antes de primero y este siendo ahora el primero
        nodo = Node(data)
        if self.vacio():
            self.PTR = nodo
            nodo.next = self.PTR
        else:
            nodito = self.PTR
            while nodito.next is not self.PTR:
                nodito = nodito.next
            nodito.next = nodo
            nodo.next   = self.PTR
            self.PTR    = nodo

    def agregar_ULT(self, data):
        ## agregar nodo al final "ULT" y luego este ser el ultimo "ULT"
        nodo = Node(data)
        if self.vacio():
            self.PTR = nodo
            nodo.next = self.PTR
        else:
            nodito = self.PTR
            while nodito.next is not self.PTR:
                nodito = nodito.next
            nodito.next = nodo
            nodo.next = self.PTR

    def agregar_posicion_especifica(self, indice,data):
        ## egragar nodo en una posicion especifica
        nodo = Node(data)
        if indice < 0 or indice > self.length():
            print("posicion no valida")
            return False
        elif indice == 0:
            self.agregar_PTR(data)
        elif indice == 0:
            self.agregar_ULT()
        else:
            nodito = self.PTR
            pre = None
            count = 0

            while count < indice:
                pre = nodito
                nodito = nodito.next
                count += 1
            pre.next = nodo
            nodo.next = nodito

    def eliminar_nodo(self, data):
        ## eliminar el nodo 
        if self.vacio():
            return
        elif data == self.PTR.data:
            nodito = self.PTR
            while nodito.next != self.PTR:
                nodito = nodito.next
            nodito.next = self.PTR.next
            self.PTR = self.PTR.next
        else:
            nodito = self.PTR
            pre= None
            while nodito.data != data:
                pre = nodito
                nodito = nodito.next
            pre.next = nodito.next
    """def is_exist(self, data):
            "" "Buscar si el nodo especificado existe" ""
        cur = self.head
        while cur is not None:
                    # Encuentra el nodo encontrado
            if cur.data == data:
                return True
                    # La cola ha sido encontrada
            elif cur.next == self.head:
                return False
            else:
                cur = cur.next
        return False"""








if __name__ == '__main__':
    lists = LinkedList()
    lists.agregar_ULT(2)
    lists.agregar_PTR(1)
    lists.agregar_PTR(0)
    lists.agregar_ULT(3)
    lists.insert_node(2, 8)
    lists.travel()
    print ("Longitud de la lista:", lists.length ())
    lists.remove_node(8)
    lists.travel()
    print(lists.is_exist(2))