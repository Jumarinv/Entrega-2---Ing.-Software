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
from src.gestorAplicacion.administrativo.Interfaz_quimico import InterfazQuimico
from datetime import date
from PIL import Image, ImageTk

 
class Login:

    root1 = None
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

            if rol == "Asesor comercial":
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
        ventana.title("Asesor comercial")
        ventana.geometry("800x600")
        ventana.configure(bg="#f0f0f0")
        
            # Cargar la imagen de fondo
        imagen_fondo = Image.open("descarga1.jpg")
        imagen_fondo = imagen_fondo.resize((800, 600))
        fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crear un label con la imagen
        label_fondo = tk.Label(ventana, image=fondo)
        label_fondo.place(relwidth=1, relheight=1)
        label_fondo.image = fondo  # Evitar que la imagen sea eliminada por el recolector de basura

        tk.Label(ventana, text="Bienvenido asesor comercial", font=("Arial", 22, "bold"), bg="#f0f0f0").pack(pady=20)
        
        botones = [
            ("Registrar Cliente", self.mostrar_encuesta),
            ("Crear Pedido", self.crear_pedido),
            ("Mostrar historial", self.mostrarCambios),
            ("Volver", lambda: self.reingresar(ventana))
        ]
        
        for texto, comando in botones:
            tk.Button(ventana, text=texto, command=comando, font=("Arial", 12), width=20, height=2, bg="#0056b3", fg="white").pack(pady=10)
    
    def crear_pedido(self):
        pedido_ventana = tk.Toplevel()
        pedido_ventana.title("Crear pedido")
        pedido_ventana.geometry("500x650")
        pedido_ventana.configure(bg="#f0f0f0")
        lista_ingredientes = []

        # Etiqueta de instrucciones
        label = tk.Label(pedido_ventana, text="Seleccione un cliente:")
        label.pack(pady=10)

        # Listbox para mostrar los nombres de los objetos
        listbox_nombres = tk.Listbox(pedido_ventana)
        for cliente in AgenteComercial.clientes:
            listbox_nombres.insert(tk.END, cliente.getNombre())
        listbox_nombres.pack(pady=10)

        tk.Label(pedido_ventana, text="Nombre del pedido:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        entry_nombre = tk.Entry(pedido_ventana)
        entry_nombre.pack(pady=5)

        tk.Label(pedido_ventana, text="Cantidad del pedido").pack(pady=5)
        entry_cantidad = tk.Entry(pedido_ventana)
        entry_cantidad.pack(pady=5)
  

        #boton_agregar_ingrediente = tk.Button(pedido_ventana, text ='agregar ingredientes', command = lambda :self.agregar_ingrediente(lista_ingredientes))
        #boton_agregar_ingrediente.pack(pady=20)

        tk.Label(pedido_ventana, text="Ingrese un descripcion del pedido:").pack(pady=20)
        text = tk.Text(pedido_ventana, height=5, width=40)
        text.pack(pady=10)
        

        #cliente, nombre, estado, ingredientes, cantidad,fechaCaducidad=None

        boton_registrar_cliente = tk.Button(pedido_ventana, text="Registrar Cliente", command= lambda :self.registrar_Cliente1(pedido_ventana))
        boton_registrar_cliente.pack(pady=20)

        def confirmar_seleccion():
            try:
                seleccion = listbox_nombres.get(listbox_nombres.curselection())
                Cambio("Pedido", "Asesor", entry_nombre.get(), date.today() )
                self.terminar_proceso(seleccion, entry_nombre.get(), 'Pendiente', entry_cantidad.get(), pedido_ventana)
            except tk.TclError:
                print("Por favor, selecciona un elemento de la lista.")

        boton_confirmar = tk.Button(pedido_ventana, text="Confirmar", command=confirmar_seleccion)
        boton_confirmar.pack(pady=10) 

    

    def registrar_Cliente1(self,ventana):
        self.mostrar_encuesta()
        ventana.destroy()



    def terminar_proceso(self,cliente,nombre,estado,cantidad,ventana):
        AgenteComercial.crear_pedidos(cliente,nombre,estado,None,cantidad,None)
        messagebox.showinfo('Resultado','Pedido creado correctamente')
        ventana.destroy()
    
    def mostrar_encuesta(self):
        encuesta_ventana = tk.Toplevel()
        encuesta_ventana.title("Registro de Cliente")
        encuesta_ventana.geometry("400x350")
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
        ventana1.geometry("800x600")
        ventana1.title("Administrador")

        imagen_fondo = Image.open("descarga1.jpg")
        imagen_fondo = imagen_fondo.resize((800, 600))
        fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crear un label con la imagen
        label_fondo = tk.Label(ventana1, image=fondo)
        label_fondo.place(relwidth=1, relheight=1)
        label_fondo.image = fondo  # Evitar que la imagen sea eliminada por el recolector de basura

        # bienvenida
        tk.Label(ventana1, text="Bienvenido administrador", font=("Arial", 22, "bold")).pack(pady=20)

        # Botón para volver
        botonVolver = tk.Button(ventana1, text="Volver", command= lambda: self.reingresar(ventana1) )
        botonVolver.pack(pady=20)

    def rol_quimico(self):
        ventana2 = tk.Toplevel()
        ventana2.geometry("800x600")

        imagen_fondo = Image.open("descarga1.jpg")
        imagen_fondo = imagen_fondo.resize((1000, 800))
        fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crear un label con la imagen
        label_fondo = tk.Label(ventana2, image=fondo)
        label_fondo.place(relwidth=1, relheight=1)
        label_fondo.image = fondo  # Evitar que la imagen sea eliminada por el recolector de basura

        #bienvenida
        tk.Label(ventana2, text="Bienvenido quimico", font=("Arial", 22, "bold")).pack(pady=20)
        ventana2.title("Quimico")
        r = InterfazQuimico(ventana2)

        

    def rol_bodeguero(self):
        
        ventana3 = tk.Toplevel()
        ventana3.title("Bodeguero")
        ventana3.geometry("800x600")

        imagen_fondo = Image.open("descarga1.jpg")
        imagen_fondo = imagen_fondo.resize((800, 600))
        fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crear un label con la imagen
        label_fondo = tk.Label(ventana3, image=fondo)
        label_fondo.place(relwidth=1, relheight=1)
        label_fondo.image = fondo  # Evitar que la imagen sea eliminada por el recolector de basura

        # bienvenida
        tk.Label(ventana3, text="Bienvenido bodeguero", font=("Arial", 22, "bold")).pack(pady=20)

        ventana3.title("Bodeguero")

        # Botón para registrar cliente
        botonMostrarCambios = tk.Button(ventana3, text="Mostrar historial", command=self.mostrarCambios)
        botonMostrarCambios.pack(pady=20)

        boton_nuevo = tk.Button(ventana3, text="Stock productos", command=self.excelStockProductos)
        boton_nuevo.pack(pady=20)

        # Botón para volver
        botonVolver = tk.Button(ventana3, text="Volver", command= lambda: self.reingresar(ventana3) )
        botonVolver.pack(pady=20)

    def reingresar (self, ventana):

        LoginApp(Login.root1)
        ventana.destroy()