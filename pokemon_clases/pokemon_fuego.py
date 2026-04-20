from pokemon import Pokemon

class PokemonFuego(Pokemon):
    def __init__(self, nombre, hp_maxima, energia_maxima):
        super().__init__(nombre, 'Fuego', hp_maxima, energia_maxima)

    def atacar(self):
        return super().atacar()