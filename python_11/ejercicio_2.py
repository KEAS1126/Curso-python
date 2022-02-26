
etiqueta1= str(input("Ingrese la etiqueta 1 "))
etiqueta2= str(input("Ingrese la etiqueta 2 "))
etiqueta3= str(input("Ingrese la etiqueta 3 "))


PRECIO_ETIQUETA_AMARILLA=100
PRECIO_ETIQUETA_ROJA=90


if etiqueta1=="Amarilla"and etiqueta2=="Roja" and etiqueta3== "Roja":
    total= (PRECIO_ETIQUETA_AMARILLA+PRECIO_ETIQUETA_ROJA+PRECIO_ETIQUETA_ROJA)/2
    print("Felicitaciones señor usuario puede acceder a la super oferta de la libreria", "Precio total: ",total)
    

elif etiqueta1=="Amarilla"and etiqueta2=="Amarilla" and etiqueta3== "Roja":
    total= PRECIO_ETIQUETA_AMARILLA+(PRECIO_ETIQUETA_ROJA+PRECIO_ETIQUETA_ROJA)/2
    print("Solo uno de los libros adicionales aplica para la oferta", "Precio total: ", total)
    

elif etiqueta1=="Amarilla" and etiqueta2=="Amarilla" and etiqueta3=="Amarilla":
    total= PRECIO_ETIQUETA_AMARILLA+ PRECIO_ETIQUETA_ROJA+PRECIO_ETIQUETA_ROJA
    print("Ninguno de los libros aplica para la oferta", "Precio total: ", total)
    

else:
    print("No aplica para la oferta")



    









