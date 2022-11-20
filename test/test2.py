from tkinter import messagebox, ttk
import tkinter as tk
def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )
    print(selection)
main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(
    state="readonly",
    values=["Python", "C", "C++", "Java"]
)
combo.place(x=50, y=50)
button = ttk.Button(text="Mostrar selección", command=show_selection)
button.place(x=50, y=100)
main_window.mainloop()