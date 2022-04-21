"""
Topic: For Loop 2
Author: Julio Mendoza
"""
IP_list=["192.168.0.1",
        "192.168.0.2",
        "192.168.0.3",
        "192.168.0.4",
        "192.168.0.5"]
estado_IPs={"Buenas":[],"Malas":[]}
print("Chekeando conectividad...")
for IP in IP_list:
    print("ping "+str(IP))
    connectivity=str(input("Hay conexión?: [Sí/No]"))
    if (connectivity=="Sí"):
        print("Todo OK")
        estado_IPs["Buenas"].append(IP)
    else:
        print("Todo mal")
        estado_IPs["Malas"].append(IP)

print("Resultados:")
print("Buenas: ", estado_IPs["Buenas"])
print("Malas: ",estado_IPs["Malas"])