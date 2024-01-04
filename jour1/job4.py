class Personne:
    def __init__(self, nom="", prenom=""):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes avec des valeurs de construction
personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Alice")
personne3 = Personne("Dupont", "Pierre")

# Appel à la méthode SePresenter pour chaque personne
print(personne1.sePresenter())
print(personne2.sePresenter())
print(personne3.sePresenter())
