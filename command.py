"""
Ce module contient la classe Command qui représente une commande dans le jeu.
"""

class Command:
    """
    Cette classe représente une commande, 
    Composée d'un mot de commande, d'une chaîne d'aide, d'une action et d'un nombre de paramètres.

    Attributs:
        command_word (str): Le mot de commande.
        help_string (str): La chaîne d'aide.
        action (function): L'action à exécuter lorsque la commande est appelée.
        number_of_parameters (int): Le nombre de paramètres attendus pour la commande.

    Méthodes:
        __init__(self, command_word, help_string, action, number_of_parameters) : Le constructeur.
        __str__(self) : La représentation sous forme de chaîne de la commande.
    """

    # Le constructeur.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    # La représentation sous forme de chaîne de la commande.
    def __str__(self):
        return self.command_word + " " + self.help_string
  
