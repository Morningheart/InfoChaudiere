class chaudiere():
    __instance = None

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if chaudiere.__instance == None:
            chaudiere()
        return chaudiere.__instance