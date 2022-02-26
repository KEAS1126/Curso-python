
autos=["Mazda","Nisssan","Honda","Mercedez"]

print(autos[:]) #mi lista completa
print(autos[2]) #indice de la lista, desde 0, 1, 2....
print(autos[1:3]) #acceder a una porcion de la lista
print(autos[-2]) #accede  accededesde el ultimo valor -1, -2, -3....

autos.append("Hyundai") #para agregar un valor en el ultimo indice de la lista
print(autos[:])

autos.insert(2,"Mitsubishi") #para agregar un valor en un indice correspondiente
print(autos[:])

autos.extend(["Lamborghini","Ferrari","Porsche"]) #para agregar varios elementos a una lista
print(autos[:])

print(autos.index("Lamborghini")) #para saber en que indice esta un elemento de la lista

print("Ferrari" in autos) #para seber si un elemento de la lista se encuentra

autos.remove("Mazda") #para eliminar un elemento de la lista
print(autos[:])

autos.pop() #para eliminar el ultimo elemento de la lista
print(autos[:])

