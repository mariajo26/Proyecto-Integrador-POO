import pokedex
from random import randint as aleatorio
import pokemon_agua, pokemon_electrico, pokemon_fuego, pokemon_planta


class Jugador:
    def __init__(self, es_cpu):
        self.pokemon = None
        self.es_cpu = es_cpu  # True si es computadora, False si es jugador

    def elegir_pokemon(self, no_jugador, excepcion):
        pokedex.mostrar_catalogo_disponible()
        numero_pokemons = len(pokedex.CATALOGO_POKEMON)

        while True:
            try:
                # Pedir selección al usuario
                opcion_pokemon = int(input(f'Jugador {no_jugador}, elija el número de su Pokémon: '))

                # Validar que el número sea válido y exista en el catálogo
                if opcion_pokemon <= 0 or opcion_pokemon > numero_pokemons:
                    print('[ERROR] El Pokémon no existe en el catálogo.')
                    continue

                # Evitar repetidos
                if opcion_pokemon == excepcion:
                    print('Ese Pokémon ya fue elegido, escoge otro.')
                    continue

                return opcion_pokemon

            except ValueError:
                print('[ERROR] Ingresa un número válido.')

    # Función para que la computadora elija pokemon
    def elegir_aleatoriamente(self, excepcion):
        numero_pokemons = len(pokedex.CATALOGO_POKEMON)
        print('Computadora eligiendo Pokémon...')

        while True:
            # Selección aleatoria
            opcion_pokemon = aleatorio(1, numero_pokemons)

            # Evitar repetición
            if opcion_pokemon != excepcion:
                return opcion_pokemon


class FabricaPokemon:
    # Método estitico que devuelve el id del pokemon
    @staticmethod
    def get_pokemon_id(pokemon):
        # Buscar ID del Pokémon por nombre
        for clave, datos in pokedex.CATALOGO_POKEMON.items():
            if datos['nombre'] == pokemon.nombre:
                return int(clave)

    # Método que devuelve el pokemon segun lo escoja el jugador
    @staticmethod
    def crear_pokemon(no_jugador, jugador, excepcion=0):
        # Elegir Pokémon según si es CPU o jugador
        if not jugador.es_cpu:
            opcion_pokemon = jugador.elegir_pokemon(no_jugador, excepcion)
        else:
            opcion_pokemon = jugador.elegir_aleatoriamente(excepcion)

        pokemon_elegido = pokedex.CATALOGO_POKEMON[str(opcion_pokemon)]

        nombre = pokemon_elegido['nombre']
        hp_maximo = pokemon_elegido['hp_maximo']
        ep_maximo = pokemon_elegido['energia_maxima']

        # Mensaje de selección
        if not jugador.es_cpu:
            print(f'¡Has seleccionado a {nombre}!')
        else:
            print(f'La computadora eligió a {nombre}!')

        # Crear instancia según tipo y retorna pokemon
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
                raise ValueError('Tipo de Pokémon inválido')