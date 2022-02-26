# Realizar un programa que solicite el nombre del aprendiz y la cantidad de calificaciones que se promediarán.
# Calcular el promedio, y si el promedio es mayor o igual a 70, está aprobado. En otro caso, está reprobado
# Al final deberá preguntarle al usuario si desea capturar a otro aprendiz. El programa deberá repetirse mientras la respuesta sea diferente de “No”.
# Nota: Por cada aprendiz se debe preguntar cuántas notas/calificaciones se van a promediar.


Acomulado_notas_promedio=0

opcion="si"
while opcion=="si":
    Nombre=str(input("ingrese el nombre del estudiante: "))
    Cantidad_notas=int(input("¿Cuántas calificaciones va a promediar? "))
    for i in range(Cantidad_notas):
        notas=int(input("ingrese la nota: "))
        Acomulado_notas_promedio+=(notas)/Cantidad_notas
    if Acomulado_notas_promedio>=70:
            resultado="es aprobado"
    else:
            resultado="no es aprobado"
    print("el aprendiz",Nombre, "tiene un promedio de ",Acomulado_notas_promedio,resultado)
    Acomulado_notas_promedio=0    
    opcion=str(input("¿desea capturar otro aprendiz? si o no "))
    
 
    