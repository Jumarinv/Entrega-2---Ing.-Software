import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))



class Quimico:
    def __init__(self):
        pass

    def listaPorAprovar(self):#Listas de productos para verificar viavilidad
        pass

    def crearListaIngredientes(self):
        pass

    @staticmethod
    def asociar_ingredientes(nombre,cantidad,producto):
        from src.gestorAplicacion.administrativo.materiaPrima import MateriaPrima
        producto.ingredientes = []
        Materia_Prima = MateriaPrima(nombre,int(cantidad),producto)
        producto.ingredientes.append(Materia_Prima)
    
    @staticmethod
    def productos_pendientes():
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial

        lista = []

        dictionary_objects = {}

        contador = 0
        for i in AgenteComercial.Pedidos:
            if i.estado == None:
                lista.append(f"{i.nombre}") #Nombre del producto
                dictionary_objects[contador] = i
                contador += 1

        return [lista,dictionary_objects,contador]

        

        
    