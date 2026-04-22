from abc import ABC, abstractmethod

class Pokemon(ABC):
    dano = 15

    def __init__(self, nombre, tipo, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.tipo = tipo

        self.__hp_maxima = hp_maximo
        self.__hp_actual = hp_maximo  # 🔧 CORRECCIÓN: inicializar privado correctamente

        self.__energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima

        self.estado = 'Normal'

    # -------- HP --------
    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, nueva_hp):
        if nueva_hp > self.__hp_maxima:
            self.__hp_actual = self.__hp_maxima
        elif nueva_hp < 0:
            self.__hp_actual = 0
        else:
            self.__hp_actual = nueva_hp

    # -------- ENERGIA --------
    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter 
    def energia_actual(self, nueva_energia):
        if nueva_energia > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        elif nueva_energia < 0:
            self.__energia_actual = 0
        else:
            self.__energia_actual = nueva_energia

    @property
    def energia_maxima(self):
        return self.__energia_maxima

    @property
    def hp_maxima(self):
        return self.__hp_maxima

    def atacar(self, oponente):
        self.energia_actual -= 15  
        self.tipo_ataque()

        if oponente.estado == 'Defensa':
            dano = Pokemon.dano * 2 / 3
            oponente.hp_actual -= dano
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def defender(self):
        self.energia_actual -= 5
        self.estado = 'Defensa'
        print(f'{self.nombre} levanto su escudo 🛡️ y aguanta un golpe 💪!')

    def descansar(self):
        self.energia_actual += 20
        print(f'{self.nombre} descansó 😴 y recuperó energía ❤️‍🩹')

    @abstractmethod
    def tipo_ataque(self):
        pass

    def tipo_dano(self, oponente, dano):
        if dano == Pokemon.dano * 2:
            print('¡Es súper efectivo!', end=' ')
        elif dano == Pokemon.dano * 2 / 3:
            print('No es muy efectivo...', end=' ')
        else:
            print('¡Es efectivo!', end=' ')

        print(f'{oponente.nombre} recibe {dano} puntos de daño.')

    def obtener_estado(self):
        return f'[HP: {self.__hp_actual}/{self.__hp_maxima}] [EP: {self.__energia_actual}/{self.__energia_maxima}]'