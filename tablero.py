"""
Tablero del juego.

Por ahora pide el número de jugadores (2 a 4) en una ventana de Tkinter. El
dibujo del tablero con pygame está pendiente.
"""

from pathlib import Path
from typing import Optional
import tkinter as tk
from tkinter import ttk

import pygame

RUTA_ICONO = Path(__file__).resolve().parent / "assets" / "logo.ico"
OPCIONES_JUGADORES = ("2", "3", "4")
COLOR_FONDO = "#CBE8E0"
ANCHO_VENTANA = 350
ALTO_VENTANA = 106


def pedir_numero_jugadores() -> Optional[int]:
    """
    Muestra una ventana para elegir el número de jugadores.

    Retorna:
        El número elegido, o ``None`` si se cerró la ventana sin elegir.
    """
    jugadores: Optional[int] = None

    ventana = tk.Tk()
    ventana.title("Jugadores")
    ventana.config(width=ANCHO_VENTANA, height=ALTO_VENTANA, background=COLOR_FONDO)
    try:
        ventana.iconbitmap(str(RUTA_ICONO))
    except tk.TclError:
        # Los iconos .ico solo se soportan en Windows
        pass

    etiqueta = ttk.Label(ventana, text="Numero De Jugadores: ", background=COLOR_FONDO)
    etiqueta.place(x=18, y=20)

    # Caja de selección del número de jugadores
    estilo = ttk.Style(ventana)
    estilo.theme_create(
        "combostyle",
        parent="alt",
        settings={
            "TCombobox": {
                "configure": {
                    "selectbackground": COLOR_FONDO,
                    "fieldbackground": COLOR_FONDO,
                    "background": COLOR_FONDO,
                }
            }
        },
    )
    estilo.theme_use("combostyle")
    cajon = ttk.Combobox(ventana, state="readonly", values=OPCIONES_JUGADORES)
    cajon.place(x=140, y=20)

    def confirmar() -> None:
        """Guarda la opción elegida y cierra la ventana (si no hay opción, no hace nada)."""
        # Aquí se debería anexar el nombre de cada jugador y su turno
        nonlocal jugadores
        valor = cajon.get()
        if not valor:
            return
        jugadores = int(valor)
        print(f"{valor} jugadores")
        ventana.destroy()

    boton = ttk.Button(ventana, text="  ▶  ", command=confirmar)
    boton.place(x=290, y=20)

    ventana.resizable(False, False)
    ventana.mainloop()
    return jugadores


class Tablero:
    """Representación visual del tablero (pendiente de implementar con pygame)."""


def main() -> None:
    """Pide el número de jugadores e inicializa pygame para el tablero."""
    pedir_numero_jugadores()
    # Inicializa todos los módulos de pygame
    pygame.init()


if __name__ == "__main__":
    main()
