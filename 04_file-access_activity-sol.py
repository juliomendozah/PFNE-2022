
file = open("devices.txt", "a")
while True:
    newItem=str(input("Escriba un nuevo equipo: "))
    print(newItem)
    
    if newItem =="Exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()

