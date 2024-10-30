#! /usr/bin/python3

def imprime(lista):
    """impresion recursiva de una lista
    con enfoque primero; restantes"""
    print("<", end="")
    if len(lista) == 0:
        print(">", end="")
        return
    primero = lista[0]
    listaRestantes = lista[1:]
    print(primero, end=", ")
    imprime(listaRestantes)
    print(">", end="")    
 
 
if __name__ == "__main__":
    
    l = [33,22,11]
    imprime(l)
    
    # l = [33,22]
    # imprime(l)

    # l = [33]
    # imprime(l)
    
    # l = []
    # imprime(l)
    
    