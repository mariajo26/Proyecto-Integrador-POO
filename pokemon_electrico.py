from pokemon import Pokemon
from random import randint

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, 'Electrico', hp_maxima, energia_maxima)

    
    def atacar(self, oponente):
        super().atacar(oponente)

        aleatorio = randint(1, 100)

        if 0 < aleatorio <= 20:
            oponente.estado = 'Paralizado'
            print('Se paralizo')
            print(aleatorio)

        dano = Pokemon.dano

        self.tipo_dano(oponente, dano)
        
        oponente.hp_actual -= dano
    

    
    def tipo_ataque(self):
        print(f'¡{self.nombre} usa un ataque Electrico!')