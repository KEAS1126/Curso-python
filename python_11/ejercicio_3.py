
Salario_minimo=float(877803.00)
Descuento_seguridad_social=float(0.08)
Bonificacion=float(0.02)

Horas_trabajadas=float(input("ingrese las horas trabajadas"))
Valor_hora=float(input("ingrese el valor de la horas trabajadas"))

Sueldo=Horas_trabajadas*Valor_hora


Descuento=Sueldo*Descuento_seguridad_social
Sueldo_total=Sueldo-Descuento


if Sueldo_total< (Salario_minimo/2):
    sueldo_con_Bonificacion=(Bonificacion*Sueldo)+Sueldo_total
    print("el sueldo con bonificion: ",sueldo_con_Bonificacion)
else: print(Sueldo_total)




    










