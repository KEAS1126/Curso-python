for i in [1,2,3]:
    print(i, end=" ") #para que no haga salto de linea

print("--------------------------------------------")

email=False
for i in "kevin.arroyave@misena.edu.co":
    if i=="@":
        email=True

if email==True:
    print("Email correcto")
else:
    print("Email incorrecto")


print("--------------------------------------------")

