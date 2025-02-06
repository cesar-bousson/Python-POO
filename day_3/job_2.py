
#job 2
'''
Créer une classe CompteBancaire avec les
attributs privés, numéro de compte, nom,
prénom et solde. Cette classe doit posséder
les méthodes suivantes :

➔ afficher : qui affiche le détail sur le compte.
➔ afficherSolde : cette méthode affiche dans le terminal le solde du
client.
➔ versement : cette méthode prend un paramètre le montant du
versement et ajoute celui-ci au solde du client.
➔ retrait : cette méthode prend un entier en argument (le montant à
retirer) ,enlève ce montant au solde du compte et affiche le nouveau
solde.

Veillez à ce que le compte possède bien le montant disponible sinon un
message d’erreur est affiché.

Créer un compte avec les valeurs de construction de votre choix et faites
appel aux différentes méthodes afin de vérifier que tout fonctionne
correctement.

Ajouter l’attribut découvert à votre classe CompteBancaire, cet attribut aura
pour valeur un booléen. Si le client a le droit à un découvert, la valeur de cet
attribut sera True et des opérations pourront être effectuées même si le solde
est de zéro (méthode retrait).

Ajouter les méthodes suivantes :
➔ agios : cette méthode permet d’appliquer des agios au solde du
compte si celui-ci est négatif.
➔ virement : cette méthode prend en paramètre une référence, un
compte bancaire (celui qui reçoit l’argent) et un montant. Un message
de confirmation ou d'erreur doit être affiché.

Créez une deuxième instance de la classe CompteBancaire. Ce deuxième
compte doit être à découvert (solde négatif). Faire un versement du premier
compte vers celui à découvert afin de le remettre à zéro.

'''

class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde=0, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°: {self.__numero}\nTitulaire: {self.__prenom} {self.__nom}\nSolde: {self.__solde:.2f} €\nDécouvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde:.2f} €")

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant:.2f} € effectué. Nouveau solde: {self.__solde:.2f} €.")
        else:
            print("Le montant du versement doit être positif.")

    def retrait(self, montant):
        if montant > 0:
            if self.__solde - montant < 0 and not self.__decouvert:
                print("Fonds insuffisants et découvert non autorisé.")
            else:
                self.__solde -= montant
                print(f"Retrait de {montant:.2f} € effectué. Nouveau solde: {self.__solde:.2f} €.")
        else:
            print("Le montant du retrait doit être positif.")

    def agios(self):
        if self.__solde < 0:
            taux_agios = 0.05  # 5% d'agios
            montant_agios = abs(self.__solde) * taux_agios
            self.__solde -= montant_agios
            print(f"Agios appliqués: {montant_agios:.2f} €. Nouveau solde: {self.__solde:.2f} €.")
        else:
            print("Aucun agios à appliquer car le solde est positif.")

    def virement(self, compte_destinataire, montant):
        if montant > 0:
            if self.__solde - montant < 0 and not self.__decouvert:
                print("Fonds insuffisants pour effectuer le virement.")
            else:
                self.__solde -= montant
                compte_destinataire.versement(montant)
                print(f"Virement de {montant:.2f} € effectué vers le compte n° {compte_destinataire.__numero}.")
        else:
            print("Le montant du virement doit être positif.")

# Création des comptes
compte1 = CompteBancaire(numero="123456", nom="Dupont", prenom="Jean", solde=500, decouvert=False)
compte2 = CompteBancaire(numero="789012", nom="Martin", prenom="Sophie", solde=-100, decouvert=True)

# Tests des méthodes
print("--- Informations du compte 1 ---")
compte1.afficher()

print("\n--- Informations du compte 2 ---")
compte2.afficher()

print("\n--- Versement sur le compte 1 ---")
compte1.versement(200)

print("\n--- Retrait sur le compte 1 ---")
compte1.retrait(100)

print("\n--- Agios sur le compte 2 ---")
compte2.agios()

print("\n--- Virement du compte 1 vers le compte 2 ---")
compte1.virement(compte2, 300)

print("\n--- État final des comptes ---")
compte1.afficher()
compte2.afficher()
