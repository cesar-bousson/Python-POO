
# job 1 : 
''' Créez une classe Operation avec un constructeur (méthode qui sera appelée
lors de l’instance de la classe). Ajoutez les attributs “nombre1” et “nombre2”
initialisés avec des valeurs par défaut. Instanciez votre première classe et
imprimez l’objet en console. '''

class Operation: 
    def __init__(self, nombre1, nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2
        
    def calcul(self):
        return (f"Calcul: {self.nombre1} + {self.nombre2}.")
        

calcul1 = Operation(2, 5)
calcul2 = Operation(4, 4)

print(calcul1) # résultat : <__main__.Operation object at 0x000002517007AB40>

# --------------------------------------------------------------------------------------
