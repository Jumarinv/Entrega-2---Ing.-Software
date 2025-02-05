import tkinter as tk
from tkinter import messagebox
from gestorAplicacion.administrativo.login import Login,LoginApp


# Función para abrir la ventana de login y ocultar la ventana principal

def ingresar(root):
    root.withdraw()
    app = LoginApp(root)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de gestión")
root.geometry("800x600")

# Descripción de la empresa
descripcion = """
Bienvenido a nuestra empresa.

Somos una compañía dedicada a ofrecer soluciones innovadoras
en el ámbito tecnológico. Nuestro objetivo es brindar
servicios de alta calidad que satisfagan las necesidades
de nuestros clientes.

¡Gracias por visitarnos!
"""

label_descripcion = tk.Label(root, text=descripcion, justify="center", font=("Arial", 12))
label_descripcion.pack(pady=100)

#login = LoginApp(root)

# Botón para abrir la ventana de login
boton_login = tk.Button(root, text="Iniciar sesión", command= lambda : ingresar(root))
boton_login.pack(side="bottom", pady=50)

# Iniciar el bucle principal de la aplicación
root.mainloop()