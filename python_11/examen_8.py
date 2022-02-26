# 8.	¿Cuál es la salida que produce este bloque de código en Python? Debe mostrar la prueba de escritorio.
x=0
while x<3:
    x=x+1
else:
    for n in range(x, x+3):
        print(n)

#la variable x va iniciar en 0 
#mientras x sea menor a 3  seguira con el ciclo
#incialmente x=0 entonces cumple la condicion, 0 es menor 3 y  es cierto
#saltara a la line 4 y replazara x por 0,  x=0+1 igual 1
#ahora x vale 1 y volvera hacer el mismo ciclo, hasta que x sea mayor o igual 3
#sabemos que despues de hacer ese ciclo queda determinado en 3, 

#ya ese 3 funcionara en el ciclo for 
#tiene una funcion range(x,x+3), donde x sera remplazada por el 3 que quedo en el clicl0 while
#si hacemos las operaciones quedaria, range(3,3+3) igual a range(3,3) 
#finalmente imprimiria el ciclo for con la variable n, imprimira el range(3,3)=
#3
#4
#5

