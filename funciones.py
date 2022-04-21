"""
Topic: Functions misc
Author: Julio Mendoza
"""

def leer_archivo(filename):
    file=open(filename,"r")
    for item in file:
        item=item.strip()
        print(item)
        