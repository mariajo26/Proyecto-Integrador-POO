from pokemon import Pokemon
import pokemon_agua, pokemon_fuego


class PokemonPlanta(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, 'Planta', hp_maxima, energia_maxima)

    def atacar(self, oponente):
        super().atacar(oponente)

        if isinstance(oponente, pokemon_agua.PokemonAgua):
            dano = Pokemon.dano * 2
        elif isinstance(oponente, pokemon_fuego.PokemonFuego):
            dano = Pokemon.dano * 2 / 3
        else:
            dano = Pokemon.dano
        
        self.tipo_dano(oponente, int(dano))
        
        oponente.hp_actual -= int(dano)     

    def tipo_ataque(self):
        print(f'¡{self.nombre} usa un ataque de Planta! 🍃')