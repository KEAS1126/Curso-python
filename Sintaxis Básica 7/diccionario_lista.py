#un diccionario con listas dentro

aviones={"Airbus":["A318","A319","A320","A321"],"Boeing":["B727","B737","B747","B757"]}  
print(aviones)
print(aviones["Airbus"])

#un diccionario dentro de un diccionario

aviones={"Airbus":["A318","A319","A320","A321"],"Boeing":{"Clases":["B727","B737","B747","B757"]}}  
print(aviones)
print(aviones["Airbus"])
print(aviones["Boeing"])

#llaves de los diccionarios

print(aviones.keys()) 

#valores de los diccionarios

print(aviones.values())

#longitud del diccionario

print(len(aviones))