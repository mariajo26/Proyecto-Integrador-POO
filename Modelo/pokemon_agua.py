from pokemon import Pokemon

class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, 'Agua',hp_maxima, energia_maxima)