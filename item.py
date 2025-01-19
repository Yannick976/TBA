class Item:
    def __init__(self, name, description, weight, state):
        """
        Initialise un nouvel objet Item.

        :paramètre name: str, le nom de l'objet
        :paramètre description: str, la description de l'objet
        :paramètre weight: float, le poids de l'objet
        """
        self.name = name
        self.description = description
        self.weight = weight
        self.state = state

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.
        """
        return f"Item(name='{self.name}', description='{self.description}', weight={self.weight})"
    

  

    

