#! /usr/bin/python3

def factorial(n):
    """factorial recursivo"""
    if n == 0: return 1
    if n == 1: return 1
    return n * factorial(n-1)
 
if __name__ == "__main__":
    
    x = 3
    print(factorial(x)) # 6
    
    x = 2
    print(factorial(x)) # 2

    x = 1
    print(factorial(x)) # 1
    
    x = 0
    print(factorial(x)) # 0
    
    