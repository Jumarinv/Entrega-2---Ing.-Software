import pickle


class Deserializador():
    @staticmethod
    def deserializar(nombre, listaSet):

        picklefile = open(f'src/baseDatos/temp/{nombre}.txt', 'rb') # Abrir la ruta de nuestro archivo
        
        objetos = pickle.load(picklefile) # Deserializar la lista
        
        listaSet(objetos) # Aplicar el Seteo de los objetos
        #print(objetos)
        picklefile.close() # Cerrar el archivo

    @staticmethod
    def deserializarListas():
        # Comentadas temporalmente hasta tener la lógica funcionando

        #Deserializador.deserializar("NombreEjemplo", Clase.getLista())
        pass


