import os
import openpyxl

class Cambio ():

    cambios = []

    def __init__ (self, tipo, lote, cantidad, nombre):

        self.tipo = tipo
        self.lote = lote
        self.cantidad = cantidad
        self.nombre = nombre
        Cambio.cambios.append (self)

    @classmethod
    def tablaDeCambios (cls):

        wb = openpyxl.Workbook()
        hoja = wb.active
        print(wb.path)
        print("a")
        hoja.append (("Tipo", "Nombre", "Lote", "Cantidad"))

        for i in Cambio.cambios:

            hoja.append ((i.tipo, i.nombre, i.lote, i.cantidad))
        
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

    cambio1 = Cambio("Eliminar", "1234", 12, "CremaX")
    cambio2 = Cambio("Agregar", "1244", 12, "CremaY")
    cambio3 = Cambio("Agregar", "1233", 12, "CremaZ")
    Cambio.tablaDeCambios()

