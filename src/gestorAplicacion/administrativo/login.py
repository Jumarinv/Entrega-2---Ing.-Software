import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        # Lista de usuarios (simulando una base de datos)
        self.usuarios = [
            {"id": "001", "nombre": "Juan", "rol": "Asesor financiero", "contraseña": "1234"},
            {"id": "002", "nombre": "Maria", "rol": "Quimico", "contraseña": "1234"},
            {"id": "003", "nombre": "Pedro", "rol": "Bodeguero", "contraseña": "1234"},
            {"id": "004", "nombre": "Ana", "rol": "Admin", "contraseña": "1234"},
        ]

    def autenticar(self, id_usuario, password):
        """
        Método para autenticar al usuario.
        Recibe la ID del usuario y la contraseña, y devuelve el diccionario del usuario si existe y la contraseña es correcta.
        """
        for usuario in self.usuarios:
            if usuario["id"] == id_usuario and usuario["contraseña"] == password:
                return usuario
        return None

    def obtener_rol(self, id_usuario, password):
        """
        Método para obtener el rol del usuario.
        Recibe la ID del usuario y la contraseña, y devuelve el rol si existe y la contraseña es correcta.
        """
        usuario = self.autenticar(id_usuario, password)
        if usuario:
            return usuario["rol"]
        return "No se encuentra registrado en el sistema o la contraseña es incorrecta."


class LoginApp:
    def __init__(self, root):
        self.principal = root
        self.root = tk.Toplevel()
        self.root.title("Sistema de Login")
        self.root.geometry("300x250")

        # Instancia de la clase Login
        self.login_sistema = Login()

        # Crear widgets
        self.label_id = tk.Label(self.root, text="ID de Usuario:")
        self.label_id.pack(pady=5)

        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack(pady=5)

        self.label_pw = tk.Label(self.root, text="Contraseña:")
        self.label_pw.pack(pady=5)

        self.entry_pw = tk.Entry(self.root, show="*")  # Ocultar la contraseña
        self.entry_pw.pack(pady=5)

        self.boton_login = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_login.pack(pady=10)

        #self.root.protocol("WM_DELETE_WINDOW", lambda: (root.deiconify(), self.root.destroy()))

    def iniciar_sesion(self):
        """
        Método para manejar el evento de inicio de sesión.
        Obtiene la ID y la contraseña ingresadas, verifica el rol y muestra un mensaje en una ventana emergente.
        """
        id_usuario = self.entry_id.get()  # Obtener la ID del campo de entrada
        password = self.entry_pw.get()    # Obtener la contraseña del campo de entrada

        rol = self.login_sistema.obtener_rol(id_usuario, password)  # Obtener el rol

        # Mostrar el resultado en una ventana emergente
        if rol != "No se encuentra registrado en el sistema o la contraseña es incorrecta.":

            self.root.destroy()

            #messagebox.showinfo("Login Exitoso", f"Bienvenido. Su rol es: {rol}.")

            if rol == "Asesor financiero":
                self.rol_asesor_financiero()

            elif rol == "Admin":
                self.rol_admin()

            elif rol == "Bodeguero":
                self.rol_bodeguero()

            else:
                self.rol_quimico()

        else:
            messagebox.showerror("Error", rol)

    def rol_asesor_financiero(self):

        ventana = tk.Toplevel()
        ventana.title("Asesor financiero")
        ventana.geometry("800x600")


    def rol_admin(self):

        ventana1 = tk.Toplevel()
        ventana1.title("Admin")
        ventana1.geometry("800x600")


    def rol_quimico(self):

        ventana2 = tk.Toplevel()
        ventana2.title("Quimico")
        ventana2.geometry("800x600")  


    def rol_bodeguero(self):

        ventana3 = tk.Toplevel()
        ventana3.title("Bodeguero")
        ventana3.geometry("800x600")  