
#Job 7

'''
Développer votre version du célèbre jeu Blackjack. Le but est de faire le plus
de points sans dépasser 21. Chaque carte représente une valeur :
- de 2 à 10 : ces cartes ont pour valeur sa valeur nominale
- une figure a pour valeur 10 points
- un as 1 ou 11 points au choix

Le jeu commence avec les joueurs qui reçoivent chacun 2 cartes. Ensuite, le
joueur peut choisir de "prendre" (recevoir) une ou plusieurs cartes
supplémentaires pour tenter d'améliorer sa main, ou de "passer" et laisser le
tour au croupier. Le croupier prend des cartes jusqu'à ce qu'il ait au moins 17
points, puis s'arrête. Si la main du joueur dépasse 21, il perd immédiatement.
Si le total de la main du joueur est supérieur à celui du croupier, le joueur
gagne. Sinon, c'est le croupier qui gagne.

Créer au minimum deux classes Carte et Jeu.

La classe Carte aura au minimum un attribut valeur et couleur. La classe Jeu
quant à elle devra gérer l’ensemble des cartes. Les cartes du jeu seront
stockées dans un attribut paquet représenté par une liste et contenant 52
cartes.

Créer toutes les méthodes nécessaires pour jouer une partie.

Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au
long des exercices.

'''

import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def get_valeur(self):
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10
        elif self.valeur == "As":
            return 11  # L'As sera ajusté à 1 si nécessaire dans le calcul du score
        else:
            return int(self.valeur)


class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        random.shuffle(self.paquet)

    def creer_paquet(self):
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        valeurs = [str(i) for i in range(2, 11)] + ["Valet", "Dame", "Roi", "As"]
        return [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]

    def tirer_carte(self):
        return self.paquet.pop()


class Blackjack:
    def __init__(self):
        self.jeu = Jeu()

    def calculer_score(self, main):
        total = 0
        nb_as = 0

        for carte in main:
            valeur = carte.get_valeur()
            total += valeur
            if carte.valeur == "As":
                nb_as += 1

        # Ajuster la valeur des As si le total dépasse 21
        while total > 21 and nb_as > 0:
            total -= 10
            nb_as -= 1

        return total

    def afficher_main(self, joueur, main):
        print(f"\n{joueur} a les cartes :")
        for carte in main:
            print(f"  - {carte}")
        print(f"Score : {self.calculer_score(main)}")

    def jouer(self):
        print("Bienvenue au Blackjack !")

        # Initialisation
        main_joueur = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]
        main_croupier = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]

        # Tour du joueur
        while True:
            self.afficher_main("Le joueur", main_joueur)
            if self.calculer_score(main_joueur) > 21:
                print("\nLe joueur dépasse 21 ! Le croupier gagne.")
                return

            choix = input("\nVoulez-vous 'prendre' une carte ou 'passer' ? (prendre/passer) : ").lower()
            if choix == "prendre":
                main_joueur.append(self.jeu.tirer_carte())
            elif choix == "passer":
                break
            else:
                print("Choix invalide, essayez à nouveau.")

        # Tour du croupier
        while self.calculer_score(main_croupier) < 17:
            main_croupier.append(self.jeu.tirer_carte())

        # Afficher les résultats
        self.afficher_main("Le joueur", main_joueur)
        self.afficher_main("Le croupier", main_croupier)

        score_joueur = self.calculer_score(main_joueur)
        score_croupier = self.calculer_score(main_croupier)

        if score_croupier > 21 or score_joueur > score_croupier:
            print("\nLe joueur gagne !")
        elif score_joueur < score_croupier:
            print("\nLe croupier gagne !")
        else:
            print("\nÉgalité !")


# Lancer le jeu
blackjack = Blackjack()
blackjack.jouer()
