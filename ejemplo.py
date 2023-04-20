class clase1(object):
    instancias = []
    def __init__(self, atr) -> None:
        self.atr = atr
        clase1.instancias.append(self)

    def findInstance(self, atr):
        for instancia in clase1.instancias:
            if instancia.atr == atr
                return instancia
            else:
                return None