Persona=1
nPersonas=0
mayoresDeEdad=0
acumuladorDeSueldo=0
nPersonas= int(input("ingrese la cantidad de personas : "))

while Persona<=nPersonas:
    edad=int(input("ingrese la edad : "))
    Sueldo=float(input("ingrese el sueldo : "))
    acumuladorDeSueldo=acumuladorDeSueldo+Sueldo
    if edad>=18:
        mayoresDeEdad=mayoresDeEdad+1
    Persona=Persona+1
    
print("total personas mayores de edad : ",mayoresDeEdad)
print("acumulado de los sueldos : ",acumuladorDeSueldo)