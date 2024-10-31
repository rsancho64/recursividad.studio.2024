#! /usr/bin/python3

"""lista iterativa
   RSA oct 2024
"""

def imprime(lista):
    """impresion iterativa de una lista
    con enfoque primero+restantes"""
    print(f"( ", end="")
    while len(lista):
        print(f"{lista[0]} ", end="")
        lista = lista[1:]
    print(f")")


if __name__ == "__main__":
    
    l = [33,22,11]
    imprime(l)
    print()    
    
    