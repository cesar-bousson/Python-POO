

#job 4: 

''' Créez une classe Personne avec les attributs nom et prenom. Ajoutez une
méthode SePresenter qui retourne le nom et le prénom de la personne.
Ajoutez aussi un constructeur prenant en paramètres de quoi donner des
valeurs initiales aux attributs nom et prenom. Instanciez plusieurs personnes
avec les valeurs de construction de votre choix et faites appel à la méthode
SePresenter afin de vérifier que tout fonctionne correctement.'''

class Personne:
    def __init__(self, nom, prenom):
        self.nom=nom
        self.prenom=prenom
    
    def SePresenter(self):
        return f"je suis {self.nom} {self.prenom}"

personne1 = Personne("Cesar", "Trujillo")
personne2 = Personne("Cesar" , "Bousson")

print(personne1.SePresenter())
print(personne2.SePresenter())

'''
resultat: 
je suis Cesar Trujillo
je suis Cesar Bousson 

'''

# ---------------------------------------------------------------------