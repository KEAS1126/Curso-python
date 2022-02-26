i=1
while i<=10:
    print("Kevin",i)
    i=i+1

edad=int(input("Ingrese su edad "))

while edad<18 or edad>100:
    print("Edad incorrecta.Vuelva a intentarlo")
    edad=int(input("Ingrese su edad "))


print("Edad correcta, Bienvenido al sistema")
