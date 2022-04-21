"""
Topic: OOP2
Author: Julio Mendoza
"""

class Equipo_Red(object):
    def __init__(self,IP,device):
        self.IP=IP
        self.device=device
    def mandar_ping(self,other_device):
        print("Enviando ping desde "+str(self.IP)+" hasta "+other_device.IP)

class Mandar_alertas(Equipo_Red):
    def __init__(self,alerta):
        self.alerta=alerta

    def mandar_mensaje(self,mensaje):
        print(mensaje+": "+self.alerta)

switch=Equipo_Red("10.96.246.2", "Switch")
print(switch)
print(type(switch))
print(switch.IP)
print(switch.device)
router=Equipo_Red("10.96.246.1", "Router")
print(router.IP)
print(router.device)
switch.mandar_ping(router)
router.mandar_ping(switch)

test=Mandar_alertas("Shutdown")
test.mandar_mensaje("SOS")