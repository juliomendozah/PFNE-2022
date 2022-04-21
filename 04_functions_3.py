"""
Topic: Functions 3
Author: Julio Mendoza
"""
import funciones as fcs #fcs.leer_archivo(filename)
#from funciones import leer_archivo #leer_archivo(filename)
#import funciones    #funciones.leer_archivo(filename)

lista_ips=[]
headers={"tipo":"json",
        "token":"Cisco12345"}

def llenar_lista_ips():
    ip=str(input("Ingresar IP: "))
    lista_ips.append(ip)

def enviar_mensaje_webex(mensaje):
    print("Enviando mensaje ...")
    trama=" Se enviara un mensaje tipo " + headers["tipo"] + " con token: "+ headers["token"]+". El contenido es: Nueva IP: "+mensaje
    print(trama)

def escribir_archivo(contenido):
    archivo=open("lista_ips.txt","a")#abre el archivo y lo pone en modo de agregar 
    archivo.write(contenido + "\n")
    archivo.close()
"""
def leer_archivo(filename):
    file=open(filename,"r")
    for item in file:
        item=item.strip()
        print(item)
"""
for i in range(1):
    llenar_lista_ips()

for ip in lista_ips:
    enviar_mensaje_webex(ip)
    escribir_archivo(ip)

#leer_archivo("lista_ips.txt")
fcs.leer_archivo("lista_ips.txt")

print(lista_ips)