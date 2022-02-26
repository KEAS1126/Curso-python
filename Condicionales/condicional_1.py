print("Programa de evaluacion de notas de alumnos")
nota_alumno=int(input("introduce la nota del alumno "))

def evaluacion(nota):
    valoracion="abrobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(nota_alumno))