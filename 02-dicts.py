"""
Topic: Dictionaries
Author: Julio Mendoza
"""
participantes={"Perú":["Julio","Fraeyzer","Kleider","Miller","Juan"],"Costa Rica":["Alex","Juan Diego"],"México":["Christian"]}
print("Costa Rica: " ,participantes["Costa Rica"])
print("Perú: " ,participantes["Perú"])
print("México: " ,participantes["México"])

print(participantes.keys())
print(type(participantes.keys()))
print(list(participantes.keys()))

print(participantes.values())
print(type(participantes.values()))
print(list(participantes.values()))
participantes["Portugal"]=["Cristiano Ronaldo"]
print(participantes)
print("México" in participantes)#Con in se puede saber si un elemento está en la lista o diccionario
print("Mexico" in participantes)

print("Mi nombre: "+participantes["Perú"][0])
print("Julio" in participantes["Perú"])
print("a" in participantes["Perú"][0])
