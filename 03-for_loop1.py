"""
Topic: For Loop 1
Author: Julio Mendoza
"""
participants=["Julio","Chrstian","Fraeyzer","Juan","Juan Diego","Miller"]

print(participants)
print("Lista de participantes:")
for participante in participants:
    print("- "+str(participante))

print(len(participants))
print(range(len(participants)))
print(list(range(len(participants))))
for i in range(len(participants)):
    print(str(i+1)+". "+str(participants[i]))

print(participants[6])