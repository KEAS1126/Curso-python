# 1.	Write the python code that corresponds to the following pseudocode – 
# Competencia que incluye: inglés.
#  Pseudocode: If then Else
# If age > 17
#   Display a message indicating you can vote.
# Else
#   Display a message indicating you can't vote.
# Endif
# Pseudocode: While
# count assigned zero
# While count < 5
#   Display "I love computers!"
#   Increment count
# Endwhile
edad=int(input("ingrese su edad "))
if edad >17:
    print("puedes votar")
else:
    print("no puede votar")
    
contador=0
while contador<5:
    print("yo amo los computadores")
    contador+=1
    