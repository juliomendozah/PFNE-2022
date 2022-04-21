"""
Topic: File Access
Author: Julio Mendoza
"""
file=open("devices.txt","r")
#print(type(file))
#print(file)
print("Lista de dispositivos")
dispositivos={"Router":[],"Switch":[],"Phone":[],"Security":[],"Meraki":[],"Catalyst":[],"Nexus":[]}
for item in file:
    item=item.strip()
    print(item)
    for tipo in dispositivos.keys():
        if tipo in item:
            dispositivos[tipo].append(item)
        """if "Router" in item:
            dispositivos["Routers"].append(item)
        elif "Switch" in item:
            dispositivos["Switches"].append(item)
        elif "Phone" in item:
            dispositivos["Phones"].append(item)
        elif "Security" in item:
            dispositivos["Security"].append(item)"""
file.close()    #Siempre cerrar el archivo
print(list(dispositivos.keys()))
print(dispositivos)
