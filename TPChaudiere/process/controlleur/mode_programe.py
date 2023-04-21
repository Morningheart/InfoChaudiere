import time
from enum import Enum
from threading import Thread

from process.controlleur.config import current_mode, heureDebut, heureFin, Mode
from process.controlleur.mode_regule_pipe import result_commande
from process.controlleur.mode_programe_pipe import result_commande as result_commande_programe

class Commande(Enum):
    ON = 1
    OFF = 2

class mode_programe():
    
    def __init__(self):
        print("Mode programmé initialisé")
        print("Heure de début: " + str(heureDebut))
        print("Heure de fin: " + str(heureFin))
        print("Commande: " + str(result_commande_programe))
        Thread(target=self.update).start()

    def update(self):
        result_commande_programe = self.commandeToReturn()
        print("Mode programmé mis à jour")
        print("Heure de début: " + str(heureDebut))
        print("Heure de fin: " + str(heureFin))
        print("Commande: " + str(result_commande_programe))
        self.update()
    
    def commandeToReturn(self):
        heure = time.localtime().tm_hour
        if current_mode == Mode.REGULE:
            return result_commande
        elif current_mode == Mode.PROGRAME:
            if not(heure >= heureDebut and heure <= heureFin):
                return result_commande
            return Commande.ON
        else:
            return None