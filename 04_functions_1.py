"""
Topic: Functions 1
Author: Julio Mendoza
"""
TOKEN="asdf12345"
def sumar(a,b,texto):
    suma=a+b
    print(TOKEN)
    print(texto+" : "+str(suma))
    return suma
def ingresar_valores():
    a=int(input("a: "))
    b=int(input("b: "))
    c=int(input("c: "))
    d=int(input("d: "))
    e="Hola"
    f=True
    return a,b,c,d,e,f
#Main
a,b,c,d,e,f=ingresar_valores()#a,b,c,d es una tupla
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
x=sumar(a,b,"a+b")
y=sumar(c,d,"c+d")