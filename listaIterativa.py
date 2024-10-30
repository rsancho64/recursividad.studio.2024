#! /usr/bin/python3

def imprime(lista):
    """impresion iterativa de una lista
    con enfoque primero; restantes"""
    print("<", end="")
    print(lista[0], end="")
    listaRestantes = lista[1:]
    while listaRestantes != 0:
        primero = listaRestantes[0]
        print("<", end="")
        listaRestantes = listaRestantes[1:]
        print(">", end="")

 
if __name__ == "__main__":
    
    l = [33,22,11]
    imprime(l)
    
    
    