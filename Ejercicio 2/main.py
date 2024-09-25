from ArbolBB import *

#mostrar padre y hermano, el nodo puede no existir
#mostrar cantidad de nodos en forma recursiva
#mostrar altura
#mostrar sucesores de un nodo

if __name__ == '__main__':
    arbol = Arbol_Binario_Busqueda()
    arbol.Insertar(5)
    arbol.Insertar(2)
    arbol.Insertar(7)
    arbol.Insertar(9)
    arbol.Insertar(3)
    arbol.Insertar(1)
    arbol.Insertar(11)
    arbol.Insertar(12)
    arbol.Insertar(10)
    arbol.In_Orden()
    print(" ")
    arbol.Padre_Hermano(9)
    c= arbol.Cantidad_Nodos()
    print(f"Cantidad de nodos: {c}")
    altura = arbol.Altura()
    print(f"Altura del arbol: {altura}")
    arbol.Sucesores(2)