
# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item 
from character import Character


class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items=[]
    
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
        inventory = Command("inventory"," : affiche l'inventaire du joueur", Actions.inventory, 0)
        self.commands["inventory"] = inventory
        look = Command("look", " : Regarder autour de soi", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <objet> : prendre un objet", Actions.take,1)
        self.commands["take"] = take
        drop = Command("drop", " <objet> : reposer un objet", Actions.drop,1)
        self.commands["drop"] = drop
        check = Command("check", " : affiche l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        use = Command("use", " : utilise un item de ton inventaire", Actions.use, 1)
        self.commands["use"] = use
        talk = Command("talk", " : interagir avec un pnj de la même piece", Actions.talk, 1)
        self.commands["talk"] = talk
        
        


        
        # Setup des pièces 
        grande_place = Room("La grande place", "sur une place centrale avec une grande fontaine au milieu.")
        maison_chef = Room("Maison du chef", "dans la maison impressionnante du chef du village.")
        maison_joueur = Room("Maison du joueur", "dans votre propre maison chaleureuse.")
        exterieur_maison = Room("Extérieur de la maison", "devant l'entrée de votre maison.")
        cave = Room("Cave", "dans une cave sombre et mystérieuse.")
        maison_abandonnee = Room("Maison abandonnée", "dans une maison décrépite, où règne une ambiance inquiétante.")
        entree_abandonnee = Room("Entrée maison abandonée", "devant la porte d'une maison abandonnée")
        taverne = Room("Taverne", "dans la teverne du village.")
        ferme = Room("Ferme", "dans un champ avec des cultures et des outils agricoles.")
        maison_fermier = Room("Mais du fermier", "dans la maison du fermier du village")


        #Setup des sorties

        grande_place.exits = {"N": maison_chef, "S": taverne, "O": ferme, "E": entree_abandonnee}
        maison_chef.exits = {"S": grande_place, "O": maison_fermier}
        maison_joueur.exits = {"O": exterieur_maison}
        exterieur_maison.exits = {"O": grande_place, "E": maison_joueur , "O" : taverne}
        cave.exits = {"S": maison_abandonnee}
        maison_abandonnee.exits = {"E": entree_abandonnee, "N": cave}
        taverne.exits = {"E": exterieur_maison , "N" :grande_place}
        ferme.exits = {"E": grande_place}
        maison_fermier.exits = {"O" : ferme}
        entree_abandonnee.exits = {"O" : grande_place}

        self.rooms.extend([grande_place, maison_chef, maison_joueur, exterieur_maison, cave, maison_abandonnee, taverne, ferme, maison_fermier, entree_abandonnee])


        #Setup des items
        cle = Item('clé',"une clé permettant d'ouvrir la porte du manoir" , 1, False)
        self.items.append(cle)
        taverne.inventory.add(cle)
        if cle.state == True:
            if self.player.current_room == entree_abandonnee:
                entree_abandonnee.exits['E']= maison_abandonnee
                print("Vous avez ouvert la pporte de la maison abandonnée")
            else :
                print("La clé n'est pas utilisable ici.")

        
        sword = Item('épée','une épée tranchante', 7, False)
        self.items.append(sword)
        piece = Item('pièce', 'une pièce précieuse', 0.1, False)
        maison_chef.inventory.add(piece)
        depouille =Item("dépouille", "le cadavre d'une jeune fille en décomposition", 35,  False)
        self.items.append(depouille)
        ferme.inventory.add(depouille)
        telephone = Item('téléphone', 'un téléphone déchargé', 1,  False)


        #Setup des characters
        fermier = Character("Fermier", "un fermier avec un sourire étrange", grande_place, ["Il se fait tard, à demain !"])
        maison_fermier.characters[fermier.name] = fermier
        chef = Character("Chef", "le chef du village avec son imposante carrure", maison_chef, ["Rends toi chez Albert, il aura sûrement de la place pour toi !"])
        maison_chef.characters[chef.name] = chef

        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom (qui vous servira de fausse identié): "))
        self.player.current_room = grande_place

        self.player.inventory['téléphone'] = telephone 




    #Setup des utilisations des objets




    """
    def move_characters(self) :
        for room in self.rooms :
            for character in room.characters.values():
                character.move()
                character.has_moved = False
                """


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            #self.move_characters()
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
        print("\nVous êtes un détective et avez entendu parlé d’une rumeur à propos d’un mystérieux village où aurait eu lieu plusieurs disparitions.")
        print("\nLe dernier en date étant celui de Mme Becker, une jeune journaliste de 24 ans.")
        print("Vous décidez donc de vous rendre dans ce village sous une fausse identité  afin d’éclaircir ce mystère.")
        print("\nEntrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())






    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
