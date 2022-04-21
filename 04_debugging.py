"""
Topic: Debugging
Author: Julio Mendoza
"""



try:
    a=int(input("Ingresa un texto: "))
    b=int(input("Ingresa un número: "))
    c=a/b
    print(c)
except TypeError:
    print("Problema con los datos ingresados")
except ValueError:
    print("Problema de valores")
except:
    print("Bug detected")
