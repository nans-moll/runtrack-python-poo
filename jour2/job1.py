class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def getLongueur(self):
        return self._longueur

    def getLargeur(self):
        return self._largeur

  
    def setLongueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur


rectangle = Rectangle(12, 8)


print("Longueur initiale du rectangle :", rectangle.getLongueur())
print("Largeur initiale du rectangle :", rectangle.getLargeur())


rectangle.setLongueur(15)
rectangle.setLargeur(8)


print("Longueur après modification :", rectangle.getLongueur())
print("Largeur après modification :", rectangle.getLargeur())

