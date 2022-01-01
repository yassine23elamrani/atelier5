# class Etudiant
class Etudiant():
    # Constructeur avec parametres
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.Nom = nom
        self.Prenom = prenom
        self.Age = age
        self.Cne = cne
        self.Moyenne = moyenne

    def display(self):
        return "["+self.Nom+", "+self.Prenom + ", " + str(self.Age) + ", "+self.Cne+", " + str(self.Moyenne) + "]"


myEtudiant = []
print("\n la liste principale : ____________________________________")
e1 = Etudiant("hind", "aabou", 21, "P145082842", 18)
e2 = Etudiant("houda", "aabou", 19, "P135015515", 16)
e3 = Etudiant("afnan", "aabou", 7, "P145082842", 8)
e4 = Etudiant("douae", "aabou", 10, "P145082842", 2)
myEtudiant.append(e1)
myEtudiant.append(e2)
myEtudiant.append(e3)
myEtudiant.append(e4)
for i in myEtudiant:
    print(i.display())
print("\n la liste trie selon l'age : ____________________________________")
List_Age = sorted(myEtudiant, key=lambda Etudiant: Etudiant.Age)
for a in List_Age:
    print(a.display())
print("\n la liste trie selon la moyenne : ____________________________________")
List_Moyenne = sorted(myEtudiant, key=lambda Etudiant: Etudiant.Moyenne)
for m in List_Moyenne:
    print(m.display())
