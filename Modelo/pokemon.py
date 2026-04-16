from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        self.nombre = nombre
        self.__hp_actual = self.hp_actual(hp_maxima)
        self.__energia_actual = self.energia_actual(energia_maxima)

    @property
    def hp_actual(self):
        return self.__hp_actual
    
    @hp_actual.setter
    def hp_actual(self, nueva_hp):
        self.__hp_actual = nueva_hp

    @property
    def energia_actual(self):
        return self.__energia_actual
    
    @hp_actual.setter
    def energia_actual(self, nueva_energia):
        self.__energia_actual = nueva_energia 

    def atacar(self):
        pass

    def defender(self):
        pass

    def descansar(self):
        pass