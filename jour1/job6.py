class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = "bobby"

    def vieillir(self):
        self.age += 1
    
    def nommer(self, nouveau_nom):
        self.prenom = nouveau_nom


# Instanciation de l'objet Animal
mon_animal = Animal()

   
# Affichage de l'âge initial
print("Âge initial de l'animal :", mon_animal.age)

# Faire vieillir l'animal
mon_animal.vieillir()


# Affichage de l'âge après avoir vieilli
print("Âge de l'animal après avoir vieilli :", mon_animal.age)


mon_animal.nommer("bobby")


print("Nom de l'animal :", mon_animal.prenom)