from Nodo import *

class Arbol_Binario_Busqueda:
    __raiz: object
    
    def __init__(self):
        self.__raiz = None
    
    def Vacio(self):
        return self.__raiz == None
        
    def Insertar(self, x):
        if (self.__raiz == None):
            self.__raiz = Nodo(x)
        else:
            nodo = self.__raiz
            self.Insertar_Recursivo(x, nodo)
    
    def Insertar_Recursivo(self, x, nodo):
        if (nodo.getDato() == x):
            print("El elemento ya esta en el arbol")
        else:
            if (nodo.getDato() > x):
                if (nodo.getIzq() == None):
                    nodo.setIzq(Nodo(x))
                else:
                    self.Insertar_Recursivo(x, nodo.getIzq())
            else:
                if (nodo.getDer() == None):
                    nodo.setDer(Nodo(x))
                else:
                    self.Insertar_Recursivo(x, nodo.getDer())
    
    def Suprimir(self, x):
        nodo = self.__raiz
        self.Suprimir_Recursivo(x, nodo)
    
    def Suprimir_Recursivo(self, x, nodo):
        if (nodo == None):
            print("El elemento no esta en el arbol")
            return nodo
        else:
            if (x < nodo.getDato()):
                nodo.setIzq(self.Suprimir_Recursivo(x, nodo.getIzq()))
            else:
                if(x > nodo.getDato()):
                    nodo.setDer(self.Suprimir_Recursivo(x, nodo.getDer()))
                else:
                    if (nodo.getIzq() == None):
                        return nodo.getDer() 
                    else:
                        if (nodo.getDer() == None):
                            return nodo.getIzq()
                    cambio = self.Busca_Menor_Derecho(nodo.getDer())
                    nodo.setDato(cambio.getDato())
                    nodo.setDer(self.Suprimir_Recursivo(cambio.getDato(), nodo.getDer()))
        return nodo
                        
    def Busca_Menor_Derecho(self, nodo):
        while (nodo.getIzq() != None):
            nodo = nodo.getIzq()
        return nodo
    

    def In_Orden(self):
        nodo = self.__raiz
        self.In_Orden_Recursivo(nodo)

    def In_Orden_Recursivo(self, nodo):
        if (nodo != None):
            self.In_Orden_Recursivo(nodo.getIzq())
            print(nodo.getDato(), end = ' ' )
            self.In_Orden_Recursivo(nodo.getDer())
    
    
    def Pre_Orden(self):
        nodo = self.__raiz
        self.Pre_Orden_Recursivo(nodo)
        
    def Pre_Orden_Recursivo(self, nodo):
        if (nodo != None):
            print(nodo.getDato(), end = ' ' )
            self.Pre_Orden_Recursivo(nodo.getIzq())
            self.Pre_Orden_Recursivo(nodo.getDer())
        
    
    def Post_Orden(self):
        nodo = self.__raiz
        self.Post_Orden_Recursivo(nodo)
        
    def Post_Orden_Recursivo(self, nodo):
        if(nodo != None):
            self.Post_Orden_Recursivo(nodo.getIzq())
            self.Post_Orden_Recursivo(nodo.getDer())
            print(nodo.getDato(), end = ' ' )