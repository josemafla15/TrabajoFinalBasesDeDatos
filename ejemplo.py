import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def obtener_fecha():
    fecha_seleccionada = calendario.get_date()
    print(f"Fecha seleccionada: {fecha_seleccionada}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Seleccionar Fecha")
root.geometry("300x200")

# Etiqueta
label = ttk.Label(root, text="Selecciona una fecha:")
label.pack(pady=10)

# Calendario
calendario = DateEntry(root, width=20, background="darkblue",
                       foreground="white", borderwidth=2, year=2024)
calendario.pack(pady=10)

# Botón para obtener la fecha
boton = ttk.Button(root, text="Obtener Fecha", command=obtener_fecha)
boton.pack(pady=10)

root.mainloop()