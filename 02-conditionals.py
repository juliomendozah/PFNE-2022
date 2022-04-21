"""
Topic: Conditionals
"""
user = str(input("Enter your username: "))
password = str(input("Enter your password: "))

if(user=="admin" and password=="Cisco12345"):
    print("Welcome admin")
elif(user=="guest" and password=="Cisco12345"):
    print("Welcome guest")
else:
    print("Access Denied")
