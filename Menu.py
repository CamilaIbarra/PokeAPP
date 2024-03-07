import tkinter as tk


def iniciar_juego():
    # Agrega aquí la lógica para iniciar el juego
    print("Iniciar juego")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Principal")

# Función para cerrar la aplicación


def cerrar_app():
    ventana.destroy()


# Etiqueta del título
titulo = tk.Label(ventana, text="Menú Principal", font=("Arial", 20))
titulo.pack(pady=20)

# Botón para iniciar el juego
btn_iniciar = tk.Button(ventana, text="Iniciar Juego", command=iniciar_juego)
btn_iniciar.pack(pady=10)

# Botón para cerrar la aplicación
btn_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_app)
btn_cerrar.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
