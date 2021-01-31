"""Application controller."""

from application.controller.mainmenu import MainController
from application.controller.categorymenu import CatMenuController


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""

    def show(self):
        """Show the application controller."""
        main_controller = MainController()
        category_menu = CatMenuController()

        main_controller.show()
        choice = int(input())

        if choice == 1:
            category_menu.show()
        if choice == 2:
            print("2 - indisponible.")

        # afficher le menu principal
        # l'utilisateur fait un choix 1 ou 2
        # le controller menu principal retourne le choix de l'utilisateur
        # pour le choix 1 afficher menu catégories (controller category)
        # l'utilisateur choisi une catégorie
        # SQL sélectionne produits dans catégorie choisie
        # afficher menu prduits (résultats requête SQL)
