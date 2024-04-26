import random
class monedas:
    """crea las monedas y permite modificar su valor cada turno"""
    
    def __init__ (self, valor, nombre): ##sd
        self.valor = valor
        self.nombre = nombre
    def precioactual(self):
        return print(self.valor, self.nombre)

    def cambioprecio(self):
        mercado = None
        porcentaje_de_cambio = None
        mercado = random.randint(0,3)
        if mercado == 0:
            self.valor = self.valor
            print(self.valor, self.nombre)
        if mercado == 1:
            porcentaje_de_cambio = round(random.random(),2)
            self.valor = self.valor * porcentaje_de_cambio
            print(self.valor, self.nombre)
        if mercado == 2:
            porcentaje_de_cambio = random.uniform(2.0,10.0)
            ## random.randint(2,50) la segunda implementacio no usaba float
            self.valor = self.valor * porcentaje_de_cambio
            print(self.valor, self.nombre)
    def pruebavalor (self,posee):

        esto_vale = posee * self.valor
        return print( 'cuenta con $',esto_vale,' en ', self.nombre)





if __name__ == '__main__':
    bitcoin = monedas(100000.0, 'BTC')
    cardano = monedas(0.70, 'ADA')
    ethereum = monedas(1500.0, 'ETH')
    doge = monedas(0.05, 'DOGE')
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

    wallet_btc  = 1
    wallet_ada  = 600
    wallet_eth  = 400
    wallet_doge = 8000
    cardano.pruebavalor(wallet_ada)
    bitcoin.pruebavalor(wallet_btc)
    ethereum.pruebavalor(wallet_eth)
    doge.pruebavalor(wallet_doge)
## probamos que el precio de estas monedas cambia
    cardano.cambioprecio()
    bitcoin.cambioprecio()
    ethereum.cambioprecio()
    doge.cambioprecio()
    ## ahora confirmamos cuanto tiene el usuario
    cardano.pruebavalor(wallet_ada)
    bitcoin.pruebavalor(wallet_btc)
    ethereum.pruebavalor(wallet_eth)
    doge.pruebavalor(wallet_doge)

