"""
Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.

#The error message is stored in the MSG0 
# and MSG1 variables and formatted with the command_word variable, the first word in the command.
"""
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    Cette classe contient les actions que le joueur peut exécuter dans le jeu.
    Chaque action correspond à une commande et a des paramètres.
    """

    def __init__(self):
        """
        Initialise l'attribut finished
        """
        self.finished = False  # Initialisation de l'attribut 'finished'

    def go(self, game, list_of_words, number_of_parameters):
        """
        Permet au joueur de se déplacer dans la direction spécifiée par le paramètre.
        La direction doit être un cardinal (N, E, S, O).

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus.

        Returns:
            bool: True si la commande a été exécutée avec succès, sinon False.
        Examples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False
        """
        player = game.player
        l = len(list_of_words)
        # Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        direction = list_of_words[1].upper()
        if direction not in player.current_room.exits:
            print(f"\nLa direction '{direction}' n'est pas valide depuis ici.")
            return False
        player.move(direction)
        print("Vous avez déjà été:")
        print(player.get_history())  # Affichage de l'historique après chaque déplacement
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise.
        Examples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def quit(self, game, list_of_words, number_of_parameters):
        """
        Quitte le jeu.
        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus.
        Returns:
            bool: True si la commande a été exécutée avec succès, sinon False.
        Examples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True
    
    def help(self, game, list_of_words, number_of_parameters):
        """
        Affiche la liste des commandes disponibles.
        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus.
        Returns:
            bool: True si la commande a été exécutée avec succès, sinon False.
        Examples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    def back(self, game, list_of_words, number_of_parameters):
        """
        Permet de revenir à la dernière pièce visitée.
        """
        player = game.player
        if len(player.history) > 0:
            last_room_description = player.history.pop()
            for room in game.rooms:
                if room.description == last_room_description:
                    player.current_room = room
                    print(player.current_room.get_long_description())
                    print("Vous avez déjà visité les pièces suivantes:")
                    print(player.get_history())  # Affichage de l'historique après retour en arrière
                    return True
        else:
            print("Vous ne pouvez pas revenir en arrière, aucun historique de déplacements.")
            return False

    @staticmethod
    def history(game):
        """
        Affiche l'historique des pièces visitées.
        """
        player = game.player
        print("Vous avez déjà visité les pièces suivantes:")
        print(player.get_history())  # Affichage de l'historique
        return True
    def inventory(self, game, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire du joueur si la commande est correcte.
        """
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        game.player.get_inventory()
        return True
    def inventoryroom(self, game, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire de la pièce si la commande est correcte.
        """
        rooms = game.rooms
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        game.player.current_room.get_inventoryroom()
        return True
    def look(self, game, list_of_words, number_of_parameters):
        """
        Affiche ce qu'il y a autour du joueur.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print(game.player.current_room.get_inventoryroom())
        return True
    def take(self, game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        name_item = list_of_words[1]
        total_weight = 0

        for poids in player.inventory.values():
            total_weight += poids.weight

        for item in player.current_room.inventory:
            if name_item == item.name:
                total_weight += item.weight
                if total_weight > player.max_weight:
                    print("\nVous ne pouvez pas porter plus de 30kg sur vous.\n")
                    return True
                player.inventory[item.name] = item
                player.current_room.inventory.remove(item)
                print(f"\nVous avez pris l'objet : '{item.name}'.\n")
                return True
        if name_item in player.inventory:
            print(f"\nL'objet '{name_item}' se trouve déjà dans votre inventaire.\n")
        else:
            print(f"\nL'objet '{name_item}' n'est pas présent dans ce lieu.\n")
        return True
    def drop(self, game, list_of_words, number_of_parameters):
        """
        Dépose un objet de l'inventaire du joueur dans la pièce.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        itemdrop = list_of_words[1]  # Nom de l'objet à déposer
        player = game.player
        if itemdrop in player.inventory:
            item = player.inventory[itemdrop]
            player.current_room.inventory.add(item)
            del player.inventory[itemdrop]  # Suppression de l'objet de l'inventaire du joueur
            print(f"Vous avez déposé {item.description}.")
            return True
        else:
            print(f"L'objet '{itemdrop}' n'est pas dans votre inventaire. Veuillez réessayer.")
            return False

    def check(game, list_of_words, number_of_parameters):
        """
        Vérifie si un objet est dans l'inventaire du joueur.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print(f"\n{game.player.get_inventory()}")

    def use(game, list_of_words, number_of_parameters):
        """
        Permet au joueur d'utiliser un objet de son inventaire.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1]
        if item_name == 'clé' :
            print("Vous pouvez rentrer dans la maison abandonnée.")
        elif item_name == 'clé_voiture' :
            print("Félicitation vous pouvez vous échapper vous avez récupérer les clefs et des preuves.")
        elif item_name == 'journal':
            print("Journal de Becker : J'ai enfin découvert le secret de ce village...")
            print("\n Ils assassinent les visiteurs pour vendre leurs organes afin de subvenir aux besoins financiers du village !")
        elif item_name == 'oreiller':
            print("Vous avez dormi. Vous avez passé une nuit agitée à cause des bruits venant le l'éxterieur.")
        elif item_name =='verre' :
            print("Vous commencez à vous sentir mal. Le verre que vous venez de boire était empoisonné.  Vous êtes mort. ")

        else:
            print("L'objet n'est pas dans votre inventaire.")
            return False


    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler à un personnage dans la pièce actuelle.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        if len(game.player.current_room.characters) >= 1:
            character_name = list_of_words[1]
            character = game.player.current_room.get_character(character_name)
            if character is None:
                print(f"Le personnage '{character_name}' n'existe pas dans cette pièce.")
                return False
            else:
                print(character.get_msg())  # Affiche le message du PNJ
            return True
        else:
            print("Il n'y a aucun PNJ dans cette pièce")
        return True

        