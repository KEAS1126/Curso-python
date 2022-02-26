

#una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
#(4 por la mañana y 4 por la tarde). Escriba un programa que permita almacenar
#los sueldos de los empleados agrupados en dos listas.
#Imprimir las dos listas de sueldos.

list_morning=[]


list_afternoon=[]
number_workers_morning = 4
number_workers_afternoon = 4

# INPUTS
for i in range(0,number_workers_morning):
    list_morning.append(input("ingrese el valor del sueldo(mañana): "))

for i in range(0,number_workers_afternoon):
    list_afternoon.append(input("ingrese el valor del sueldo(tarde): "))

# OUTPUTS
print(list_morning)
print(list_afternoon)


