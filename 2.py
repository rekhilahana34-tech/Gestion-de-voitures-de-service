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