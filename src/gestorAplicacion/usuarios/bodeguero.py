import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))

class Bodeguero:
    def __init__(self):
        self.productos = []

    @staticmethod
    def productos_pendientes():
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        lista = []

        for i in AgenteComercial.Pedidos:
            if i.estado == "Pedido realizado":
                lista.append(i)

        return lista
    
    def productos_pendientes2():
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        lista = []

        for i in AgenteComercial.Pedidos:
            if i.estado == "Pendiente":
                lista.append(i)

        return lista
    
    @staticmethod
    def productosEnProduccion():
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        lista = []

        for i in AgenteComercial.Pedidos:
            if i.estado == "En produccion":
                lista.append(i)

        return lista
    
    def productosTerminados():
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        lista = []

        for i in AgenteComercial.Pedidos:
            if i.estado == "Terminado":
                lista.append(i)

        return lista
    
    @classmethod
    def buscar(cls,id):
        from src.gestorAplicacion.administrativo.producto import Producto

        encontrado = False

        for i in range(len(Producto.productos)):
            if Producto.productos[i].id == id:
                return Producto.productos[i]
            
        if encontrado == False:
            return None


    @staticmethod
    def cambiar_estado_producto(producto,estado):
        producto.estado = estado
