#Création de la classe Character
import random
DEBUG = True


class Character():

    #Définition des attributs
    def __init__(self, name, description, current_room, msgs):
        self.name = name 
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.has_moved = False
    

    def __str__(self):
        return f" {self.name} : {self.description}"
    
    def move_decision(self):
        """
        Détermine si le PNJ doit se déplacer ou non (1 chance sur 2).
        """
        return random.choice([True, False])

    """
    def move(self):
        
        Déplace le PNJ vers une pièce adjacente aléatoire avec une chance sur deux.
        
        if self.move_decision():
            # Vérifie si la salle actuelle a des sorties valides
            valid_exits = [key for key, value in self.current_room.exits.items() if value is not None]
        
            if not valid_exits:
                if DEBUG:
                    print(f"{self.name} ne peut pas bouger car il n'y a aucune sortie valide.")
                return False  # Pas de mouvement possible
        
            # Choisit une direction aléatoire parmi les sorties valides
            direction = random.choice(valid_exits)
            next_room = self.current_room.exits[direction]

            # Déplace le PNJ vers la nouvelle salle
            self.current_room.characters.pop(self.name, None)  # Supprime le PNJ de la salle actuelle
            next_room.characters[self.name] = self  # Ajoute le PNJ à la nouvelle salle
            self.current_room = next_room  # Met à jour la salle actuelle du PNJ

            if DEBUG:
                print(f"{self.name} a été déplacé vers {next_room.name}.")
                self.has_moved = True
            return True  # Le mouvement a eu lieu
        else:
            # Le PNJ ne bouge pas
            if DEBUG:
                print(f"{self.name} n'a pas bougé.")
            return False
            """
    
    def get_msg(self):
        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg