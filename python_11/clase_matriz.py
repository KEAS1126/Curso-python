aprendices=[["Jorge","Kevin"],["Anyela","Juan"]]

notas=[[6,9,18,9],
       [6,19,17,9],
       [8,9,7,30]]
f=3
c=4
#imprimir la matriz
for m in notas:
    print(m)

#Imprimir la matriz recorriendo elemento por elemento
#necesitamos hacerlo con 2 bucles for
#El primero para recorrer la fila y el segundo para las columnas

def imprimirMatriz(matriz,filas,columnas):
    print("\nContenido de la matriz ")
    for fila in range(filas):#bucle para las filas...desde 0 hasta 2 (0,1,2)
        for columna in range(columnas): # desde 0 hasta 3 (0,1,2,3)
            print(matriz[fila][columna],end=" ")
        print()

#función para calcular la nota promedio del grupo
def notaPromedio(matriz,filas,columnas):
    suma=0
    nota_promedio=0
    for fila in range(filas):
        for columna in range(columnas):
           suma=suma+matriz[fila][columna]
    nota_promedio=suma/(filas*columnas)#Calculamos el promedio---- 3x4 = 12
    return nota_promedio

def notaPorEstudiante(matriz,filas,columnas):

    print("\nNota promedio de cada estudiante")
    for f in range(filas):
        nota_final = 0
        for c in range(columnas):
            print(matriz[f][c],end=" ")
            nota_final=nota_final+matriz[f][c]
        print()
        print("Nota final : ",nota_final/len(matriz[f]))#Aquí conocer cuántas columnas tiene la fila

def notaMayor(matriz,filas,columnas):
    mayor=matriz[0][0]
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] > mayor:
                mayor=matriz[f][c]
    return mayor


#llamar a la funcióm imprimirMatriz
imprimirMatriz(notas,f,c)
imprimirMatriz(aprendices,2,2)

nota_promedio=notaPromedio(notas,3,4)#llamada a la función notaPromedio
print("La nota promedio del grupo es ",nota_promedio)

notaPorEstudiante(notas,f,c)

nota_mayor=notaMayor(notas,f,c)
print("La mayor nota en el grupo es ",nota_mayor)


#El trimestre termina el 30 de sep
#Nos quedan 2 encuentros presenciales - 21 y 28

#última evidencia de algoritmos
# Desde condicionales hasta matrices...if...elif..else...for...while...def...listas(matrices)

#1 Teoría
#2 Caso de estudio
#3 Otros

#El jueves vamos a iniciar con el tema de POO-conceptos básicos