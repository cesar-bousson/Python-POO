
#job 5 : 


''' Créez une classe nommée Point avec les attributs x et y correspondant aux
coordonnées horizontales et verticales du point. Les deux attributs doivent
être initialisés dans le constructeur.

La classe Point doit posséder les méthodes suivantes :
➔ afficherLesPoints qui affiche les coordonnées des points.
➔ afficherX et afficherY qui affiche respectivement x et y.
➔ changerX et changerY qui change la valeur des attributs x et y.  

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def afficherLesPoints(self): #retourne coordonnées (x, y)
        return self.x, self.y
    
    
    def afficherX(self):
        return f"x = {self.x}"
    
    def afficherY(self):
        return f"y = {self.y}"
    
    
    def changerX(self, nouveau_X):
        self.x = nouveau_X
    
    def changerY(self, nouveau_Y):
        self.y = nouveau_Y
    
#instance/objet   
coordonnees1 = Point(200, 300)

print(coordonnees1.afficherLesPoints())

print(coordonnees1.afficherX())
print(coordonnees1.afficherY())

# -------------------------------------------

nouveau_X = int(input("Nouvelle valeur X: "))
nouveau_Y = int(input("Nouvelle valeur Y: "))

coordonnees2 = Point(nouveau_X, nouveau_Y)

print (f"Nouvelles coordonnées : {coordonnees2.afficherLesPoints()}")

''' resultat: 

(200, 300)
x = 200
y = 300
Nouvelle valeur X: 50
Nouvelle valeur Y: 60
Nouvelles coordonnées : (50, 60)

'''

# ------------------------------------------------------------------

