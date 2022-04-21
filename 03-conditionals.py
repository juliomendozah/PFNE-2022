"""
Topic: More conditionals
Author:Julio Mendoza
"""
user=str(input("Ingrese su usuario: "))
password=str(input("Password: "))
#my_ip=str(input("Ingrese la IP a consultar: "))
#device=str((input("Ingrese el tipo de dispositivo de red(Switch/Router): ")))

if (user=="admin" and password=="Cisco12345"):#Credenciales correctas

    my_ip=str(input("Ingrese la IP a consultar: "))
    device=str((input("Ingrese el tipo de dispositivo de red(Switch/Router): ")))

    if (my_ip=="192.168.0.1" and device=="Switch"):#IP y tipo de dispositivo de red
        print("This is a gateway IP.")
    elif (my_ip=="192.168.0.2" and device=="Router"):
        print("This is another IP")
    else:
        print("Datos incorrectos")
else:
    print("Usuario no autorizado")


