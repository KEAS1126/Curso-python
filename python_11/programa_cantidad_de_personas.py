#escribir un programa que pida una cantidad de personas, 
#pida la edad de cada uno
#pida el sueldo de cada uno
#y al final le muestre al usuario cuantas personas  son mayores de edad y 
# el promedio de los sueldos

persona=0
numero_pesonas_mayores_edad=0
numero_sueldos=0
cantidad_de_personas=int(input("ingrese la cantidad de personas: "))


while persona<cantidad_de_personas:
    edad=int(input("ingrese la edad la persona: "))
    sueldo=float(input("ingrese el sueldo de la persona: "))
    persona+=1
    
    if edad>18:
        numero_pesonas_mayores_edad+=1

    numero_sueldos+=sueldo
    promedio=numero_sueldos/cantidad_de_personas


print("perosonas mayores de edad: ",numero_pesonas_mayores_edad,"promedio de sueldos: ",promedio )






