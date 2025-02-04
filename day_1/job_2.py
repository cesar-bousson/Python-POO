
#Job2 :

''' À l’aide de la classe Operation créée au-dessus, imprimez en console la
valeur des attributs “nombre1” et “nombre2”.'''

class Operation: 
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
nombres = Operation(12, 3)

print(f" Le nombre 1 est {nombres.nombre1}")
print(f" Le nombre 2 est {nombres.nombre2}")


'''

resultat : 

 Le nombre 1 est 12
 Le nombre 2 est 3 
 
'''
 
 
# -------------------------------------------------------

# essai perso: 

class Voiture: 
    def __init__(self,marque,type):
        self.marque= marque
        self.type = type
        
voiture1 = Voiture("peugeot", "berlin")

print(voiture1.marque)
print(voiture1.type)

        

voiture2 = Voiture("porsche", "citadine")

print(voiture2.marque, voiture2.type)