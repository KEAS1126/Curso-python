# Realice un algoritmo que determine el sueldo semanal de N trabajadores considerando que se les descuenta 5% 
# de su sueldo si ganan entre 0 y 150000 pesos. Se les descuenta 7% 
# si ganan más de 150000 pero menos de 300000, y 9% si ganan más de 
# 300000 pero menos de 450000. Los datos de entrada son: horas 
# trabajadas, sueldo por hora y nombre de cada trabajador. 
# Datos de prueba
# Horas trabajadas: 30
# Sueldo por hora: 12000
# Nombre del trabajador: Juan Pérez
# Sueldo: 360000
# Descuento: 32400
# Sueldo semanal: 327600

# Datos de prueba
# Horas trabajadas: 18
# Sueldo por hora: 12000
# Nombre del trabajador: Juana Rodríguez
# Sueldo: 216000
# Descuento: 15120
# Sueldo semanal: 200880

Opcion="si"
while Opcion=="si":


    Nombre_trabajador=str(input("ingrese el nombre del trabajador: "))
    Horas_trabajadas=int(input("ingrese las horas trabajadas: "))
    Valor_hora=12000*Horas_trabajadas
    print(Valor_hora)
    if Valor_hora<=150000:
        Descuento=Valor_hora*0.95
    elif Valor_hora>150000 and Valor_hora<300000:
        Descuento=Valor_hora*0.93
    elif Valor_hora>300000 and Valor_hora<450000:
        Descuento=Valor_hora*0.91


    print(Nombre_trabajador,"Su sueldo semanal es: ",Descuento)
    Opcion=input(str("desea mi un sueldo mas"))