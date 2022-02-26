costo=float(input("ingrese el valor "))
marca=str(input("ingrese la marca "))
if costo>=2000 and marca=="SONY":
    precio_articulo=costo*0.90
    precio_total=precio_articulo*0.95
    print("usted pagara: " ,precio_total, "soles")

if costo>=2000 and marca!="SONY":
    precio_total=costo*0.90
    print("usted pagara: ",precio_total, "soles")
    
if costo<2000 and marca=="SONY":
    precio_articulo=costo*0.95
    precio_total=precio_articulo+precio_articulo*0.20
    print("usted pagara: ",precio_total, "soles")

if costo<2000 and marca!="SONY":
    precio_total=costo*1.20
    print("usted pagara: ",precio_total, "soles")







    










