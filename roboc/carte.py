# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""


class Carte:
    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        """Methode constructeur."""
        self.nom = nom

        def creer_labyrinthe_depuis_chaine(chaine):
            """Methode."""
            return chaine

        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        """Methode d'affichage de la carte."""
        return "<Carte {}>".format(self.nom)
