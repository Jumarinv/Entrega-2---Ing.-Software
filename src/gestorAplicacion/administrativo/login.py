import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))
from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
#from src.gestorAplicacion.administrativo.Cambio import Cambio
from src.gestorAplicacion.administrativo.materiaPrima import MateriaPrima
from src.gestorAplicacion.administrativo.Cambio import Cambio
from src.gestorAplicacion.administrativo.producto import Producto

 
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

        # Instancia de la clase AgenteComercial
        self.agente_comercial = AgenteComercial()

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
        ventana.configure(bg="#f0f0f0")
        
        tk.Label(ventana, text="Bienvenido asesor comercial", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        
        botones = [
            ("Registrar Cliente", self.mostrar_encuesta),
            ("Crear Pedido", self.crear_pedido),
            ("Mostrar historial", self.mostrarCambios)
        ]
        
        for texto, comando in botones:
            tk.Button(ventana, text=texto, command=comando, font=("Arial", 12), width=20, height=2, bg="#007BFF", fg="white").pack(pady=10)
    
    def crear_pedido(self):
        pedido_ventana = tk.Toplevel()
        pedido_ventana.title("Crear pedido")
        pedido_ventana.geometry("500x350")
        pedido_ventana.configure(bg="#f0f0f0")
        lista_ingredientes = []

        tk.Label(pedido_ventana, text="Seleccione un producto:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        
        listbox = tk.Listbox(pedido_ventana)
        for cliente in AgenteComercial.clientes:
            listbox.insert(tk.END, cliente.getNombre())
        listbox.pack(pady=10)

        tk.Label(pedido_ventana, text="Nombre del pedido:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        entry_nombre = tk.Entry(pedido_ventana)
        entry_nombre.pack(pady=5)

        tk.Label(pedido_ventana, text="Ingrese una descripción del pedido:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        text = tk.Text(pedido_ventana, height=5, width=40)
        text.pack(pady=10)
        
        tk.Button(pedido_ventana, text="Confirmar", command=lambda: self.terminar_proceso(listbox.get(listbox.curselection()), entry_nombre.get(), 'Pendiente', lista_ingredientes, pedido_ventana), font=("Arial", 12), bg="#28A745", fg="white").pack(pady=10)
        
        tk.Button(pedido_ventana, text="Registrar Cliente", command=lambda: self.registrar_Cliente1(pedido_ventana), font=("Arial", 12), bg="#DC3545", fg="white").pack(pady=10)
    
    def registrar_Cliente1(self, ventana):
        self.mostrar_encuesta()
        ventana.destroy()
    
    def terminar_proceso(self, cliente, nombre, estado, lista, ventana):
        AgenteComercial.crear_pedidos(self, cliente, nombre, estado, lista)
        messagebox.showinfo("Resultado", "Pedido creado correctamente")
        ventana.destroy()
    
    def mostrar_encuesta(self):
        encuesta_ventana = tk.Toplevel()
        encuesta_ventana.title("Registro de Cliente")
        encuesta_ventana.geometry("400x300")
        encuesta_ventana.configure(bg="#f0f0f0")
        
        campos = [
            ("ID del Cliente:", None),
            ("Nombre del Cliente:", None),
            ("Correo del Cliente:", None),
            ("Teléfono del Cliente:", None)
        ]
        
        entradas = []
        for texto, _ in campos:
            tk.Label(encuesta_ventana, text=texto, font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
            entry = tk.Entry(encuesta_ventana)
            entry.pack(pady=5)
            entradas.append(entry)
        
        tk.Button(encuesta_ventana, text="Registrar", command=lambda: self.registrar_cliente(entradas[0].get(), entradas[1].get(), "", entradas[2].get(), entradas[3].get(), encuesta_ventana), font=("Arial", 12), bg="#007BFF", fg="white").pack(pady=20)
    
    def registrar_cliente(self, id, nombre, productos, correo, tel, ventana):
        resultado = self.agente_comercial.registrar_cliente(id, nombre, productos, correo, tel)
        messagebox.showinfo("Resultado", resultado)
        if "éxito" in resultado.lower():
            ventana.destroy()
    
    def mostrarCambios(self):
        Cambio.tablaDeCambios()
        messagebox.showinfo("Creado", "Archivo excel creado")
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "historialDeCambios.xlsx")
        os.system(filename)
    
    def excelStockProductos(self):
        Producto.crearInformeExcel()
        messagebox.showinfo("Información", "Se ha creado el archivo de excel.")


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

        # Botón para registrar cliente
        boton_registrar_cliente = tk.Button(ventana3, text="Mostrar historial", command=self.mostrarCambios)
        boton_registrar_cliente.pack(pady=20)

        boton_nuevo = tk.Button(ventana3, text="Stock productos", command=self.excelStockProductos)
        boton_nuevo.pack(pady=20)
