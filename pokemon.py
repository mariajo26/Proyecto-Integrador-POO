from abc import ABC, abstractmethod


class Pokemon(ABC):
    dano = 15  # daño base

    def __init__(self, nombre, tipo, hp_maximo, energia_maxima):
        # atributos base del Pokémon
        self.nombre = nombre
        self.tipo = tipo

        self.__hp_maxima = hp_maximo
        self.__hp_actual = hp_maximo

        self.__energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima

        self.estado = 'Normal'

    # -------- HP --------

    @property
    def hp_actual(self):
        # retorna HP actual
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, nueva_hp):
        # asegura límites de HP (0 - max)
        if nueva_hp > self.__hp_maxima:
            self.__hp_actual = self.__hp_maxima
        elif nueva_hp < 0:
            self.__hp_actual = 0
        else:
            self.__hp_actual = nueva_hp

    # -------- ENERGÍA --------

    @property
    def energia_actual(self):
        # retorna energía actual
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, nueva_energia):
        # asegura límites de energía (0 - max)
        if nueva_energia > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        elif nueva_energia < 0:
            self.__energia_actual = 0
        else:
            self.__energia_actual = nueva_energia

    @property
    def energia_maxima(self):
        # retorna energía máxima
        return self.__energia_maxima

    @property
    def hp_maxima(self):
        # retorna HP máxima
        return self.__hp_maxima

    def atacar(self, oponente):
        # consume energía y realiza ataque
        self.energia_actual -= 15  
        self.tipo_ataque()

        # daño reducido si el oponente está defendiendo
        if oponente.estado == 'Defensa':
            dano = Pokemon.dano * 2 / 3
            oponente.hp_actual -= dano

    def cambiar_estado(self, nuevo_estado):
        # cambia estado del Pokémon
        self.estado = nuevo_estado

    def defender(self):
        # activa defensa y reduce energía
        self.energia_actual -= 5
        self.estado = 'Defensa'
        print(f'{self.nombre} levantó su escudo 🛡️!')

    def descansar(self):
        # recupera energía
        self.energia_actual += 20
        print(f'{self.nombre} descansó 😴 y recuperó energía ❤️‍🩹')

    @abstractmethod
    def tipo_ataque(self):
        # ataque específico por tipo
        pass

    def tipo_dano(self, oponente, dano):
        # muestra efectividad del ataque

        if dano == Pokemon.dano * 2:
            print('¡Es súper efectivo!', end=' ')
        elif dano == Pokemon.dano * 2 / 3:
            print('No es muy efectivo...', end=' ')
        else:
            print('¡Es efectivo!', end=' ')

        print(f'{oponente.nombre} recibe {dano} puntos de daño.')

    def obtener_estado(self):
        # devuelve estado actual del Pokémon
        return f'[HP: {self.__hp_actual}/{self.__hp_maxima}] [EP: {self.__energia_actual}/{self.__energia_maxima}]'