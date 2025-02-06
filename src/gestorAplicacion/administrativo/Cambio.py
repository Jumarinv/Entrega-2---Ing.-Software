import os
import openpyxl
from datetime import date

class Cambio ():

    cambios = []

    def __init__ (self, tipo, responsable, nombre, fecha):

        self.tipo = tipo
        self.responsable = responsable
        self.fecha = fecha
        self.nombre = nombre
        Cambio.cambios.append (self)

    @classmethod
    def tablaDeCambios (cls):

        wb = openpyxl.Workbook()
        hoja = wb.active
        print(wb.path)
        print("a")
        hoja.append (("Tipo", "Responsable", "Nombre", "Fecha"))

        for i in Cambio.cambios:

            hoja.append ((i.tipo, i.responsable, i.nombre, str(i.fecha)))
        
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'historialDeCambios.xlsx')
        wb.save(filename)
        



def setLote (self, lote):

    self.lote = lote

def getLote (self):

    return self.lote

def setTipo (self, tipo):

    self.tipo = tipo

def getTipo(self):

    return self.tipo

def setCantidad (self, cantidad):

    self.cantidad = cantidad

def getCantidad (self):

    return self.cantidad

if __name__ == "__main__":

    Cambio("Pedido", "Asesor", "crema", date.today() )
    Cambio.tablaDeCambios()

