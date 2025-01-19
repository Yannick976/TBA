"""
Description: coeur du jeu 
présente toutes les pieces, personnages etc
""" 
#import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item 
from character import Character

class Game:
    """
    La classe Game représente le jeu d'aventure dans lequel un joueur peut se déplacer dans un monde
    et interagir avec des objets et des personnages.
    """
    # Constructor
    def __init__(self):
        """
        constructeur des attribut de game
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items=[]
    # Setup the game
    def setup(self):
        """
        Initialise les attributs de la classe Game, y compris les pièces, commandes, et joueur.
        """
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", 
                     " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", 
                     Actions.go, 1
                     )
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
        grande_place = Room("La grande place", 
                            "sur une place centrale avec une grande fontaine au milieu."
                            )
        maison_chef = Room("Maison du chef", "dans la maison impressionnante du chef du village.")
        maison_joueur = Room("Maison du joueur", "dans la maison où Albert vous hébèrge.")
        exterieur_maison = Room("Extérieur de la maison", "devant l'entrée de votre maison.")
        cave = Room("Cave", "dans une cave sombre et mystérieuse.")
        maison_abandonnee = Room("Maison abandonnée", 
                                 "dans une maison décrépite, où règne une ambiance inquiétante."
                                 )
        entree_abandonnee = Room("Entrée maison abandonée", 
                                 "devant la porte d'une maison abandonnée"
                                 )
        taverne = Room("Taverne", "dans la teverne du village.")
        ferme = Room("Ferme", "dans un champ avec des cultures et des outils agricoles.")
        maison_fermier = Room("Mais du fermier", "dans la maison du fermier du village")

        #Setup des sorties
        grande_place.exits = {"N": maison_chef, "S": taverne, "O": ferme, "E": entree_abandonnee}
        maison_chef.exits = {"S": grande_place, "O": maison_fermier}
        maison_joueur.exits = {"O": exterieur_maison}
        exterieur_maison.exits = {"O": grande_place, "E": maison_joueur , "S" : taverne}
        cave.exits = {"S": maison_abandonnee}
        maison_abandonnee.exits = {"O": entree_abandonnee, "N": cave}
        taverne.exits = {"E": exterieur_maison , "N" :grande_place}
        ferme.exits = {"E": grande_place}
        maison_fermier.exits = {"O" : ferme}
        entree_abandonnee.exits = {"O" : grande_place,"E":maison_abandonnee}

        self.rooms.extend([grande_place, maison_chef, maison_joueur, exterieur_maison, cave, maison_abandonnee, taverne, ferme, maison_fermier, entree_abandonnee])

        #Setup des items
        cle = Item('clé',"une clé permettant d'ouvrir la porte du manoir" , 1, False)
        self.items.append(cle)
        taverne.inventory.add(cle)
        sword = Item('épée','une épée tranchante', 7, False)
        self.items.append(sword)
        piece = Item('pièce', 'une pièce précieuse', 0.1, False)
        maison_chef.inventory.add(piece)
        depouille =Item("dépouille", "le cadavre d'une jeune fille en décomposition", 35, False)
        self.items.append(depouille)
        ferme.inventory.add(depouille)
        telephone = Item('téléphone', 'un téléphone déchargé', 1, False)
        oreiller = Item("oreiller", "un oreiller parfait pour dormir", 1, False)
        maison_joueur.inventory.add(oreiller)
        journal = Item('journal', 
                       "le journal intime de Becker, la journaliste portée disparue", 
                       3 ,False
                       )
        cave.inventory.add(journal)
        verre = Item('verre', "un verre rempli proposé par le frère d'Albert", 2, False)
        taverne.inventory.add(verre)
        cle_voiture = Item("clé_voiture", "une clé servant à démarrer la voiture d'Albert", 1, False)
        ferme.inventory.add(cle_voiture)
        voiture = Item("voiture", "la voiture bleu d'Albert", 3000, False)
        grande_place.inventory.add(voiture)
        #Setup des characters
        fermier = Character("Fermier", "un fermier avec un sourire étrange", grande_place, ["Albert a perdu ses clefs de voiture en venant m'aider à travailler dans le champ, si tu les trouves fait moi signe."])
        maison_fermier.characters[fermier.name] = fermier
        chef = Character("Chef", "le chef du village avec son imposante carrure", maison_chef, ["Rends toi chez Albert, il aura sûrement de la place pour toi !"])
        maison_chef.characters[chef.name] = chef
        albert = Character("Albert", "un aimable villagois", maison_joueur,
                           ["Bienvenue dans notre village !"" Vous pouvez loger chez moi le temps de votre séjour, j'irai habiter chez mon frère entre temps."]
                           )
        maison_joueur.characters[albert.name] = albert
        frere = Character("Bruno", "Frère de Albert", 
                          taverne , ["Ahh tu es le petit nouveau ? Aller prend ce verre, cadedau de la maison."]
                          )
        taverne.characters[frere.name] = frere
        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom (qui vous servira de fausse identié): "))
        self.player.current_room = grande_place

        self.player.inventory['téléphone'] = telephone 

    # Play the game
    def play(self):
        """
        Lance le jeu, configure les éléments nécessaires et commence la boucle principale.
        """
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
        """
        Traite la commande entrée par le joueur et appelle l'action appropriée.
        """
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue."
                  " Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        """
        Affiche le message de bienvenue.
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("\nVous êtes un détective et avez entendu parlé d’une rumeur à propos d’un mystérieux village"
              " où aurait eu lieu plusieurs disparitions.")
        print("\nLe dernier en date étant celui de Mme Becker, une jeune journaliste de 24 ans.")
        print("Vous décidez donc de vous rendre dans ce village sous une fausse identité."
              "  afin d’éclaircir ce mystère.")
        print("\nEntrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())

    def isused(name, self):
        """
        determine si la clé est utilisable ou non 
        """
        if name == 'clé' :
            if self.player.current_room.name == self.entree_abandonnee :
                self.entree_abandonnee.exits['E'] = self.entree_abandonnee
                print("Vous avez ouvert la porte de la maison abandonnée.")
            else:
                print("La clé n'est pas utilisable ici.")
        else:
            print("L'objet n'est pas utilisable.")


def main():
    """
    Fonction principale pour demarre le jeu
    """
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
