"""
Topic: While Loop 1
Author: Julio Mendoza
"""
max_intentos=5
intentos=0
while intentos<max_intentos:
    print("-----  LOGIN  -----")
    user=str(input("Ingrese su usuario: "))
    password=str(input("Password: "))
    #my_ip=str(input("Ingrese la IP a consultar: "))
    #device=str((input("Ingrese el tipo de dispositivo de red(Switch/Router): ")))

    if (user=="admin" and password=="Cisco12345"):#Credenciales correctas
        val_correctos=False #bandera o flag
        while val_correctos==False:
            print("Ingresando valores ...")
            my_ip=str(input("Ingrese la IP a consultar: "))
            device=str((input("Ingrese el tipo de dispositivo de red(Switch/Router): ")))

            if (my_ip=="192.168.0.1" and device=="Switch"):#IP y tipo de dispositivo de red
                print("This is a gateway IP.")
                val_correctos=True
                
            elif (my_ip=="192.168.0.2" and device=="Router"):
                print("This is another IP")
                val_correctos=True

            else:
                print("Datos incorrectos")
        break

    elif (user!="admin" and password!="Cisco12345"):
        print("Usuario no autorizado. Intente de nuevo")
        intentos+=1#intentos=intentos+1
        print(intentos)

print("END")