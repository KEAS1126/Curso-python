Notas=1
Notas_acomuladas=0
Numero_de_notas=0
promedio=0
Cantidad_de_notas=0
opcion="si"
while opcion =="si":
    Nombre=str(input("ingrese su nombre: "))
    Numero_de_notas=int(input("ingrese el numero de nota: "))
    while Notas<=Numero_de_notas:
        Notas=Notas+1
        Cantidad_de_notas=float(input("ingrese la nota: "))
        Notas_acomuladas= Notas_acomuladas + Cantidad_de_notas
        Promedio=Notas_acomuladas /Numero_de_notas
        if Promedio>=70.0:
            print(Nombre,"es aprobado","nota: ",Promedio)
        else:print(Nombre,"no aprobado","nota: ",Promedio)
    Notas=1
    Notas_acomuladas=0
    Numero_de_notas=0
    promedio=0
    Cantidad_de_notas=0
    opcion=str(input("desea capturar otro aprendiz: "))


    