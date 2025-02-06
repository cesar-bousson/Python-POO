

#Job 6
'''
Créer une classe Commande avec les attributs privés, numéro de
commande, liste de plats commandés et statut de la commande (en cours,
terminée ou annulée).

Ajouter des méthodes permettant d’ajouter un plat à la commande, annuler
une commande, calculer le total d’une commande privée et afficher une
commande avec son total à payer, ainsi qu’une méthode permettant de
calculer la TVA.

Utiliser l’encapsulation et l’abstraction pour créer cette classe de manière que
les attributs ne puissent pas être modifiés de l’extérieur. La liste des plats
commandés doit être représentée sous forme de dictionnaire avec les noms
des plats, le prix ainsi que le statut de la commande.

Sur votre script doit apparaître l’ensemble des méthodes appelées tout au
long de cet exercice.

'''

# Unfinished:

class Commande:
    def __init__(self, num_commande, liste_plats_commande, statut_commande, prix_commande):
        self.__num_commande = num_commande
        self.__liste_plats_commande = liste_plats_commande
        self.__statut_commande = statut_commande
        
        self.__prix_commande = prix_commande
        
        self.__commande = {"salade" : 12,
                           "saumon" : 12,
                           "fondant" : 12,
                           "menu1" : 12,
                           "menu2" : 12,
                           "menu3" : 12 }
        
        
        
    def set_ajouter_plat(self, plat): 
        self.__liste_plats_commande.append(plat)# a instancier
    
    def get_listing_commande(self):
        return f"\nCommande actuelle:\n Numéro de Table: {self.__num_commande} , Liste des plats: {self.__liste_plats_commande}\nStatut:  {self.__statut_commande} \n"

    def annuler_commande(self, statut_annuler):
        self.demande = input("Annuler la commande ? Tapez X pour oui, O pour non :")
        self.statut_annuler = statut_annuler
        
        if self.demande not in ["x", "o", "X", "O"]:
            raise ValueError("Tapez X ou O. Recommencez")
        else:
            self.__statut_commande = statut_annuler
            return self.__statut_commande
    
    ''''''''''''
    def prix_commande():
        pass
            
table12 = Commande(12, ["salade", "saumon papillote", "fondant au chocolat" ], "en cours")
print(table12.get_listing_commande())

''''''''
plat = input("\nAjouter un plat à la commande : ")
table12.set_ajouter_plat(plat)

print(table12.get_listing_commande())

''''''''

statut_annuler = (table12.annuler_commande("Annulé"))
print(table12.get_listing_commande())

''''''''

liste_plats_commande = [""]



# ------------------------------------- CORRECTION -------------------------------------------------

class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}  # Dictionnaire {nom_du_plat: prix}
        self.__statut = "en cours"  # en cours, terminée, annulée

    # Getter pour le statut
    def get_statut(self):
        return self.__statut

    # Ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix):
        if self.__statut != "en cours":
            print("Impossible d'ajouter un plat : la commande n'est pas en cours.")
            return
        self.__plats[nom_plat] = prix
        print(f"Plat '{nom_plat}' ajouté avec succès.")

    # Annuler la commande
    def annuler_commande(self):
        if self.__statut != "en cours":
            print("La commande ne peut pas être annulée.")
            return
        self.__statut = "annulée"
        print("Commande annulée avec succès.")

    # Terminer la commande
    def terminer_commande(self):
        if self.__statut != "en cours":
            print("La commande ne peut pas être terminée.")
            return
        self.__statut = "terminée"
        print("Commande terminée avec succès.")

    # Calculer le total des plats
    def __calculer_total(self):
        return sum(self.__plats.values())

    # Calculer la TVA (20% du total)
    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.2
        return round(tva, 2)

    # Afficher la commande avec le total
    def afficher_commande(self):
        print(f"Commande n° {self.__numero_commande}")
        print(f"Statut : {self.__statut}")
        print("Plats commandés :")
        for nom_plat, prix in self.__plats.items():
            print(f" - {nom_plat}: {prix:.2f} €")
        total = self.__calculer_total()
        tva = self.calculer_tva()
        print(f"Total (hors TVA) : {total:.2f} €")
        print(f"TVA (20%) : {tva:.2f} €")
        print(f"Total à payer : {total + tva:.2f} €")

# Exemple d'utilisation
commande = Commande(123)
commande.ajouter_plat("Pizza Margherita", 12.5)
commande.ajouter_plat("Salade Caesar", 9.8)
commande.afficher_commande()
commande.terminer_commande()
commande.afficher_commande()
commande.ajouter_plat("Tiramisu", 6.0)  # Ne sera pas ajouté car la commande est terminée
