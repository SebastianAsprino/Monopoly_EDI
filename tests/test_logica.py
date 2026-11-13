"""Pruebas unitarias de la lista circular y de las monedas.

Ejecutar desde la raíz del repositorio:

    python -m unittest discover -s tests
"""

import contextlib
import io
import random
import unittest

from data_tablero import ListaCircular
from monedas import FACTOR_ALCISTA_MAX, Moneda


def silencioso(funcion, *args):
    """Ejecuta ``funcion`` ocultando lo que imprime en consola."""
    with contextlib.redirect_stdout(io.StringIO()):
        return funcion(*args)


class TestListaCircular(unittest.TestCase):
    def crear(self, *datos):
        lista = ListaCircular()
        for dato in datos:
            lista.agregar_final(dato)
        return lista

    def test_lista_nueva_esta_vacia(self):
        lista = ListaCircular()
        self.assertTrue(lista.vacio())
        self.assertEqual(lista.tamano_lista(), 0)

    def test_agregar_inicio_y_final(self):
        lista = ListaCircular()
        lista.agregar_final(2)
        lista.agregar_inicio(1)
        lista.agregar_final(3)
        self.assertEqual(list(lista), [1, 2, 3])

    def test_es_circular(self):
        lista = self.crear(1, 2, 3)
        self.assertIs(lista._ultimo().next, lista.ptr)

    def test_agregar_posicion_especifica(self):
        lista = self.crear(0, 1, 2, 3)
        self.assertTrue(silencioso(lista.agregar_posicion_especifica, 2, 8))
        self.assertTrue(silencioso(lista.agregar_posicion_especifica, 5, 9))
        self.assertEqual(list(lista), [0, 1, 8, 2, 3, 9])

    def test_posicion_invalida(self):
        lista = self.crear(1)
        self.assertFalse(silencioso(lista.agregar_posicion_especifica, 5, 9))
        self.assertFalse(silencioso(lista.agregar_posicion_especifica, -1, 9))
        self.assertEqual(list(lista), [1])

    def test_eliminar(self):
        lista = self.crear(1, 2, 3)
        self.assertTrue(lista.eliminar_nodo(1))
        self.assertTrue(lista.eliminar_nodo(3))
        self.assertEqual(list(lista), [2])

    def test_eliminar_unico_nodo_vacia_la_lista(self):
        lista = self.crear(1)
        self.assertTrue(lista.eliminar_nodo(1))
        self.assertTrue(lista.vacio())

    def test_eliminar_inexistente_no_cuelga(self):
        lista = self.crear(1, 2)
        self.assertFalse(lista.eliminar_nodo(99))
        self.assertEqual(list(lista), [1, 2])

    def test_existe(self):
        lista = self.crear("salida", "carcel")
        self.assertTrue(lista.existe("carcel"))
        self.assertFalse(lista.existe("parqueadero"))


class TestMoneda(unittest.TestCase):
    def test_valor_en_cartera(self):
        moneda = Moneda(1500.0, "ETH")
        self.assertEqual(silencioso(moneda.valor_en_cartera, 2), 3000.0)

    def test_cambiar_precio_queda_en_rango(self):
        random.seed(0)
        for _ in range(200):
            moneda = Moneda(100.0, "BTC")
            nuevo = silencioso(moneda.cambiar_precio)
            self.assertEqual(nuevo, moneda.valor)
            self.assertGreaterEqual(nuevo, 0.0)
            self.assertLessEqual(nuevo, 100.0 * FACTOR_ALCISTA_MAX)


if __name__ == "__main__":
    unittest.main()
