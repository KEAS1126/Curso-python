matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
for fila in range(3):
    for columna in range(3):
        print(matriz[fila][columna],end="")
    print("")
print(matriz[1,2])