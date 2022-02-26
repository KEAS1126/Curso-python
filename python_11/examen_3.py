# 3.	Realice la prueba de escritorio para las siguientes líneas de código y diga 
# qué salidas produce:
for num in range(1,10):

    if num % 15==0:
        print("DíaNoche")
    elif num % 3==0:
        print("Día")
    elif num % 5==0:
        print("Noche")
    else:
        print(num)

#tenemos un ciclo for el cual contienen un iterador con el nombre de num
#en el se tiene un rango de 1 al 9
#se tiene un condicional el cual evaluara el iterador num   de tres maneras:
#si num modulo 15 es igual 0, imprimir "DiaNoche"
#si num modulo 3 es igual 0, imprimir "Dia"
#si num modulo 5 es igual 0, imprimir "noche"
#sino imprimir num


        

