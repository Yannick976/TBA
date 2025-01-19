# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory=set()
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventoryroom(self):
        """
        Retourne l'inventaire de la salle
        """
        if ((not self.inventory) and (not self.characters)) :
            return "\nIl n'y a rien ici."
        
        content_return = "\nOn voit :"
        for obj in self.inventory:
            content_return += f"\n {obj.name} : {obj.description} ({obj.weight}kg)"
        for pnj in self.characters.values() :
            content_return += f"\n {pnj.name} : {pnj.description}"
        return content_return
    

    def get_character(self, name):        
        name_lower = name       
        for key in self.characters.keys():
            if key == name_lower:
                return self.characters[key]
        return None