from threading import Thread

from process.store_Temp_actuel import tempActuel
from process.store_Temp_choisi import tempChoisi
from process.controlleur.mode_regule_pipe import result_commande

from enum import Enum

class Commande(Enum):
    ON = 1
    OFF = 0

class mode_regule():
    
    def __init__(self):
        print("Mode régulé initialisé")
        print("Température actuelle: " + str(tempActuel))
        print("Température choisie: " + str(tempChoisi))
        print("Commande: " + str(result_commande))
        Thread(target=self.update).start()

    def update(self):
        global result_commande
        if tempActuel > (tempChoisi + 2):
            result_commande = Commande.OFF
        elif tempActuel < (tempChoisi - 2):
            result_commande = Commande.ON
        else:
            result_commande = None
        print("Mode régulé mis à jour")
        print("Température actuelle: " + str(tempActuel))
        print("Température choisie: " + str(tempChoisi))
        print("Commande: " + str(result_commande))
        self.update()