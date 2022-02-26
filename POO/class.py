class Avion():                                    #la clase es el molde de los objetos
    tipo="A320-200 Neo"
    longitud="37.6m"                              #propiedades, atributos  o caracteristicas de la clase
    envergadura="34.1m"
    altura="11.8m"
    motores="CFM International LEAP 1A"
    potencia=input("INGRESE ")

    
    def despegar(self):
        if self.potencia=="maxima potencia":
            return "El avion esta despegando"
        elif self.potencia=="potencia estable":
            print("El avion no puede despegar")
        elif self.potencia=="potencia minima":
            print("El avion no puede despegar")

            
    def volar(self):                  #comportaminetos de una clase
        
        
        pass
    def aterrizar(self):
        pass

Avianca=Avion()  #asi se instancia una clase 

print(Avianca.tipo)  

print(Avianca.potencia,Avianca.despegar())




    