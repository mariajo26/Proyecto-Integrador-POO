from pokemon import Pokemon

class PokemonPlanta(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, hp_maxima, energia_maxima)