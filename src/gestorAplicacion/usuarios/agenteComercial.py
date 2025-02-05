import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))
from src.gestorAplicacion.usuarios.cliente import Cliente
from src.gestorAplicacion.administrativo.producto import Producto

class AgenteComercial:

    clientes = []
    Pedidos = []
    
    def __init__(self):
        """
        Inicializa el agente comercial con una lista para almacenar los clientes.
        Cada cliente es una instancia de la clase Cliente.
        """
        

    def registrar_cliente(self, id, nombre, productos, correo, tel):
        """
        Registra un nuevo cliente.

        :param id: Identificación del cliente
        :param nombre: Nombre del cliente
        :param productos: Lista de productos del cliente
        :param correo: Correo del cliente
        :param tel: Teléfono del cliente
        :return: Mensaje indicando el resultado del registro
        """
        if not id or not nombre or not correo or not tel:
            return "Error: Todos los campos (id, nombre, correo, teléfono) son obligatorios."

        productos_lista = [p.strip() for p in productos.split(',')]
        nuevo_cliente = Cliente(id=id, nombre=nombre, productos=productos_lista, correo=correo, tel=tel)

        if self.validar_duplicado(nuevo_cliente):
            return "Error: El cliente ya existe. Actualice los datos del cliente existente si es necesario."

        self.clientes.append(nuevo_cliente)
        return "Cliente registrado exitosamente."

    def validar_duplicado(self, nuevo_cliente):
        """
        Verifica si ya existe un cliente con el mismo correo o identificación.

        :param nuevo_cliente: Instancia de la clase Cliente a verificar
        :return: True si el cliente ya existe, False en caso contrario
        """
        for cliente in AgenteComercial.clientes:
            if cliente.correo == nuevo_cliente.correo or cliente.id == nuevo_cliente.id:
                return True
        return False

    def listar_clientes(self):
        """
        Devuelve la lista actual de clientes.

        :return: Lista de clientes
        """
        return [
            {
                "id": cliente.id,
                "nombre": cliente.nombre,
                "productos": cliente.productos,
                "correo": cliente.correo,
                "tel": cliente.tel,
            }
            for cliente in self.clientes
        ]
    
    def crear_pedidos(self, cliente,nombre,estado, ingrediente):
        Pedido = Producto(cliente,nombre,estado, ingrediente)
        AgenteComercial.Pedidos.append(Pedido)

        
