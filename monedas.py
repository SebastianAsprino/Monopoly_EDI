import random
class monedas:
    """crea las monedas"""
    def __init__ (self, valor, nombre):
        self.valor = valor
        self.nombre = nombre
    def precioactual(self):
        return print(self.valor, self.nombre)

    def cambioprecio(self):
        mercado = None
        mercado = random.randint(0,2)
        if mercado == 0:
            self.valor = self.valor
            print(self.valor, self.nombre)
        if mercado == 1:
            self.valor = self.valor * 0.20
            print(self.valor, self.nombre)
        if mercado == 2:
            self.valor = self.valor * 3
            print(self.valor, self.nombre)




##print(bitcoin.cambioprecio) 



if __name__ == '__main__':
    bitcoin = monedas(100000, 'btc')
    cardano = monedas(0.70, 'ada')
    ethereum = monedas(1500, 'eth')
    bitcoin.precioactual()
    cardano.precioactual()
    ethereum.precioactual()
    bitcoin.cambioprecio()
    cardano.cambioprecio()
    ethereum.cambioprecio()
    bitcoin.precioactual()
    cardano.precioactual()
    ethereum.precioactual()





