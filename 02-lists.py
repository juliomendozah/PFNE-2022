"""
Topic: Script Class 2
Author: Julio Mendoza
"""
paises=["Perú","Costa Rica","Ecuador","México"]
print("La variable paises es de tipo :"+ str(type(paises)))#type permite saber el tipo de dato
print("Tenemos participantes de "+ str(len(paises))+" países")
print("Los países son: ", paises)
print("Estados Unidos" in paises)
print(paises[0])
print(paises[1])
print(paises[2])
print(paises[3])
print(paises[1:3])
print(paises[1:])
print(paises[len(paises)-1])
print(paises[-1])
texto="Cisco"
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])
print(texto[1:3])
print(list(range(10)))#La función range genera una lista de números en un determinado rango
print(list(range(1,6)))
paises.append("Chile")#comando append para agregar elementos a la lista
paises.append("Argentina")
print(paises)
paises[0]="Bolivia"
print(paises)
del paises[0] #Con del se borran elementos de la lista
print(paises)
temp=["Colombia"]
temp.append(paises)
print(temp)
temp1=["Colombia"]
print(temp1)
temp1.append(paises[0])
print(temp1)
temp1.append(paises[1])
print(temp1)
temp1.append(paises[2])
print(temp1)
temp1.append(paises[3])
print(temp1)
temp1.append(paises[4])
print(temp1)

temp2=["Colombia"]+paises #concatenar listas
print(temp2)
