aviones={"A321-200":"185 pasajeros","A320-200":"220 pasajeros","A318-100":"132 pasajeros"}

print(aviones) #para acceder al diccionario completo

print(aviones["A320-200"]) #para acceder al valor de un diccionario

aviones["A330-200"]="268 pasajeros" #para agregar un un nuevo elemento
print(aviones)

del aviones["A318-100"] #para eliminar un elemento del diccionario
print(aviones)