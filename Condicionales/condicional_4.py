USUARIO=["KEAS1126"]
CONTRASEÑA=["kevin1126"]

usuario=input("Ingrese usuario ")
contraseña=input("ingrese su contraseña ")

if USUARIO[0]==usuario and CONTRASEÑA[0]==contraseña:
    print("usuario y contraseña correctos")
else:
    print("contraseña incorrecta")

autos=["mazda","nissan","ferrari","honda","mercede","toyota"]

auto=input("¿Que auto desea? ")
concesionario=auto.lower()

if concesionario in autos:
    print("Tenemos el auto")
else:
    print("no tenemos el auto")

