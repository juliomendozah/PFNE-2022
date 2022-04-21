"""
Topic:User Input
Author: Julio Mendoza
"""

mi_ip=str(input("Ingresa tu IP: "))
print("Tu IP es " + mi_ip)
nro_host=int(input("Número de host: "))
print(mi_ip == "8.8.8.8")
print(nro_host == 254)
print(mi_ip == "8.8.8.8" or mi_ip =="0.0.0.0")
acceso=(mi_ip =="0.0.0.0" and nro_host == 254)
print(acceso)