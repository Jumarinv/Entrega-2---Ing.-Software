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

        # Botón para registrar cliente
        boton_registrar_cliente = tk.Button(ventana, text="Registrar Cliente", command=self.mostrar_encuesta)
        boton_registrar_cliente.pack(pady=20)

        # Botón para crear pedido
        boton_crear_pedido = tk.Button(ventana, text="Crear Pedido", command=self.crear_pedido)
        boton_crear_pedido.pack(pady=50)

        # Boton para mostrar historial de cambios

        botonHistorial = tk.Button(ventana, text="Mostrar historial", command=self.mostrarCambios)
        botonHistorial.pack(pady=70)

    def crear_pedido(self):
        pedido_ventana = tk.Toplevel()
        pedido_ventana.title("Crear pedido")
        pedido_ventana.geometry("500x350")
        lista_ingredientes=[]

        # Etiqueta de instrucciones
        label = tk.Label(pedido_ventana, text="Seleccione un producto:")
        label.pack(pady=10)

        # Listbox para mostrar los nombres de los objetos
        listbox = tk.Listbox(pedido_ventana)
        for cliente in AgenteComercial.clientes:
            listbox.insert(tk.END, cliente.getNombre())
        listbox.pack(pady=10)


        tk.Label(pedido_ventana, text="Nombre del pedido").pack(pady=5)
        entry_nombre = tk.Entry(pedido_ventana)
        entry_nombre.pack(pady=5)
  

        #boton_agregar_ingrediente = tk.Button(pedido_ventana, text ='agregar ingredientes', command = lambda :self.agregar_ingrediente(lista_ingredientes))
        #boton_agregar_ingrediente.pack(pady=20)

        tk.Label(pedido_ventana, text="Ingrese un descripcion del pedido:").pack(pady=20)
        text = tk.Text(pedido_ventana, height=5, width=40)
        text.pack(pady=20)
        

        boton_confirmar = tk.Button(pedido_ventana, text="Confirmar", command=lambda: self.terminar_proceso(listbox.get(listbox.curselection()),entry_nombre.get(),'Pendiente',lista_ingredientes,pedido_ventana))
        boton_confirmar.pack(pady=10)

        boton_registrar_cliente = tk.Button(pedido_ventana, text="Registrar Cliente", command= lambda :self.registrar_Cliente1(pedido_ventana))
        boton_registrar_cliente.pack(pady=20)

    def registrar_Cliente1(self,ventana):
        self.mostrar_encuesta()
        ventana.destroy()



    def terminar_proceso(self,cliente,nombre,estado,lista,ventana):
        AgenteComercial.crear_pedidos(self,cliente,nombre,estado,lista)
        messagebox.showinfo('Resultado','Pedido creado correctamente')
        ventana.destroy()
    
    def agregar_ingrediente(self,lista):
        ingrediente_ventana = tk.Toplevel()
        ingrediente_ventana.title("Ingrediente")
        ingrediente_ventana.geometry("500x350")

        tk.Label(ingrediente_ventana, text="Nombre del ingrediente").pack(pady=5)
        entry_nombre = tk.Entry(ingrediente_ventana)
        entry_nombre.pack(pady=5)

        tk.Label(ingrediente_ventana, text="Ingrese cantidad").pack(pady=5)
        entry_cantidad = tk.Entry(ingrediente_ventana)
        entry_cantidad.pack(pady=5)

        boton_agregar_ingrediente = tk.Button(ingrediente_ventana, text ='agregar ingredientes', command = lambda: self.agregar_ingrediente_lista(entry_nombre.get(), entry_cantidad.get(),lista))
        boton_agregar_ingrediente.pack(pady=20)

    def agregar_ingrediente_lista(self,nombre,cantidad, lista):
        materia = MateriaPrima(nombre,cantidad, None)
        messagebox.showinfo('Resultado','Ingrediente agreado correctamente')
        lista.append(materia)

    def mostrar_encuesta(self):
        encuesta_ventana = tk.Toplevel()
        encuesta_ventana.title("Registro de Cliente")
        encuesta_ventana.geometry("400x300")

        # Campos de la encuesta
        tk.Label(encuesta_ventana, text="ID del Cliente:").pack(pady=5)
        entry_id = tk.Entry(encuesta_ventana)
        entry_id.pack(pady=5)

        tk.Label(encuesta_ventana, text="Nombre del Cliente:").pack(pady=5)
        entry_nombre = tk.Entry(encuesta_ventana)
        entry_nombre.pack(pady=5)

        #tk.Label(encuesta_ventana, text="Productos (separados por comas):").pack(pady=5)
        #entry_productos = tk.Entry(encuesta_ventana)
        #entry_productos.pack(pady=5)

        tk.Label(encuesta_ventana, text="Correo del Cliente:").pack(pady=5)
        entry_correo = tk.Entry(encuesta_ventana)
        entry_correo.pack(pady=5)

        tk.Label(encuesta_ventana, text="Teléfono del Cliente:").pack(pady=5)
        entry_tel = tk.Entry(encuesta_ventana)
        entry_tel.pack(pady=5)

        # Botón para registrar
        boton_registrar = tk.Button(encuesta_ventana, text="Registrar", command=lambda: self.registrar_cliente(
            entry_id.get(), entry_nombre.get(), "", entry_correo.get(), entry_tel.get(), encuesta_ventana))
        boton_registrar.pack(pady=20)

    def registrar_cliente(self, id, nombre, productos, correo, tel, ventana):
        resultado = self.agente_comercial.registrar_cliente(id, nombre, productos, correo, tel)
        messagebox.showinfo("Resultado", resultado)
        if "éxito" in resultado.lower():
            ventana.destroy()


    def mostrarCambios (self):

            Cambio.tablaDeCambios()
            messagebox.showinfo("Creado", "Archivo excel creado")
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, 'historialDeCambios.xlsx')
            os.system(filename)

    def excelStockProductos(self):

        Producto.crearInformeExcel()
        messagebox.showinfo("Información","Se ha creado el archivo de excel.")

    def rol_admin(self):
        ventana1 = tk.Toplevel()
        ventana1.title("Admin")
        ventana1.geometry("800x600")

    def rol_quimico(self):
        ventana2 = tk.Toplevel()
        r = InterfazQuimico(ventana2)

    def rol_bodeguero(self):
        
        ventana3 = tk.Toplevel()
        ventana3.title("Bodeguero")
        ventana3.geometry("800x600")

        # Botón para registrar cliente
        boton_registrar_cliente = tk.Button(ventana3, text="Mostrar historial", command=self.mostrarCambios)
        boton_registrar_cliente.pack(pady=20)

        boton_nuevo = tk.Button(ventana3, text="Stock productos", command=self.excelStockProductos)
        boton_nuevo.pack(pady=20)
