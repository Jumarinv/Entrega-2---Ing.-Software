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
            if i.estado == "Pendiente":
                lista.append(i)

        return lista
    
    @staticmethod
    def cambiar_estado_producto(producto,estado):
        producto.estado = estado