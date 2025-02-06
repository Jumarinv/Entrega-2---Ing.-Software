from datetime import datetime
import pandas as pd
import pytz
import os

class Producto:

    productos = []
    Contador = 0
    
    def __init__(self,cliente, nombre, estado, ingredientes, cantidad,fechaCaducidad=None):
        self.cliente = cliente
        self.nombre = nombre
        self.estado = estado
        self.ingredientes = ingredientes
        self.cantidad = cantidad
        self.fechaCaducidad = fechaCaducidad
        self.id = Producto.Contador
        Producto.Contador +=1
    
    @classmethod
    def crearInformeExcel(cls):
        colombia_tz = pytz.timezone("America/Bogota")
        now_colombia = datetime.now(colombia_tz)
        fecha = now_colombia.strftime("%Y_mes_%m_dia_%d_Hora_%H_%M")
        nombre_archivo = f"{fecha}.xlsx"  # Nombre del archivo con la fecha
        ubicacion = f"C:\\Users\\jonat\\OneDrive\\Documentos\\GitHub\\Entrega-2---Ing.-Software\\{fecha}.xlsx"
        
        # Filtrar productos con fecha de caducidad y sin fecha
        productos_con_fecha = [p for p in cls.productos if p.fechaCaducidad is not None]
        productos_sin_fecha = [p for p in cls.productos if p.fechaCaducidad is None]
        
        # Ordenar los productos con fecha de caducidad por la fecha
        productos_con_fecha.sort(key=lambda p: p.fechaCaducidad)
        
        # Combinar los productos con fecha de caducidad y sin fecha
        productos_ordenados = productos_con_fecha + productos_sin_fecha
        
        # Crear la lista de diccionarios con la información de los productos
        datos = [
            {
                "Cliente": p.cliente,
                "Nombre": p.nombre,
                "Estado": p.estado,
                "Cantidad": p.cantidad,
                "Fecha de Caducidad": p.fechaCaducidad if p.fechaCaducidad else "Sin fecha"
            }
            for p in productos_ordenados
        ]
        
        # Crear el DataFrame y guardarlo como un archivo Excel
        df = pd.DataFrame(datos)
        df.to_excel(nombre_archivo, index=False)
        
        # Imprimir mensaje de éxito
        print(f"Archivo '{nombre_archivo}' generado exitosamente.")
        
        # Abrir el archivo Excel generado
        os.startfile(ubicacion)

    @classmethod
    def agregarProducto(cls,p):
        cls.productos.append(p)

producto1 = Producto(cliente="Cliente1", nombre="Producto1", estado="Nuevo", ingredientes=["Azúcar", "Harina"], cantidad=10, fechaCaducidad="2025-05-01")
producto2 = Producto(cliente="Cliente2", nombre="Producto2", estado="Nuevo", ingredientes=["Sal", "Aceite"], cantidad=5, fechaCaducidad="2025-06-01")
producto3 = Producto(cliente="Cliente3", nombre="Producto3", estado="Usado", ingredientes=["Leche", "Cereal"], cantidad=3, fechaCaducidad="2025-07-01")
producto4 = Producto(cliente="Cliente4", nombre="Producto4", estado="Nuevo", ingredientes=["Arroz", "Frijoles"], cantidad=7)
producto5 = Producto(cliente="Cliente5", nombre="Producto5", estado="Nuevo", ingredientes=["Pasta", "Tomate"], cantidad=2)
Producto.agregarProducto(producto1)
Producto.agregarProducto(producto2)
Producto.agregarProducto(producto3)
Producto.agregarProducto(producto4)
Producto.agregarProducto(producto5)
Producto.agregarProducto(Producto("Juan", "Pizza", "Entregado", ["Queso", "Tomate"], 2, "2024-07-01"))
Producto.agregarProducto(Producto("Ana", "Hamburguesa", "Pendiente", ["Carne", "Pan"], 3,"2025-07-02"))
#Producto.crearInformeExcel()