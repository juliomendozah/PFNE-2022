"""
Topic: Libraries1
Author: Julio Mendoza
"""

import os #Importamos la libreria
lista=["10.96.246.1","10.96.246.2","10.96.246.3","10.96.246.4","10.96.246.5"]
#hostname = "google.com" #example
for ip in lista:

    response = os.system("ping " + ip)

    #and then check the response...
    if response == 0:
        print (ip, 'is up!')
    else:
        print (ip, 'is down!')