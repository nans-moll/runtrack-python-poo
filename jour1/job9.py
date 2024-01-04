class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom: {self.nom}, Prix HT: {self.prixHT} €, TVA: {self.TVA}%"
        print(infos)

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Livre", 15, 5)
produit2 = Produit("Ordinateur", 1200, 20)

# Affichage des informations initiales
produit1.afficher()
produit2.afficher()

# Calcul des prix TTC
prix_ttc_produit1 = produit1.calculerPrixTTC()
prix_ttc_produit2 = produit2.calculerPrixTTC()

print(f"Prix TTC du {produit1.obtenirNom()}: {prix_ttc_produit1} €")
print(f"Prix TTC du {produit2.obtenirNom()}: {prix_ttc_produit2} €")

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Cahier")
produit1.modifierPrixHT(3)

produit2.modifierNom("Smartphone")
produit2.modifierPrixHT(800)

# Affichage des informations après modification
produit1.afficher()
produit2.afficher()

