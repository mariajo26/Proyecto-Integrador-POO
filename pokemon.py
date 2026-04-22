from abc import ABC, abstractmethod

class Pokemon(ABC):
    dano = 15 # El daño x1 = 15 hp

    def __init__(self, nombre, tipo, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.tipo = tipo
        
        self.__hp_maxima = hp_maximo
        self.hp_actual = hp_maximo
        
        self.__energia_maxima = energia_maxima
        self.energia_actual = energia_maxima

        self.estado = 'Normal'

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
        if nueva_energia <= self.__energia_maxima:
            self.__energia_actual = nueva_energia 
        else:
            self.__energia_actual = self.__energia_maxima

    @property
    def energia_maxima(self):
        return self.__energia_maxima

    @property
    def hp_maxima(self):
        return self.__hp_maxima

    def atacar(self, oponente):
        self.__energia_actual -= 15
        self.tipo_ataque()

        if oponente.estado == 'Defensa':
            dano = Pokemon.dano / 3
            oponente.hp_actual -= dano
            self.tipo_dano(oponente, dano)
            return

    def defender(self):
        self.__energia_actual -= 5
        self.estado = 'Defensa'
        print(f'{self.nombre} se defendio')


    def descansar(self):
        self.energia_actual = self.__energia_actual + 20
        print(f'{self.nombre} descansó y recuperó 20 HP 💚')
    
    @abstractmethod
    def tipo_ataque(self):
        pass

    def tipo_dano(self, oponente, dano):
        if dano == Pokemon.dano * 2:
            print(f'¡Es súper efectivo!', end= ' ')
        elif dano == Pokemon.dano * 0.5:
            print(f'No es muy efectivo...', end= ' ')
        else:
            print(f'¡Es efectivo!', end= ' ')
        print(f'{oponente.nombre} recibe {dano} puntos de daño.')

    def obtener_estado(self):
        return f'[HP: {self.__hp_actual}/{self.hp_maxima}] [EP: {self.__energia_actual}/{self.energia_maxima}]'