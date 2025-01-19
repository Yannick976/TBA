"""
Ce fichier contient la définition de la classe Character, représentant un personnage dans le jeu.
"""

import random
DEBUG = True

class Character:
    """
    Représente un personnage (PNJ) dans le jeu. 
    Le personnage peut se déplacer dans différentes pièces et interagir avec d'autres entités.
    """

    def __init__(self, name, description, current_room, msgs):
        """
        Initialise un personnage avec :
        un nom, une description, une pièce actuelle et une liste de messages.

        :param name: str, le nom du personnage.
        :param description: str, une description du personnage.
        :param current_room: Room, la pièce dans laquelle se trouve le personnage.
        :param msgs: list, une liste de messages que le personnage peut envoyer.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.has_moved = False

    def __str__(self):
        return f"{self.name} : {self.description}"

    def move_decision(self):
        """
        Détermine si le personnage doit se déplacer ou non. 
        La décision est aléatoire (1 chance sur 2).
        
        :return: bool, True si le personnage se déplace, False sinon.
        """
        return random.choice([True, False])

    def get_msg(self):
        """
        Retourne le prochain message du personnage en le déplaçant dans la liste des messages.
        :return: str, le message du personnage.
        """
        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg
