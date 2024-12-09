# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        history = Command("history", " : afficher l'historique des déplacements", Actions.history, 0)
        self.commands["history"] = history
        
        # Setup des pièces 
        grande_place = Room("La grande place", "sur une place centrale avec une grande fontaine au milieu.")
        maison_chef = Room("Maison du chef", "dans la maison impressionnante du chef du village.")
        maison_joueur = Room("Maison du joueur", "dans votre propre maison chaleureuse.")
        exterieur_maison = Room("Extérieur de la maison", "devant l'entrée de votre maison.")
        cave = Room("Cave", "dans une cave sombre et mystérieuse.")
        maison_abandonnee = Room("Maison abandonnée", "dans une maison décrépite, où règne une ambiance inquiétante.")
        bibliotheque = Room("Bibliothèque", "entouré de rangées de livres anciens et poussiéreux.")
        ferme = Room("Ferme", "dans un champ avec des cultures et des outils agricoles.")

        grande_place.exits = {"N": maison_chef, "E": exterieur_maison, "S": ferme, "O": maison_abandonnee}
        maison_chef.exits = {"S": grande_place}
        maison_joueur.exits = {"E": bibliotheque, "O": exterieur_maison}
        exterieur_maison.exits = {"O": grande_place, "E": maison_joueur}
        cave.exits = {"N": maison_abandonnee}
        maison_abandonnee.exits = {"E": grande_place, "S": cave}
        bibliotheque.exits = {"O": maison_joueur}
        ferme.exits = {"N": grande_place}

        self.rooms.extend([grande_place, maison_chef, maison_joueur, exterieur_maison, cave, maison_abandonnee, bibliotheque, ferme])

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = grande_place

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
