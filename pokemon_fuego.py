from pokemon import Pokemon
import pokemon_agua, pokemon_planta

class PokemonFuego(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, 'Fuego', hp_maxima, energia_maxima)

    def atacar(self, oponente):
        super().atacar(oponente)

        if isinstance(oponente, pokemon_planta.PokemonPlanta):
            dano = Pokemon.dano * 2
        elif isinstance(oponente, pokemon_agua.PokemonAgua):
            dano = Pokemon.dano / 3
        else:
            dano = Pokemon.dano
        
        self.tipo_dano(oponente, dano)
        
        oponente.hp_actual -= dano

    def tipo_ataque(self):
        print(f'¡{self.nombre} usa un ataque de Fuego!')