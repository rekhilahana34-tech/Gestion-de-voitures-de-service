class Employe:
    def __init__(self,numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformation(self):
        print("Numero permis :", self.numeroPermis)
        print("Nom :", self.nom)
        print("Prenom :", self.prenom)

        if self.voitureService is not None:
            print("Voiture :", self.voitureService.matricule)
        else:
            print("pas de voiture de service")

    def affecterVoiture(self, voiture):
        if self.voitureService is None and voiture.chauffeur is None:
            self.voitureService = voiture
            voiture.chauffeur = self
            print("voiture affectée")
        else:
            print("Impossible de faire voiture")

    def retirerVoiture(self):
        if self.voitureService is not None:
            self.voitureService.chauffeur = None
            self.voitureService = None

        print("voiture retirer")
class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformation(self):
        print("matricule:", self.matricule)
        print("annee:", self.annee)
        print("marque:", self.marque)
        print("kilometrage:", self.kilometrage)
        if self.chauffeur is not None:
            print("chauffeur:", self.chauffeur.nom)
        else:
            print("pas de chauffeur")
emp1 = Employe("p123","Dupont", "jean")
amp2 = Employe("p456","Martin", "Hana")

v1 = Voiture("AA111", 2022, "Toyota",15000)
v2 = Voiture("BB222", 2021, "Honda",15000)