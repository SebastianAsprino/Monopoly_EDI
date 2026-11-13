"""Prototipo de Tkinter: ventana con un saludo y un botón para salir."""

import tkinter as tk
from tkinter import ttk


def main() -> None:
    """Abre la ventana de prueba."""
    root = tk.Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


if __name__ == "__main__":
    main()
