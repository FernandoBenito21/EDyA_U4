class Nodo:
    __dato : int
    __izq : object
    __der : object
    
    def __init__(self, dato):
        self.__dato = dato
        self.__izq = None
        self.__der = None
    
    def setDato(self, x):
        self.__dato = x
        
    def getDato(self):
        return self.__dato
    
    def setIzq(self, i):
        self.__izq = i
    
    def getIzq(self):
        return self.__izq
    
    def setDer(self, d):
        self.__der = d
    
    def getDer(self):
        return self.__der