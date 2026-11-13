# Monopoly EDI — Monopoly cripto en Python

Proyecto del curso **Estructuras de Datos I**: una versión de Monopoly en Python donde el
tablero se modela con una **lista circular enlazada** y el dinero son **criptomonedas** cuyo
precio sube o baja cada turno.

> Estado: proyecto académico **en desarrollo**. Ya están implementadas la lista circular del
> tablero, las monedas con precio variable y la ventana de selección de jugadores; el resto
> del juego está planeado (ver [Avance](#avance)).

## Funcionalidades implementadas

- **Lista circular enlazada** (`data_tablero.py`): insertar al inicio, al final o en una
  posición, eliminar, buscar, recorrer e imprimir. El último nodo apunta al primero, como el
  recorrido cerrado del tablero.
- **Criptomonedas con precio variable** (`monedas.py`): cada turno el mercado puede estar
  estable (sin cambio), bajista (el precio se multiplica por un factor entre 0 y 1) o alcista
  (factor entre 2 y 10). Calcula el valor de la cartera de un jugador.
- **Selección del número de jugadores** (`tablero.py`): ventana de Tkinter para elegir entre
  2 y 4 jugadores.
- **Pruebas unitarias** (`tests/`) para la lista circular y las monedas.

## Reglas del juego (diseño)

- Usar listas enlazadas para tener la información del tablero.
- Cada propiedad debe tener nombre, valor de venta y valor de renta.
- Cada jugador es un objeto.
- Mínimo 2 y máximo 4 jugadores (el banco no es un jugador); el orden se define con los dados.
- 2 dados de 1 a 6 se lanzan de forma aleatoria y determinan el movimiento y la salida de la
  cárcel.
- Las cartas de cofre y suerte se leen desde archivos.
  - Cofre: recibir o dar dinero a jugadores o al banco.
  - Suerte: recibir o dar dinero a jugadores o al banco, pase libre de la cárcel o ir a la
    cárcel.
- Las cartas se seleccionan de forma aleatoria y el jugador solo conserva la de salir de la
  cárcel.
- Cada vez que un jugador cae en una propiedad, el programa le pregunta si la compra; si es de
  otro jugador debe pagar renta.

**Consideraciones**

- El banquero es el programa: tiene todas las cartas y dinero infinito.
- Al pasar por la salida paga 200 al jugador, repartidos entre las 8 monedas; el jugador elige
  cuál.
- Cobra impuestos cada vez que una carta de suerte o cofre lo pida.
- La cárcel es obligatoria.
- No hay casas, hoteles ni subastas.
- **El juego termina cuando todos los jugadores, excepto uno, están en bancarrota.**

## Estructura del proyecto

```
Monopoly_EDI/
├── data_tablero.py      # Node y ListaCircular: estructura de datos del tablero
├── monedas.py           # Moneda: criptomonedas con precio variable
├── tablero.py           # Ventana de número de jugadores; tablero con pygame (pendiente)
├── prision.py           # Lógica de la cárcel (pendiente)
├── datos_tablero.txt    # Datos de las casillas del tablero (pendiente)
├── prueba_monedas.txt   # Registro de ejecuciones manuales de monedas.py
├── assets/logo.ico      # Icono de la ventana
├── test/                # Prototipos de ventanas en Tkinter
├── tests/               # Pruebas unitarias (unittest)
└── requirements.txt
```

## Requisitos

- Python 3.8 o superior, con Tkinter.
- `pygame` (ver `requirements.txt`).

## Cómo ejecutar

```bash
python -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install -r requirements.txt

python tablero.py        # ventana de selección de jugadores
python monedas.py        # demostración del cambio de precio de las monedas
python data_tablero.py   # demostración de la lista circular

python -m unittest discover -s tests   # pruebas unitarias
```

## Avance

- ✅ Completado · 💠 Trabajando en ello · ❌ Por hacer

- [💠 ASPRINO] Tablero de juego
- [❌ ASPRINO] Carga de los datos del tablero
- [✅ ASPRINO] Hacer que el precio de las monedas cambie (05-11-2022)
- [❌ SOLAEZ] Jugadores
- [❌ SOLAEZ] Dado
- [❌ SOLAEZ] Movimiento de jugadores
- [❌] Cartas *PUMP* (cartas positivas con efecto al alza en las monedas; pueden dar la carta de
  salir de la cárcel, pero no la de ir a ella)
- [❌] Cartas *DUMP* (cartas negativas con efecto a la baja en las monedas)
- [❌] La cárcel
