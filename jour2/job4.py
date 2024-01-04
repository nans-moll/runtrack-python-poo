class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._nombre_credits = 0
        self._level = self._studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self._nombre_credits += credits
            print(f"{credits} crédits ajoutés avec succès.")
            self._level = self._studentEval()
        else:
            print("Erreur : Veuillez fournir un nombre de crédits supérieur à zéro.")

    def _studentEval(self):
        if self._nombre_credits >= 90:
            return "Excellent"
        elif self._nombre_credits >= 80:
            return "Très bien"
        elif self._nombre_credits >= 70:
            return "Bien"
        elif self._nombre_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Informations de l'étudiant {self._nom} {self._prenom} (ID: {self._numero_etudiant}):")
        print(f"Nombre de crédits : {self._nombre_credits}")
        print(f"Niveau : {self._level}")


john_doe = Student("Doe", "John", 145)


john_doe.add_credits(95)
john_doe.add_credits(75)
john_doe.add_credits(60)


john_doe.studentInfo()

