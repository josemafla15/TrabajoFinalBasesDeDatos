import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

def obtener_fecha_hora():
    fecha_seleccionada = calendario.get_date()
    hora = spin_hora.get()
    minuto = spin_minuto.get()
    fecha_hora = datetime(
        fecha_seleccionada.year,
        fecha_seleccionada.month,
        fecha_seleccionada.day,
        int(hora),
        int(minuto)
    )
    print(f"Fecha y hora seleccionadas: {fecha_hora}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Seleccionar Fecha y Hora")
root.geometry("350x250")

# Selector de fecha
label_fecha = ttk.Label(root, text="Selecciona una fecha:")
label_fecha.pack(pady=10)

calendario = DateEntry(root, width=20, background="darkblue",
                       foreground="white", borderwidth=2, year=2024)
calendario.pack(pady=5)

# Selector de hora
label_hora = ttk.Label(root, text="Selecciona la hora:")
label_hora.pack(pady=5)

# Spinbox para hora y minutos
frame_hora = ttk.Frame(root)
frame_hora.pack(pady=5)

spin_hora = ttk.Spinbox(frame_hora, from_=0, to=23, width=5, format="%02.0f")
spin_hora.set("12")
spin_hora.pack(side=tk.LEFT)

label_sep = ttk.Label(frame_hora, text=":")
label_sep.pack(side=tk.LEFT)

spin_minuto = ttk.Spinbox(frame_hora, from_=0, to=59, width=5, format="%02.0f")
spin_minuto.set("00")
spin_minuto.pack(side=tk.LEFT)

# Botón para obtener fecha y hora
boton = ttk.Button(root, text="Obtener Fecha y Hora", command=obtener_fecha_hora)
boton.pack(pady=20)

root.mainloop()