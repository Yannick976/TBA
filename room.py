"""
Module room.py
Description : Ce module gère les objets Room pour le projet.
"""

class Room:
    """
    Représente une pièce avec des caractéristiques spécifiques.
    """
    def __init__(self, name, description):
        """
        Initialise une pièce avec un nom et une description.
        
        Args:
            name (str): Le nom de la pièce.
            description (str): La description de la pièce.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = {}

    def get_exit(self, direction):
        """
        Retourne la pièce correspondante à une direction donnée si elle existe.
        
        Args:
            direction (str): La direction dans laquelle chercher une sortie.
        
        Returns:
            Room: La pièce associée à la direction, ou None si elle n'existe pas.
        """
        if direction in self.exits:
            return self.exits[direction]
        return None

    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties disponibles de la pièce.
        
        Returns:
            str: Une chaîne listant les directions des sorties.
        """
        exit_string = "Sorties: "
        for direction, room in self.exits.items():
            if room is not None:
                exit_string += direction + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """
        Retourne une description complète de la pièce, y compris les sorties disponibles.
        
        Returns:
            str: Une chaîne décrivant la pièce.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventoryroom(self):
        """
        Retourne l'inventaire de la salle, y compris les objets et les personnages présents.
        
        Returns:
            str: Une description des objets et personnages présents dans la pièce.
        """
        if not self.inventory and not self.characters:
            return "\nIl n'y a rien ici."

        content_return = "\nOn voit :"
        for obj in self.inventory:
            content_return += f"\n {obj.name} : {obj.description} ({obj.weight}kg)"
        for pnj in self.characters.values():
            content_return += f"\n {pnj.name} : {pnj.description}"
        return content_return

    def get_character(self, name):
        """
        Retourne un personnage présent dans la pièce, si trouvé.
        
        Args:
            name (str): Le nom du personnage à chercher.
        
        Returns:
            Character: Le personnage correspondant, ou None s'il n'existe pas.
        """
        name_lower = name.lower()
        for key, character in self.characters.items():
            if key == name_lower:
                return character
        return None
