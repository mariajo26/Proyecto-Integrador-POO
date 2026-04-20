from abc import ABC, abstractmethod

class Pokemon(ABC):

    def __init__(self, nombre, tipo, hp_inicial, energia_inicial):
        self.nombre = nombre
        self.tipo = tipo
        self.hp_actual = hp_inicial
        self.hp_maxima = hp_inicial
        self.energia_actual = energia_inicial
        self.energia_maxima = energia_inicial

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
        print(f'{self.nombre} ataco')

    def defender(self):
        print(f'{self.nombre} se defendio')


    def descansar(self):
        print(f'{self.nombre} restauro vida')

    def __str__(self):
        return f'[HP: {self.__hp_actual}/{self.hp_maxima}] [EP: {self.__energia_actual}/{self.energia_maxima}]'