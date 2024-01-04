class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self._disponible = disponible

    def vérification(self):
        return self._disponible

    def emprunter(self):
        if self.vérification():
            print("Le livre est disponible. Emprunt en cours...")
            self._disponible = False
            print("Emprunt réussi.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.vérification():
            print("Le livre a été emprunté. Rendre en cours...")
            self._disponible = True
            print("Rendu réussi.")
        else:
            print("Le livre n'a pas été emprunté.")


livre1 = Livre("Harry Potter", "J.K. Rowling")
livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", disponible=False)


print(f"Le livre '{livre1.titre}' est disponible : {livre1.vérification()}")
print(f"Le livre '{livre2.titre}' est disponible : {livre2.vérification()}")


livre1.emprunter()
livre2.emprunter()


livre1.rendre()
livre2.rendre()


print(f"Le livre '{livre1.titre}' est disponible : {livre1.vérification()}")
print(f"Le livre '{livre2.titre}' est disponible : {livre2.vérification()}")
