"""
Topic: Functions 2
Author: Julio Mendoza
"""

def ingresar_IP():
    ip=str(input("Ingresa la IP: "))
    return ip

def mandar_comando(ip):
    comando="ping " + ip
    return comando

def funcion_principal():
#main
    ip=ingresar_IP()
    if ip == "192.168.100.15":
        comando=mandar_comando(ip)
        respuesta="Todo OK"
        print(comando)
    else:
        print("Te has equivocado de IP")
        respuesta="Todo mal"
    return respuesta

respuesta= funcion_principal()
print(respuesta)


