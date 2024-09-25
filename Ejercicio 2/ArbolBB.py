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
                    if (nodo.grado() == 0):
                        return None
                    else:
                        if (nodo.grado() == 1):
                            if (nodo.getIzq() == None):
                                return nodo.getDer() 
                            else:
                                return nodo.getIzq()
                        else:
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
            
    
    def Padre_Hermano(self, x):
        nodo = self.__raiz
        if (nodo.getDato() == x):
            print("El nodo ingresado es la raiz, no tiene padre ni hermano")
        else:
            padre = self.Padre_Recursivo(nodo, x)
            if (padre == None):
                print ("El nodo ingresado no existe")
            else:
                print(f"El padre del nodo Ingresado es: {padre.getDato()}")
                if (padre.Grado() == 2):
                    if (padre.getIzq().getDato() == x):
                        print(f"El hermano del nodo es: {padre.getDer().getDato()}")
                    else:
                        print(f"El hermano del nodo es: {padre.getIzq().getDato()}")
                else:
                    print("El nodo no tiene hermano")
        
    
    def Padre_Recursivo(self, nodo, x):
        if (nodo.Grado() == 0) and (nodo.getDato() != x):
            return None
        if (x < nodo.getDato()):
            if (nodo.getIzq().getDato() == x):
                return nodo
            else:
                return self.Padre_Recursivo(nodo.getIzq(), x)
        else:
            if (nodo.getDer().getDato() == x):
                return nodo
            else:
                return self.Padre_Recursivo(nodo.getDer(), x)
    
    
    def Cantidad_Nodos(self):
        nodo = self.__raiz
        cant = self.Cant_Nodos_Recursivo(nodo)
        return cant

    def Cant_Nodos_Recursivo(self, nodo):
        if (nodo != None):
            return (1 + self.Cant_Nodos_Recursivo(nodo.getIzq()) + self.Cant_Nodos_Recursivo(nodo.getDer()))
        else:
            return 0
    
    
    def Altura(self):
        nodo = self.__raiz
        altura = self.Altura_Recursiva(nodo)
        return altura
    
    def Altura_Recursiva(self, nodo):
        if (nodo == None):
            return 0
        else:
            Izquierda = self.Altura_Recursiva(nodo.getIzq())
            Derecha = self.Altura_Recursiva(nodo.getDer())
        altura = 1 + max(Izquierda, Derecha)
        return altura
    
    def Sucesores(self, x):
        nodo = self.__raiz
        self.Sucesores_Recursivo(nodo, x)
    
    def Sucesores_Recursivo(self, nodo, x):
        if (nodo == None):
            print("El nodo ingresado no existe")
        else:
            if (nodo.getDato() == x):
                if (nodo.Grado() == 0):
                    print("El nodo ingresado es hoja")
                else:
                    print(f"Los hijos son:\n Izquierdo: {nodo.getIzq().getDato()}\n Derecho: {nodo.getDer().getDato()}")
            else:
                if (x < nodo.getDato()):
                    self.Sucesores_Recursivo(nodo.getIzq(), x)
                else:
                    self.Sucesores_Recursivo(nodo.getDer(), x)
