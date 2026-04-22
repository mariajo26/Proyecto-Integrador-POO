import pokedex
from random import randint as aleatorio
import pokemon_agua, pokemon_electrico, pokemon_fuego, pokemon_planta


class Jugador:
    def __init__(self, es_cpu):
        self.pokemon = None
        self.es_cpu = es_cpu
    
    def elegir_pokemon(self, no_jugador, excepcion):
        pokedex.mostrar_catalogo_disponible()
        numero_pokemons = len(pokedex.CATALOGO_POKEMON)

        while True:
            try:
                opcion_pokemon = int(input(f'Jugador {no_jugador}, elija el número de su Pokémon: '))

                if opcion_pokemon <= 0 or opcion_pokemon > numero_pokemons:
                    print('[ERROR] No existe el Pokémon. Ingresa un número válido.')
                    continue

                if opcion_pokemon == excepcion:
                    print('\nEscoge otro Pokémon. Ese ya está repetido.\n')
                    continue

                return opcion_pokemon

            except ValueError:
                print('[ERROR] Eso no es un número válido. Intenta de nuevo.')
    

    def elegir_aleatoriamente(self, excepcion):
        numero_pokemons = len(pokedex.CATALOGO_POKEMON)
        print('\nComputadora eligiendo combatiente...')

        while True:
            opcion_pokemon = aleatorio(1, numero_pokemons)
            if opcion_pokemon != excepcion:
                return opcion_pokemon


class FabricaPokemon:
    @staticmethod
    def get_pokemon_id(pokemon):
        for clave, datos in pokedex.CATALOGO_POKEMON.items():
            if datos['nombre'] == pokemon.nombre:
                return int(clave)
            
    @staticmethod
    def crear_pokemon(no_jugador, jugador, excepcion=0):
        if not jugador.es_cpu:
            opcion_pokemon = jugador.elegir_pokemon(no_jugador, excepcion)
        else:
            opcion_pokemon = jugador.elegir_aleatoriamente(excepcion)

        pokemon_elegido = pokedex.CATALOGO_POKEMON[str(opcion_pokemon)]

        nombre = pokemon_elegido['nombre']
        hp_maximo = pokemon_elegido['hp_maximo']
        ep_maximo = pokemon_elegido['energia_maxima']

        if not jugador.es_cpu:
            print(f'¡Has seleccionado a {nombre}!')
        else:
            print(f'¡La computadora ha seleccionado a {nombre}!')

        match pokemon_elegido['tipo']:
            case 'Fuego':
                return pokemon_fuego.PokemonFuego(nombre, hp_maximo, ep_maximo)
            case 'Agua':
                return pokemon_agua.PokemonAgua(nombre, hp_maximo, ep_maximo)
            case 'Planta':
                return pokemon_planta.PokemonPlanta(nombre, hp_maximo, ep_maximo)
            case 'Electrico':
                return pokemon_electrico.PokemonElectrico(nombre, hp_maximo, ep_maximo)
            case _:
                raise ValueError('[ERROR] Tipo de Pokémon no existe')