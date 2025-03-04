import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))
from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
from src.gestorAplicacion.usuarios.bodeguero import Bodeguero
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
            {"id": "001", "nombre": "Juan", "rol": "Asesor comercial", "contraseña": "1234"},
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
            ("Pedidos pendientes", self.mostrar_pedidos_pendientes),
            ("Volver", lambda: self.reingresar(ventana))
        ]
        
        for texto, comando in botones:
            tk.Button(ventana, text=texto, command=comando, font=("Arial", 12), width=20, height=2, bg="#0056b3", fg="white").pack(pady=10)
            

    def mostrar_pedidos_pendientes(self):

        # Crear un Combobox para seleccionar el producto
        productos = Bodeguero.productos_pendientes2()
        nombres_productos = [producto.nombre for producto in productos]  # Lista de nombres de productos

        if len(productos) == 0:

            messagebox.showinfo("Informacion","No hay pedidos pendientes de materia prima")

        else:
            # Crear una nueva ventana para los pedidos pendientes
            pedidos_pendientes_ventana = tk.Toplevel()
            pedidos_pendientes_ventana.title("Pedidos Pendientes")
            pedidos_pendientes_ventana.geometry("800x600")
            pedidos_pendientes_ventana.configure(bg="#f0f0f0")

            imagen_fondo = Image.open("descarga1.jpg")
            imagen_fondo = imagen_fondo.resize((800, 600))
            fondo = ImageTk.PhotoImage(imagen_fondo)

            # Crear un label con la imagen
            label_fondo = tk.Label(pedidos_pendientes_ventana, image=fondo)
            label_fondo.place(relwidth=1, relheight=1)
            label_fondo.image = fondo  # Evitar que la imagen sea eliminada por el recolector de basura
            
            # Título de la ventana
            tk.Label(pedidos_pendientes_ventana, text="Lista de productos pendientes de pedido", font=("Arial", 22, "bold"), bg="#f0f0f0").pack(pady=20)

            combo_productos = ttk.Combobox(pedidos_pendientes_ventana, values=nombres_productos)
            combo_productos.pack(pady=10)

            # Función para mostrar las materias primas del producto seleccionado
            def mostrar_materias_primas(event):
                producto_seleccionado = combo_productos.get()
                lista_materias_primas.delete(0, tk.END)  # Limpiar la lista actual
                
                # Buscar el producto seleccionado en la lista de productos
                for producto in productos:
                    if producto.nombre == producto_seleccionado:
                        # Mostrar las materias primas del producto seleccionado
                        for materia_prima in producto.ingredientes:
                            lista_materias_primas.insert(tk.END, f"{materia_prima.nombre} - {materia_prima.cantidad}")
                        break

            # Vincular la función al evento de selección del Combobox
            combo_productos.bind("<<ComboboxSelected>>", mostrar_materias_primas)

            # Crear una Listbox para mostrar las materias primas
            lista_materias_primas = tk.Listbox(pedidos_pendientes_ventana)
            lista_materias_primas.pack(pady=10)

            # Botón para cambiar el estado del pedido a "Realizado"

            boton_seleccionar = tk.Button(pedidos_pendientes_ventana, text="Realizado", command=lambda: self.cambiar_estado_pedido(combo_productos,productos,pedidos_pendientes_ventana)) ########
            boton_seleccionar.pack(pady=5)

            # Botón para volver
            boton_volver = tk.Button(pedidos_pendientes_ventana, text="Volver", command=pedidos_pendientes_ventana.destroy)
            boton_volver.pack(pady=20)

    def cambiar_estado_pedido(self,combobox,productos_pendientes,ventana):
      
        nombre_producto = combobox.get()
        indice_producto = combobox.current()

        Cambio("Pedido realizado","Asesor comercial",productos_pendientes[indice_producto].nombre, date.today())

        messagebox.showinfo("Informacion",f"Se ha cambiado el estado del pedido a realizado: {nombre_producto}")

        Bodeguero.cambiar_estado_producto(productos_pendientes[indice_producto],"Pedido realizado")



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
                print(f"Nombre ingresado: {entry_nombre.get()}")
                self.terminar_proceso(seleccion, entry_nombre.get(), None, entry_cantidad.get(), pedido_ventana)
            except tk.TclError:
                print("Por favor, selecciona un elemento de la lista.")

        boton_confirmar = tk.Button(pedido_ventana, text="Confirmar", command=confirmar_seleccion)
        boton_confirmar.pack(pady=10) 

    

    def registrar_Cliente1(self,ventana):
        self.mostrar_encuesta()
        ventana.destroy()#



    def terminar_proceso(self,cliente,nombre,estado,cantidad,ventana):
        def crear_pedidos(cliente, nombre, estado, ingredientes= None, cantidad=0 ,fechaCaducidad=None):
            Pedido = Producto(cliente,nombre,estado, ingredientes, cantidad, fechaCaducidad)
            AgenteComercial.Pedidos.append(Pedido)
            print(f"Cliente: {cliente}, Nombre: {nombre}, Estado: {estado}, Ingredientes: {ingredientes}, Cantidad: {cantidad}, Fecha: {fechaCaducidad}")
            print(nombre)
        crear_pedidos(cliente,nombre,estado,None,cantidad,None)
        messagebox.showinfo('Resultado','Pedido creado correctamente')
        
        for i in AgenteComercial.Pedidos:
            print(f"Cliente: {i.cliente}, Nombre: {i.nombre}, Estado: {i.estado}, Ingredientes: {i.ingredientes}, Cantidad: {i.cantidad}, Fecha: {i.fechaCaducidad}")
    
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





        #bienvenida
        
        r = InterfazQuimico(ventana2)

        

    def rol_bodeguero(self):
        
        ventana3 = tk.Toplevel()
        ventana3.title("Bodeguero")
        ventana3.geometry("800x600")
        ventana3.configure(bg="#f0f0f0")
        
        # Cargar la imagen de fondo
        imagen_fondo = Image.open("descarga1.jpg")
        imagen_fondo = imagen_fondo.resize((800, 600))
        fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crear un label con la imagen
        label_fondo = tk.Label(ventana3, image=fondo)
        label_fondo.place(relwidth=1, relheight=1)
        label_fondo.image = fondo  # Evitar que la imagen sea eliminada por el recolector de basura

        tk.Label(ventana3, text="Bienvenido bodeguero", font=("Arial", 22, "bold"), bg="#f0f0f0").pack(pady=20)
        
        botones = [
            ("Mostrar historial", self.mostrarCambios),
            ("Stock productos", self.excelStockProductos),
            ("Validar llegada de materia prima", self.validar_llegada_materiaprima),
            ("Terminar producto", self.actualizar_terminados),
            ("Despachar producto", self.despachar_producto),
            ("Buscar producto", self.buscar),
            ("Volver", lambda: self.reingresar(ventana3))
        ]
        
        for texto, comando in botones:
            tk.Button(ventana3, text=texto, command=comando, font=("Arial", 12), width=25, height=2, bg="#0056b3", fg="white").pack(pady=10)

    def validar_llegada_materiaprima(self):
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        from src.gestorAplicacion.usuarios.bodeguero import Bodeguero

        lista_productos_pendientes = Bodeguero.productos_pendientes2()

        for p in AgenteComercial.Pedidos:
            print(f"{p.nombre} -- {p.estado}")


        if len(lista_productos_pendientes) == 0:

            messagebox.showinfo("Informacion","No hay productos pendientes por recibir materia prima")

        else:

            llegada_ventana = tk.Toplevel()
            llegada_ventana.title("Validar llegada materia prima")
            llegada_ventana.geometry("500x400")
            
            nombres_productos = []

            for o in lista_productos_pendientes:
                nombres_productos.append(o.nombre)

            label_informacion_validar = tk.Label(llegada_ventana,text="Seleccione el producto, el cual ya cuenta con sus \n todos ingredientes para empezar su produccion:")
            label_informacion_validar.pack(pady=8)

            combobox_nombres_productos = ttk.Combobox(llegada_ventana, values=nombres_productos,state='readonly')
            combobox_nombres_productos.pack(pady=8)

            boton_seleccionar = tk.Button(llegada_ventana, text="Seleccionar", command=lambda: self.cambiar_estado_producir(combobox_nombres_productos,lista_productos_pendientes,llegada_ventana)) ########
            boton_seleccionar.pack(pady=5)

    def despachar_producto(self):

        lista_productos_pendientes = Bodeguero.productosTerminados()

        for p in AgenteComercial.Pedidos:
            print(f"{p.nombre} -- {p.estado}")


        if len(lista_productos_pendientes) == 0:

            messagebox.showinfo("Informacion","No hay productos terminados para despachar")

        else:

            llegada_ventana = tk.Toplevel()
            llegada_ventana.title("Despachar producto")
            llegada_ventana.geometry("500x400")
            
            nombres_productos = []

            for o in lista_productos_pendientes:
                nombres_productos.append(o.nombre)

            label_informacion_validar = tk.Label(llegada_ventana,text="Seleccione el producto que quiere despachar:")
            label_informacion_validar.pack(pady=8)

            combobox_nombres_productos = ttk.Combobox(llegada_ventana, values=nombres_productos,state='readonly')
            combobox_nombres_productos.pack(pady=8)

            boton_seleccionar = tk.Button(llegada_ventana, text="Despachar", command=lambda: self.despachar(combobox_nombres_productos,lista_productos_pendientes,llegada_ventana)) ########
            boton_seleccionar.pack(pady=5)

    def despachar(self,combobox,productos_pendientes,ventana):

        nombre_producto = combobox.get()
        indice_producto = combobox.current()

        #Cambio("Llegada ingredientes","Bodeguero",productos_pendientes[indice_producto].nombre, date.today())

        messagebox.showinfo("Informacion",f"Se ha despachado el producto: {nombre_producto}")

        Producto.productos.remove(productos_pendientes[indice_producto])
        ventana.destroy()



    def actualizar_terminados(self):
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        from src.gestorAplicacion.usuarios.bodeguero import Bodeguero

        productosEnProduccion = Bodeguero.productosEnProduccion()

        if len(productosEnProduccion) == 0:
            messagebox.showinfo("Información", "No hay productos pendientes por recibir materia prima")
        else:
            llegada_ventana = tk.Toplevel()
            llegada_ventana.title("Actualizar productos terminados")
            llegada_ventana.geometry("500x400")
            
            nombres_productos = [o.nombre for o in productosEnProduccion]

            label_informacion_validar = tk.Label(llegada_ventana, text="Seleccione el producto que quiere establecer como terminado:")
            label_informacion_validar.pack(pady=8)

            combobox_nombres_productos = ttk.Combobox(llegada_ventana, values=nombres_productos, state='readonly')
            combobox_nombres_productos.pack(pady=8)

            # Nuevo label para la fecha de vencimiento
            label_fecha_vencimiento = tk.Label(llegada_ventana, text="Ingresar fecha de vencimiento (dd/mm/aa):")
            label_fecha_vencimiento.pack(pady=8)

            # Campo de entrada para la fecha de vencimiento
            entry_fecha_vencimiento = tk.Entry(llegada_ventana)
            entry_fecha_vencimiento.pack(pady=8)

            boton_seleccionar = tk.Button(
                llegada_ventana, 
                text="Seleccionar", 
                command=lambda: self.cambiar_estado_terminado(
                    combobox_nombres_productos, 
                    productosEnProduccion, 
                    llegada_ventana, 
                    entry_fecha_vencimiento.get()  # Pasamos la fecha ingresada
                )
            )
            boton_seleccionar.pack(pady=5)

    def buscar(self):
        from src.gestorAplicacion.administrativo.producto import Producto

        productosTerminados = Producto.productos

        if len(productosTerminados) == 0:
            messagebox.showinfo("Información", "No hay productos terminados")
        else:
            llegada_ventana = tk.Toplevel()
            llegada_ventana.title("Buscar producto")
            llegada_ventana.geometry("500x400")

            label_fecha_vencimiento = tk.Label(llegada_ventana, text="Ingresar ID del producto:")
            label_fecha_vencimiento.pack(pady=8)

            # Campo de entrada para el ID del producto a buscar
            entryProductoABuscar = tk.Entry(llegada_ventana)
            entryProductoABuscar.pack(pady=8)

            # Label para mostrar la información del producto encontrado
            label_resultado = tk.Label(llegada_ventana, text="", wraplength=400, justify="left")
            label_resultado.pack(pady=8)

            def realizar_busqueda():
                from src.gestorAplicacion.usuarios.bodeguero import Bodeguero
                
                producto = Bodeguero.buscar(int(entryProductoABuscar.get()))

                if not producto is None:
                    label_resultado.config(text=f"""Producto encontrado:\n
                                           ID: {producto.id}\n
                                           Nombre: {producto.nombre}\n
                                           Cliente: {producto.cliente}\n
                                           Cantidad: {producto.cantidad}\n
                                           Fecha de caducidad: {producto.fechaCaducidad}""")
                else:
                    label_resultado.config(text="No se encontró el producto con ese ID")

            boton_seleccionar = tk.Button(
                llegada_ventana,
                text="Buscar",
                command=realizar_busqueda
            )
            boton_seleccionar.pack(pady=5)
            boton_regresar = tk.Button(
                llegada_ventana,
                text="Regresar",
                command=llegada_ventana.destroy
            )
            boton_regresar.pack(pady=5)      

    def cambiar_estado_producir(self,combobox,productos_pendientes,ventana):
        from src.gestorAplicacion.usuarios.bodeguero import Bodeguero
        from src.gestorAplicacion.administrativo.Cambio import Cambio

        nombre_producto = combobox.get()
        indice_producto = combobox.current()

        Cambio("Llegada ingredientes","Bodeguero",productos_pendientes[indice_producto].nombre, date.today())

        messagebox.showinfo("Informacion",f"Se ha validado la llegada de los ingredientes del producto: {nombre_producto}")

        Bodeguero.cambiar_estado_producto(productos_pendientes[indice_producto],"En produccion")

        ventana.destroy()
    
    def cambiar_estado_terminado(self,combobox,productos_pendientes,ventana,fecha):
        from src.gestorAplicacion.usuarios.bodeguero import Bodeguero
        from src.gestorAplicacion.administrativo.Cambio import Cambio
        from src.gestorAplicacion.administrativo.producto import Producto

        nombre_producto = combobox.get()
        indice_producto = combobox.current()


        Cambio("Llegada ingredientes","Bodeguero",productos_pendientes[indice_producto].nombre, date.today())

        messagebox.showinfo("Informacion",f"Se ha terminado el producto: {nombre_producto}")
        productos_pendientes[indice_producto].fechaCaducidad = fecha
        Bodeguero.cambiar_estado_producto(productos_pendientes[indice_producto],"Terminado")
        Producto.agregarProducto(productos_pendientes[indice_producto])

        ventana.destroy()
        for p in Producto.productos:
            print(p.id)
        print(Bodeguero.buscar(1))
        print(productos_pendientes[indice_producto].fechaCaducidad)
        print(Producto.productos[0].id)

    def reingresar (self, ventana):

        LoginApp(Login.root1)
        ventana.destroy()