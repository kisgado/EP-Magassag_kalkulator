from magassag import magassag


class Measurement:
    """
    A Bemenet és Kimenet osztályok ősosztálya.
    """
    def __init__(self, tav, teteje, alja):
        self.tav = float(tav)
        self.teteje = float(teteje)
        self.alja = float(alja)


class Bemenet(Measurement):
    """
    A bemeneti adatokat tárolására szolgál.
    """
    def __init__(self, tav, teteje, alja):
        super().__init__(tav, teteje, alja)

    def ki(self) -> list:
        """
        Kiszámítja a magasságot, és átadja a meglévő adatokkal együtt egy listában.\n
        Ennek az eredményével hozható létre Kimenet.\n
        :return: list
        """
        mag = magassag(self.tav, self.teteje, self.alja)
        return [self.tav, self.teteje, self.alja, mag]


class Kimenet(Measurement):
    """
    A kimeneti adatok tárolására szolgál. Létrehozásához a Bemenet osztály ki() függvénye használandó.
    """
    def __init__(self, lista):
        super().__init__(lista[0], lista[1], lista[2])
        self.mag = lista[3]
