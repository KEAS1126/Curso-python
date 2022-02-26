salario_presidente=int(input("Introduce salario presidente: "))
print("Salario presidente: "+str(salario_presidente))  #para convertir una variable se colocar el tipo  
                                                       #y entre parentesis el nombre de la variable

salario_director=int(input("Introduce salario director: "))
print("Salario director: "+str(salario_director))

salario_jefe_area=int(input("Introduce salario jefe area: "))
print("Salario jefe area: "+str(salario_jefe_area))

salario_administractivo=int(input("Introduce salario administractivo: "))
print("Salario administractivo: "+str(salario_administractivo))

if salario_administractivo<salario_jefe_area<salario_director<salario_presidente: #concatenacion de  operadores de comparacion
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")