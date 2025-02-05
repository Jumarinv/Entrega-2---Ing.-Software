from openpyxl import Workbook
from datetime import datetime
import pytz

class MateriaPrima:
    #inventario general
    materiales = {"material1" : 0, "material2" : 0, "material3" : 0, "material4" : 0} #nombre:cantidad

    def __init__(self,nombre,cantidad,producto):
        self.nombre = nombre
        self.cantidad = cantidad
        self.producto = producto
    
    def incrementar(self, nombre, cantidad):
        MateriaPrima.materiales[nombre] +=cantidad
    
    def disminuir(self, nombre, cantidad):
        MateriaPrima.materiales[nombre] -=cantidad
    
    def agregarTipo(self, nombre, cantidad):
        MateriaPrima.materiales[nombre] = cantidad
    
    @classmethod
    def crearInformeExcel(cls):
        
        colombia_tz = pytz.timezone("America/Bogota")

        # Obtener la hora actual en Colombia
        now_colombia = datetime.now(colombia_tz)

        wb = Workbook()
        ws = wb.active

        fecha = now_colombia.strftime("%Y_mes_%m_dia_%d_Hora_%H_%M")

        # Escribir los encabezados
        ws.append(["MATERIAL", "CANTIDAD"])

        # Escribir los datos del diccionario
        for material, cantidad in MateriaPrima.materiales.items():
            ws.append([material, cantidad])

        # Guardar el archivo de Excel
        wb.save(f"materiales{fecha}.xlsx")

MateriaPrima.crearInformeExcel()
