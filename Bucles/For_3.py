for i in range(5):   #rango para hacer un conte 0 a 4 
    print(i,"hola")

print("--------------------------------------------")

for i in range(10):
    print(f"gracias, Amo la aviacion {i}")

print("--------------------------------------------")

for i in range(7,100,2): #los dos primeros valores te dice que rango se quiere, el tercero te cuenta, 
                         #en este de dos en dos
    print(i)

print("--------------------------------------------")

valido=False
Email=input("Introduce tu email")

for i in range(len(Email)):
    if Email[i]=="@":
        valido=True

if valido:
    print("Email correcto")

else:
    print("Email incorrecto")

