class Pedido:
    Contador = 0
    def __init__(self,cliente,producto = None, descripcion= None):
        self._cliente = cliente
        self._producto = producto
        self._descripcion = descripcion
        self._id = Pedido.Contador
        Pedido.Contador +=1

     
        
