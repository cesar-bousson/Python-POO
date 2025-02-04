

#job 3

'''  Modifiez votre classe Operation afin d’y ajouter la méthode addition(). Cette
méthode additionne “nombre1” et “nombre2” et affiche en console le résultat.'''

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
        return self.nombre1 + self.nombre2 
        
calcul = Operation(12, 3)

print(calcul.addition())

#resultat : 15 

# -------------------------------------------------




# essai perso : 

class Operation: 
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def multiplication(self):
        return self.nombre1 * self.nombre2

calcul = Operation(15, 40)

print(calcul.multiplication())