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
        dirname = os.path.dirname(__file__)
        ubicacion = os.path.join(dirname, nombre_archivo)
        print (ubicacion)
        
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
        df.to_excel(ubicacion, index=False)
        
        # Imprimir mensaje de éxito
        print(f"Archivo '{nombre_archivo}' generado exitosamente.")
        
        # Abrir el archivo Excel generado
        os.startfile(ubicacion)

    @classmethod
    def agregarProducto(cls,p):
        cls.productos.append(p)
