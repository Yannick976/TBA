"""
Module player.py
Description : Ce module gère les objets Player pour le projet.
"""

class Player():
    """
    Représente un joueur avec un nom, un inventaire et un historique de déplacements.
    """
    def __init__(self, name):
        """
        Initialise un joueur avec un nom, une salle courante et un inventaire vide.

        Args:
            name (str): Le nom du joueur.
        """
        self.name = name
        self.current_room = None
        self.history = []  # Historique des pièces visitées
        self.inventory = {}
        self.max_weight = 30
    def move(self, direction):
        """
        Déplace le joueur dans une autre pièce selon la direction donnée.

        Args:
            direction (str): La direction vers laquelle le joueur souhaite se déplacer.

        Returns:
            bool: True si le déplacement a réussi, False sinon.
        """
        # Vérifiez si la direction est valide dans les sorties de la pièce actuelle.
        next_room = self.current_room.exits.get(direction)
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune issue dans cette direction !\n")
            return False
        # Ajoutez la description de la pièce actuelle à l'historique si elle n'y est pas encore.
        if self.current_room.description not in self.history:
            self.history.append(self.current_room.description)
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        """
        Retourne l'historique des pièces visitées sous forme de chaîne.

        Returns:
            str: L'historique des pièces visitées.
        """
        if self.history:
            return "\n".join([f"- {i}" for i in self.history])
        return "Aucun historique de visites."
    def get_inventory(self):
        """
        Affiche et retourne le contenu de l'inventaire du joueur.

        Returns:
            str: Le contenu de l'inventaire du joueur.
        """
        if not self.inventory:
            return "\nVotre inventaire est vide."
        inventory_contents = "\nVous disposez des items suivants :"
        for item_name, item_obj in self.inventory.items():
            inventory_contents += (
                f"\n  - {item_name} : {item_obj.description} "
                f"({item_obj.weight}kg)"
            )
        return inventory_contents
