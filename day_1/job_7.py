
#Job 7
'''
Créez une classe Personnage représentant un personnage de jeu. Le plateau
de jeu est représenté par une matrice. Le joueur est défini par ses attributs x
et y, représentant les index du tableau.
Créez le constructeur de cette classe en initialisant la position (x et y).
Créez les méthodes : gauche, droite, bas et haut permettant respectivement
de faire avancer à gauche et à droite, en haut ou en bas.

Implémentez une méthode “position” renvoyant les coordonnées sous forme
d’un tuple.

'''

class Personnage: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.matrice = [
            
            ["","","","",""],  # [0,0 | 0,1 | 0,2 | 0,3 | 0,4]
            ["","","","",""],  # [1.0 | 1,1 | 1,2 | 1,3 | 1,4]
            ["","","","",""],  # [2,0 | 2,1 | 2,2 | 2,3 | 2,4]
            ["","","","",""],  # [3,0 | 3,1 | 3,2 | 3,3 | 3,4]
            ["","","","",""],  # [4,0 | 4,1 | 4,2 | 4,3 | 4,4]
            
            ]

    # methodes :
    def gauche(self):
        self.y -= 1
        return f"\n Nouvelle position vers la gauche : {self.x, self.y}"
    
    def droite(self): 
        self.y += 1
        return f"\n Nouvelle position vers la droite : {self.x, self.y}"
    
    def bas(self): 
        self.x += 1
        return f"\n Nouvelle position vers le bas : {self.x, self.y}"
    
    def haut(self): 
        self.x -= 1
        return f"\n Nouvelle position vers le haut : {self.x, self.y}"
        
    def position(self): 
        return f"\n Position joueur actuelle : {(self.x, self.y)} \n " # tuple

# instances/objets :
position_joueur = Personnage(2,2)

#resultats de positions et mouvements possible:
print(position_joueur.position())

print(position_joueur.gauche())
print(position_joueur.droite())
print(position_joueur.haut())
print(position_joueur.bas())




#  ----------------------------------------------------------------
# nouvel essai de pratique solo: 

class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
        self.matrice = [
            
            [(0,0),(0,1),(0,2),(0.3),(0.4)], #comme ceci
            ["","","","",""], # ou comme cela
            ["","","","",""],
            ["","","","",""],
        ]
        
    def gauche(self):
        self.y -= 1
        return self.x, self.y
    
    def droite(self):
        self.y += 1
        return self.x, self.y
    
    def bas(self):
        self.x += 1
        return self.x, self.y
    
    def haut(self):
        self.x -= 1
        return self.x, self.y
    
    def position(self):
        return ((self.x, self.y))
    
position_joueur = Personnage(0,2)

print(position_joueur.gauche())

print(position_joueur.bas())

print(position_joueur.position())