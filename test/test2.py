"""Prototipo de Tkinter: Combobox que muestra la opción seleccionada."""

import tkinter as tk
from tkinter import messagebox, ttk


def main() -> None:
    """Abre la ventana de prueba con el Combobox."""
    main_window = tk.Tk()
    main_window.config(width=300, height=200)
    main_window.title("Combobox")
    combo = ttk.Combobox(main_window, state="readonly", values=["Python", "C", "C++", "Java"])
    combo.place(x=50, y=50)

    def show_selection() -> None:
        """Muestra la opción seleccionada en un cuadro de diálogo."""
        selection = combo.get()
        messagebox.showinfo(message=f"La opción seleccionada es: {selection}", title="Selección")
        print(selection)

    button = ttk.Button(main_window, text="Mostrar selección", command=show_selection)
    button.place(x=50, y=100)
    main_window.mainloop()


if __name__ == "__main__":
    main()
