
# Job 5

'''
Créez un jeu de combat en utilisant la POO.

À tour de rôle, votre personnage et l’ennemi attaquent. Le but étant de
vaincre l’ennemi (vie à zéro).

Votre programme doit contenir au minimum deux classes, Personnage et
Jeu.

Commencer par créer une classe nommée Personnage prenant des
paramètres de construction : nom (string) et vie(int).
Créez au minimum une méthode attaquer qui enlève des points à son
adversaire.

Ensuite créer la classe Jeu ne prenant pas de paramètre. Créer une méthode
choisirNiveau qui permet de demander au joueur le niveau de difficulté.
Celui-ci sera stocké dans l’attribut niveau.

En fonction du niveau choisi, le nombre de points de vie du joueur ainsi que
de l'ennemi seront différents.
Créer lancerJeu, méthode qui utilise l’attribut niveau. Cette méthode aura
pour but d’instancier deux objets Personnage, un qui représente le joueur et
l’autre l'ennemi avec un nombre de points défini en fonction du niveau.

Implémenter le déroulement d’une partie en demandant au joueur le niveau
de difficulté et pensez à ajouter une méthode qui vérifie la santé de vos
personnages ainsi qu’une méthode permettant de vérifier qui a gagné.

Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au
long des exercices.

'''

import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts. {adversaire.nom} a maintenant {adversaire.vie} points de vie.")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisir_niveau(self):
        print("Choisissez un niveau de difficulté :")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        while True:
            try:
                choix = int(input("Votre choix (1, 2 ou 3) : "))
                if choix in [1, 2, 3]:
                    self.niveau = choix
                    break
                else:
                    print("Veuillez entrer un chiffre entre 1 et 3.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un chiffre.")

    def lancer_jeu(self):
        if self.niveau == 1:
            vie_joueur, vie_ennemi = 100, 50
        elif self.niveau == 2:
            vie_joueur, vie_ennemi = 75, 75
        else:
            vie_joueur, vie_ennemi = 50, 100

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print(f"Le combat commence ! {joueur.nom} : {joueur.vie} PV, {ennemi.nom} : {ennemi.vie} PV.")

        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)

        self.verifier_victoire(joueur, ennemi)

    def verifier_victoire(self, joueur, ennemi):
        if joueur.est_vivant():
            print(f"Bravo ! {joueur.nom} a remporté le combat !")
        else:
            print(f"Dommage... {ennemi.nom} a gagné le combat.")

# Lancement du jeu
if __name__ == "__main__":
    jeu = Jeu()
    jeu.choisir_niveau()
    jeu.lancer_jeu()
