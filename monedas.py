import random
class monedas:
    """crea las monedas y permite modificar su valor cada turno"""
    
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
    def pruebavalor (self,posee):

        esto_vale = posee * self.valor
        return print( 'cuenta con $',esto_vale,' en ', self.nombre)





if __name__ == '__main__':
    bitcoin = monedas(100000, 'btc')
    cardano = monedas(0.70, 'ada')
    ethereum = monedas(1500, 'eth')
##    bitcoin.precioactual()
##    cardano.precioactual()
##    ethereum.precioactual()
##    bitcoin.cambioprecio()
##    cardano.cambioprecio()
##    ethereum.cambioprecio()
##    bitcoin.precioactual()
##    cardano.precioactual()
##    ethereum.precioactual()

    ## emulo un jugador que tiene x cantidad de cada ejemplo

    wallet_btc= 1
    wallet_ada= 600
    wallet_eth= 400
    cardano.pruebavalor(wallet_ada)
    bitcoin.pruebavalor(wallet_btc)
    ethereum.pruebavalor(wallet_eth)
## probamos que el precio de estas monedas cambia
    cardano.cambioprecio()
    bitcoin.cambioprecio()
    ethereum.cambioprecio()
    ## ahora confirmamos cuanto tiene el usuario
    cardano.pruebavalor(wallet_ada)
    bitcoin.pruebavalor(wallet_btc)
    ethereum.pruebavalor(wallet_eth)

