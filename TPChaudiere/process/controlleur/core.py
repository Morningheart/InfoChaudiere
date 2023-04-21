import time
from TPChaudiere.process.store_dijoncteur import dijoncteur_coupe
from TPChaudiere.process.controlleur.config import lastDefault

class controlleur():
    __instance = None

    def __init__(self):
        self.etatChaudiere = False
        from process.controlleur.mode_regule import mode_regule
        from process.controlleur.mode_programe import mode_programe
        from process.controlleur.com_with_chaudiere import com_with_chaudiere

        self.mode_regule = mode_regule()
        self.mode_programe = mode_programe()
        self.com_with_chaudiere = com_with_chaudiere()
        self.etatChaudiere = False

    @staticmethod
    def getInstance():
        if controlleur.__instance == None:
            controlleur()
        return controlleur.__instance
    
    def demarrer(self):
        global lastDefault
        if self.checkDijoncteur() and self.checkLastDefault():
            if self.etatChaudiere == False:
                self.etatChaudiere = None
                demarrage = self.com_with_chaudiere.demarrer()
                if demarrage == True:
                    self.etatChaudiere = True
                    return True
                else:
                    lastDefault = time.time()
                    self.etatChaudiere = False
                    return False

    def arreter(self):
        global lastDefault
        if self.checkDijoncteur():
            if self.etatChaudiere == True:
                self.etatChaudiere = None
                arret = self.com_with_chaudiere.arreter()
                if arret == True:
                    self.etatChaudiere = False
                    return True
                else:
                    lastDefault = time.time()
                    self.etatChaudiere = False
                    return False

    def checkLastDefault(self):
        # Regarde si le dernier default est supérieur à 5 minutes
        global lastDefault
        if lastDefault != None:
            current_time = time.time()
            if current_time - lastDefault > 300:
                print("[Default] Veuillez attendre encore {0} secondes ...".format(300 - (current_time - lastDefault)))
                return False
            else:
                return True
        else:
            return True
        
    def checkDijoncteur(self):
        if dijoncteur_coupe == True:
            print("[Default] Veuillez réenclencher le dijoncteur ...")
            return False
        else:
            return True
        
    