"""
Module qui définit la classe Item pour représenter des objets dans le jeu.
Cette classe permet de gérer les attributs et les informations des objets
comme leur nom, description, poids, et état.
"""

class Item:
    """
    Classe représentant un objet dans le jeu.

    Attributes:
        name (str): Le nom de l'objet.
        description (str): La description de l'objet.
        weight (float): Le poids de l'objet.
        state (str): L'état actuel de l'objet.
    """
    def __init__(self, name, description, weight, state):
        """
        Initialise un nouvel objet Item.

        :param name: str, le nom de l'objet
        :param description: str, la description de l'objet
        :param weight: float, le poids de l'objet
        :param state: str, l'état de l'objet
        """
        self.name = name
        self.description = description
        self.weight = weight
        self.state = state

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.
        """
        return f"Item(name='{self.name}', description='{self.description}', weight={self.weight})"
    def set_state(self, new_state):
        """
        Permet de changer l'état de l'objet (par exemple, "neuf", "usé").
        """
        self.state = new_state
