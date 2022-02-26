otra_lista=[12,"hola",223,773.87,True]
print(otra_lista)

#append agregar elementos al final de la lista
lista=[100,8,3030,383]
lista.append(500)

lista.append(-987)
lista.append(37373)
print(lista)



#Imprima con un bucle for los números del 1 al 10
for i in range(1,6,2):#1,3,5
    print(i)





#EJERCICIOS CON BUCLE FOR - LISTAS
#1-Escriba un bucle for que imprima cada elemento de la lista
animals=["koala","cat","fox","panda","penguin","dolphin"]
for i in animals:
    print(i)
print(animals)

#2-Escriba un bucle for que imprima "Hola!" más cada nombre en la lista
#Ejemplo: "Hola!, Sam"
nombres=["Sam","Luisa","Andrea","Felipe","Claudia","Sam","Iván","Pepe"]
for nombre in nombres:
    print(nombre)



#3-Escriba un bucle for que imprima la lista y la suma de todos los números en ella
numeros=[10,50,-2,100,20,80,35]
suma=0
for x in numeros:
    suma=suma+x
    print(x)
print("La lista contiene : ",numeros)
print("La suma de los números de la lista es: ",suma)


#4-Escriba un bucle for que imprima la lista y la suma de los números mayores a 10
numeros=[10,50,-2,100,60,40,-3,0,0,-89]
suma_mayores_diez=0
contador_mayores_diez=0
contador_menor_cero=0
for i in numeros:
    print(i)
    if i>10:
        suma_mayores_diez=suma_mayores_diez+i
        contador_mayores_diez=contador_mayores_diez+1
    if i<0:
        contador_menor_cero=contador_menor_cero+1
print("La suma de los mayores a 10 es : ",suma_mayores_diez)
print("La cantidad de # mayores a 10 es : ",contador_mayores_diez)
print("Cantidad de números negativos : ",contador_menor_cero)

#5-Escriba un bucle for que agregue a una nueva lista los números de la primera
#lista multiplicados por 2. Use el método append (Agrega al final de la lista)
numeros=[-300,10,50,-2,100,4,20,80,-9]
numeros_vacios=[]
for i in numeros:
    numeros_vacios.append(i*2)
print(numeros)
print(numeros_vacios)


#6-Cree una lista vacía. Luego pida la cantidad de valores que desea ingresar
# en ella.
#Use un bucle for para cargar los números/elementos desde el teclado.
# Luego muestre la lista

lista=[]
cantidad_valores=int(input("Diga la cantidad de valores para la lista:"))#3
for i in range(cantidad_valores):
    numero=input("Ingrese un valor numérico : ")#56 - 90 - 7
    lista.append(numero)
print(lista)


#7-Analice el siguiente código y diga qué hace
lista=[]
valor=int(input("Ingresar valor (0 para finalizar):")) #3
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))#89 -6  0

print("Tamano de la lista:")
print(len(lista)) #3
print(lista)

#8-Analice el siguiente código y explique qué hace
mi_lista = []

for num in range(10, 100, 10):#10,20,30....90
	mi_lista.append(num)
print(mi_lista)
#[3, 5, 7, 9, 11, 13,]


