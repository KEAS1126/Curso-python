# 7.	Si quieres saber tu IMC (Índice de Masa Corporal), 
# divide tu peso en kilogramos entre tu estatura en metros al cuadrado. 
# Es decir, si pesas 55 Kilogramos y mides 1.60 metros, 
# la operación sería 55/(1.60x1.60), es decir 55/2.56, 
# lo que equivale a un IMC de 21.48.  
# Según la tabla a continuación, que responde a parámetros de
# la Organización Mundial de la Salud (OMS), este IMC corresponde a 
# un peso normal, como lo consigna la siguiente tabla. Con base en lo 
# anterior y la tabla, escriba un programa en Python que para N personas, 
# solicite por cada una su peso en kilogramos y su estatura, y 
# con base en estos datos calcule y muestre su IMC. 
# Según el resultado obtenido, mostrar el mensaje correspondiente, 
# como lo ilustra la tabla.
opcion="si"
while opcion=="si":
    peso=int(input("ingrese su peso "))
    altura=float(input("ingrese su altura "))
    indiceMasaCorporal=peso/(altura*altura)
    if indiceMasaCorporal<18.5:
        print("tienes bajo peso")
    elif indiceMasaCorporal >=18.5 and indiceMasaCorporal<=24.9:
        print("tu peso es normal")
    elif indiceMasaCorporal >=25 and indiceMasaCorporal<=29.5:  
        print("tienes sobrepeso")
    elif indiceMasaCorporal >=30 and indiceMasaCorporal<=39.5:
        print("tienes obesidad")
    elif indiceMasaCorporal >=40:
        print("tienes obesidad mórbida")
    print(indiceMasaCorporal)
    opcion=input("¿desea calcular otroÍndice de Masa Corporal?  ")

