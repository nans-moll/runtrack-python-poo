class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    # Assesseurs (getters)
    def getMarque(self):
        return self._marque

    def getModele(self):
        return self._modele

    def getAnnee(self):
        return self._annee

    def getKilometrage(self):
        return self._kilometrage

    def getEnMarche(self):
        return self._en_marche

    def getReservoir(self):
        return self._reservoir

    # Mutateurs (setters)
    def setMarque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def setModele(self, nouveau_modele):
        self._modele = nouveau_modele

    def setAnnee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def setKilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def setEnMarche(self, nouvel_etat):
        self._en_marche = nouvel_etat

    def setReservoir(self, nouveau_reservoir):
        self._reservoir = nouveau_reservoir

    # Méthode privée
    def _verifier_plein(self):
        return self._reservoir > 5

    # Méthodes publiques
    def demarrer(self):
        if self._verifier_plein():
            print("La voiture démarre.")
            self._en_marche = True
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    def arreter(self):
        print("La voiture s'arrête.")
        self._en_marche = False

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Toyota", "Camry", 2020, 25000)

# Affichage des informations initiales
print("Marque :", ma_voiture.getMarque())
print("Modèle :", ma_voiture.getModele())
print("Année :", ma_voiture.getAnnee())
print("Kilométrage :", ma_voiture.getKilometrage())
print("En marche :", ma_voiture.getEnMarche())
print("Réservoir :", ma_voiture.getReservoir())

# Modification et affichage des informations après démarrage
ma_voiture.setReservoir(10)
ma_voiture.demarrer()
print("En marche après démarrage :", ma_voiture.getEnMarche())
print("Réservoir après démarrage :", ma_voiture.getReservoir())

# Arrêt de la voiture
ma_voiture.arreter()
print("En marche après arrêt :", ma_voiture.getEnMarche())
