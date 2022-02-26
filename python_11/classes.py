class Persona:
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def descripcion(self):
        print("Nombre:", self.nombre, "- Edad:", self.edad, "- Peso: ", self.peso)

persona1 = Persona("Kevin",21,59)
# print(persona1.descripcion())
# persona1.setNombre("Estiven")
# print(persona1.getNombre())
persona1.setNombre("Estiven")
persona1.setEdad(25)
persona1.setPeso(70)
# print(persona1.descripcion())
print(persona1.getEdad())



# letras = ["a", "b", "c"]
# print(letras)
# letras.append("D")
# print(letras)

