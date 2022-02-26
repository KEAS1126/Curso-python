# 6.	Analice el siguiente pseudocódigo, diga qué resultado produce, y 
# por último compruebe su respuesta codificándolo en Python.
# INICIO
# NUMBER num, result=0, counter

# OUTPUT "Enter a number for calculate the power of the number" 
# INPUT num
 
# FOR counter=0 TO num STEP 1 DO
#      result +=num
# ENDFOR
 
# OUTPUT "Power of the Number:" + result 

# FIN

num=int(input("ingrese el numero "))
result=0
for contador in range(num):
    result+=num

print("la potencia del numero ",result)


