import time
from process.chaudiere.store import Compte_Rendu, Author, cr_controlleur, cr_chaudiere
from process.chaudiere.chaudiere import Chaudiere

class com_with_chaudiere():

    def __init__(self):
        print("Communication avec la chaudière initialisée")

    def demarrer(self):
        print("Tentative de lance de la chaudière")
        global cr_controlleur
        global cr_chaudiere
        cr_chaudiere = None
        new_cr = Compte_Rendu()
        new_cr.setAuthor(Author.CONTROLLEUR)
        new_cr.setContent("START")
        cr_controlleur = new_cr
        retour_demarrage = self.checkDemarrage()
        return retour_demarrage        
    
    def arreter(self):
        print("Chaudière arrêtée")
        global cr_controlleur
        global cr_chaudiere
        cr_chaudiere = None
        new_cr = Compte_Rendu()
        new_cr.setAuthor(Author.CONTROLLEUR)
        new_cr.setContent("STOP")
        cr_controlleur = new_cr
        retour_arret = self.checkArret()
        return retour_arret

    def checkDemarrage(self):
        for i in range(0, 10):
            time.sleep(1)
            if cr_chaudiere != None:
                if cr_chaudiere.getContent() == "START":
                    cr_chaudiere = None
                    return True
                elif cr_chaudiere.getContent() == "DEFAULT":
                    cr_chaudiere = None
                    return False
        if cr_chaudiere == None:
            print("Default de la chaudière")
            return False
        
    def checkArret(self):
        for i in range(0, 10):
            time.sleep(1)
            if cr_chaudiere != None:
                if cr_chaudiere.getContent() == "STOP":
                    cr_chaudiere = None
                    return True
                elif cr_chaudiere.getContent() == "DEFAULT":
                    cr_chaudiere = None
                    return False
        if cr_chaudiere == None:
            print("Default de la chaudière")
            return False