
# 2.	Escriba un programa que, primero valide el nombre de un usuario y su contraseña. 
# El número de intentos máximo es de tres. 
# Por cada fallo, se debe mostrar el mensaje 
# “Credenciales incorrectas”. Al tercer fallo, 
# el programa debe mostrar en mensaje 
# “Ha agotado la cantidad de intentos. Por favor inicie de nuevo el programa”, 
# y terminar la ejecución del programa. 
# Una vez los datos sean válidos en cualquiera de los intentos (1, 2 o 3),
#  se debe mostrar un menú con las siguientes opciones, como se ilustra:

# Usuario: admin
# Contraseña: AdsiSena2021
# ***** Menú de registro de personal y números *****
# 1.	Registrar empleados
# 2.	Ver empleados registrados
# 3.	Registrar valores numéricos decimales
# 4.	Ver la suma de los valores decimales
# 5.	Salir

# Se deben ingresar empleados y valores numéricos hasta que 
# el usuario seleccione la opción correspondiente a Salir. 
# Al ingresar la opción 5, el programa debe mostrar el mensaje 
# “Hasta luego” y terminar su ejecución.

Intentos=0
opcion="no"
suma_decimales=0
registros=[]
while Intentos<3:
    Usuario=input("ingrese el nombre del usuario ")
    Clave=input("ingrese su clave ")
    Intentos+=1
    
    if Usuario=="admin" and Clave=="AdsiSena2021" :
            print("Usuario y Clave correcta")
            print("Bienviendo admin")
            break
                
    else:
        print("Credenciales incorrectas")
    
        
    if Intentos==3:
        print("Ha agotado la cantidad de intentos. Por favor inicie de nuevo el programa") 
        break

  

while opcion=="no":
     
    print("1.Registrar empleados")
    print("2.Ver empleados registrados")
    print("3.Registrar valores numéricos decimales")
    print("4.Ver la suma de los valores decimales")
    print("5.Salir")
    op = input("Ingrese el número de la opción del menú deseada: ")
    if op=="1":
        registro_empleados=str(input("ingrese el nombre de la persona "))
        registros.append(registro_empleados)
    elif op=="2":
            print(registros)
    elif op=="3":
        decimal=float(input("ingrese un valor decimal "))
    elif op=="4":
        suma_decimales+=decimal
        print(suma_decimales)
    elif op=="5":
        opcion=str(input("¿desea salir del programa? si o no"))
        print("hasta luego,la virgen  acompañe")
    

         
