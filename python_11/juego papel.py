import random

nombres=["Juan", "Carlos", "Pedro"]
d=["piedra","papel","tijera"]

Nombre1=input("ingrese su nombre ")

op="si"

while op=="si":
    Nombre2=random.choice(nombres)

    jugador1=input(Nombre1+" ingrese piedra, papel o tijera: ")
    jugador2=random.choice(d)

    print(Nombre2+" "+"eligio"+" "+jugador2)
    if jugador1 == d[0] and jugador2 == d[1]:
        print("Gano "+Nombre2)
    elif jugador1 == d[1] and jugador2 == d[0]:
        print("Gano "+Nombre1)
    elif jugador1== d[0] and jugador2==d[2]:
        print("Gano "+Nombre1)
    elif jugador1== d[2] and jugador2==d[0]:
        print("Gano "+Nombre2)
    elif jugador1== d[1] and jugador2==d[2]:
        print("Gano "+Nombre2)
    elif jugador1== d[2] and jugador2==d[1]:
        print("Gano "+Nombre1)
    elif (jugador1== d[0] and jugador2==d[0])or(jugador1== d[1] and jugador2==d[1])or(jugador1== d[2] and jugador2==d[2]):
        print("Empate")
    else:
        print("ERROR")

    op=input("¿desea jugar otra vez?")
        
