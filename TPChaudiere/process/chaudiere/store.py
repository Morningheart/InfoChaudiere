chaudiereAllumee = False
cr_controlleur = None
cr_chaudiere = None

from enum import Enum

class Author(Enum):
    CONTROLLEUR = 1
    CHAUDIERE = 2

class Compte_Rendu():

    def __init__(self):
        self.author = None
        self.content = None

    def setAuthor(self, author):
        self.author = author

    def setContent(self, content):
        self.content = content

    def getAuthor(self):
        return self.author
    
    def getContent(self):
        return self.content
    
    def __str__(self):
        return "Author: " + str(self.author) + "\nContent: " + str(self.content)
    