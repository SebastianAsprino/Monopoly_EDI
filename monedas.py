"""
Criptomonedas del juego.

En esta versión de Monopoly el dinero son criptomonedas cuyo precio cambia
cada turno de forma aleatoria, imitando la volatilidad del mercado cripto.
"""

import random

# Escenarios de mercado; cada uno tiene la misma probabilidad (estable: 50 %).
MERCADO_ESTABLE = "estable"
MERCADO_BAJISTA = "bajista"
MERCADO_ALCISTA = "alcista"
ESCENARIOS = (MERCADO_ESTABLE, MERCADO_BAJISTA, MERCADO_ALCISTA, MERCADO_ESTABLE)

# En un mercado alcista el precio se multiplica por un factor en este rango.
FACTOR_ALCISTA_MIN = 2.0
FACTOR_ALCISTA_MAX = 10.0
DECIMALES_FACTOR_BAJISTA = 2


class Moneda:
    """Criptomoneda con un precio que cambia cada turno."""

    def __init__(self, valor: float, nombre: str) -> None:
        """
        Crea una moneda.

        Parámetros:
            valor: Precio inicial de una unidad.
            nombre: Símbolo de la moneda (por ejemplo, ``"BTC"``).
        """
        self.valor = valor
        self.nombre = nombre

    def precio_actual(self) -> float:
        """Imprime y retorna el precio actual de la moneda."""
        print(self.valor, self.nombre)
        return self.valor

    def cambiar_precio(self) -> float:
        """
        Cambia el precio según un escenario de mercado aleatorio.

        - Estable: el precio no cambia.
        - Bajista: el precio se multiplica por un factor entre 0 y 1.
        - Alcista: el precio se multiplica por un factor entre 2 y 10.

        Retorna:
            El nuevo precio.
        """
        escenario = random.choice(ESCENARIOS)
        if escenario == MERCADO_BAJISTA:
            self.valor *= round(random.random(), DECIMALES_FACTOR_BAJISTA)
        elif escenario == MERCADO_ALCISTA:
            self.valor *= random.uniform(FACTOR_ALCISTA_MIN, FACTOR_ALCISTA_MAX)
        return self.precio_actual()

    def valor_en_cartera(self, cantidad: float) -> float:
        """
        Imprime y retorna cuánto valen ``cantidad`` unidades de la moneda.

        Parámetros:
            cantidad: Unidades que posee el jugador.
        """
        total = cantidad * self.valor
        print("cuenta con $", total, " en ", self.nombre)
        return total


def main() -> None:
    """Demostración: un jugador con varias monedas antes y después de un cambio de precio."""
    cartera = {
        Moneda(0.70, "ADA"): 600,
        Moneda(100000.0, "BTC"): 1,
        Moneda(1500.0, "ETH"): 400,
        Moneda(0.05, "DOGE"): 8000,
    }

    for moneda, cantidad in cartera.items():
        moneda.valor_en_cartera(cantidad)

    # El precio de las monedas cambia
    for moneda in cartera:
        moneda.cambiar_precio()

    # Valor de la cartera después del cambio
    for moneda, cantidad in cartera.items():
        moneda.valor_en_cartera(cantidad)


if __name__ == "__main__":
    main()
