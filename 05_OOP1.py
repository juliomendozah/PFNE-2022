"""
Topic: OOP1
Author: Julio Mendoza
"""

class Equipo_Red(object):
    def __init__(self,IP,device):
        self.IP=IP
        self.device=device
    def mandar_ping(self,IP_destino):
        comando="Enviando ping desde "+str(self.IP)+" hasta "+IP_destino
        return comando

dispositivo=Equipo_Red("192.168.100.20", "Switch")
print(dispositivo)
print("ATRIBUTOS")
print(dispositivo.device)
print(dispositivo.IP)
print("MÉTODOS:")
com= dispositivo.mandar_ping("8.8.8.8")
print(com)
dispositivo2=Equipo_Red("192.168.100.21", "Switch")
lista_disp=[dispositivo,dispositivo2]
print("LISTA DE OBJETOS:")
print(lista_disp)
for item in lista_disp:
    com= item.mandar_ping("8.8.8.8")
    print(com)

