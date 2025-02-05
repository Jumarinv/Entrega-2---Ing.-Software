import tkinter as tk
from tkinter import messagebox
from gestorAplicacion.administrativo.login import Login,LoginApp
from PIL import Image, ImageTk

# Función para abrir la ventana de login y ocultar la ventana principal

def ingresar(root):
    root.withdraw()
    app = LoginApp(root)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de gestión")
root.geometry("800x600")

# Cargar la imagen de fondo (asegúrate de usar un formato soportado)
imagen_fondo =  Image.open("imagen1.jpg")  # Cargar una imagen JPG, por ejemplo
imagen_fondo = imagen_fondo.resize((800, 600))  # Redimensionarla para que cubra toda la ventana
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un Label que ocupe toda la ventana y sea el fondo
label_fondo = tk.Label(root, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

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
boton_login = tk.Button(root, text="Iniciar sesión", command=lambda: ingresar(root), width=20, height=2, font=("Arial", 16))
boton_login.pack(side="bottom", pady=50, anchor="n")


# Iniciar el bucle principal de la aplicación
root.mainloop()