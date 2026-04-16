from pokemon import Pokemon

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, 'Electrico', hp_maxima, energia_maxima)
