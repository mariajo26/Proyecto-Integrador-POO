from pokemon import Pokemon
import pokemon_fuego, pokemon_planta

class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, 'Agua',hp_maxima, energia_maxima)

    def atacar(self, oponente):
        super().atacar(oponente)
        if isinstance(oponente, pokemon_fuego.PokemonFuego):
            dano = Pokemon.dano * 2
        elif isinstance(oponente, pokemon_planta.PokemonPlanta):
            dano = Pokemon.dano / 3
        else:
            dano = Pokemon.dano
        
        self.tipo_dano(oponente, dano)
        
        oponente.hp_actual -= dano

    def tipo_ataque(self):
        print(f'¡{self.nombre} usa un ataque de Agua!')
        