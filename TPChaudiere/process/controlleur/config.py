from enum import Enum

class Mode(Enum):
    REGULE = 1
    PROGRAME = 2

current_mode = Mode.REGULE
heureDebut = 5
heureFin = 6
lastDefault = None