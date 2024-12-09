# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []  # Historique des pièces visitées
    
    # Define the move method.
    def move(self, direction):
         # Vérifiez si la direction est valide dans les sorties de la pièce actuelle.
        next_room = self.current_room.exits.get(direction)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
         # Ajoutez la description de la pièce actuelle à l'historique si elle n'y est pas encore.
        if self.current_room.description not in self.history:
            self.history.append(self.current_room.description)
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        # Retourne l'historique des pièces visitées
        return "\n".join([f"- {desc}" for desc in self.history]) if self.history else "Aucun historique de visites."
    
