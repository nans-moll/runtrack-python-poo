class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage
personnage = Personnage(0, 0)

print("Position initiale du personnage :", personnage.position())

personnage.droite()
print("Position du personnage après avoir bougé à droite :", personnage.position())

personnage.bas()
print("Position du personnage après avoir bougé en bas :", personnage.position())

personnage.gauche()
print("Position du personnage après avoir bougé à gauche :", personnage.position())

personnage.haut()

print("Position du personnage après avoir bougé en haut  :", personnage.position())