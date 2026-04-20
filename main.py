# from Modelo import pokemon_agua, pokemon_electrico, pokemon_fuego, pokemon_planta
import pokedex
from pokemon_clases import pokemon_agua, pokemon_electrico, pokemon_fuego, pokemon_planta 
from random import randint as aleatorio

# ---------

def elegir_pokemon(opcion_pokemon):
    pokemon_elegido = pokedex.CATALOGO_POKEMON[opcion_pokemon]

    nombre = pokemon_elegido['nombre']
    hp_maximo = pokemon_elegido['hp_maximo']
    ep_maximo = pokemon_elegido['energia_maxima']

    match pokemon_elegido['tipo']:
        case 'Fuego':
            pokemon = pokemon_fuego.PokemonFuego(nombre, hp_maximo, ep_maximo)
        case 'Agua':
            pokemon = pokemon_agua.PokemonAgua(nombre, hp_maximo, ep_maximo)
        case 'Planta':
            pokemon = pokemon_planta.PokemonPlanta(nombre, hp_maximo, ep_maximo)
        case 'Electrico':
            pokemon = pokemon_electrico.PokemonElectrico(nombre, hp_maximo, ep_maximo)
        case __:
            print('Error')
    return pokemon

# --------- PRINCIPAL ---------

# Menú principal, modo de Juego
print('='*50)
print(f'{"SIMULADOR DE BATALLAS POKÉMON (POO)":^50}')
print('='*50)
print('Seleccione el Modo de Juego:')
print('1. Jugador vs Jugador')
print('2. Jugador vs Computadora')
modo_juego = int(input('Opción: '))

while True:
    pokedex.mostrar_catalogo_disponible()

    opcion_pokemon = input('Jugador 1, elija el número de su Pokémon: ')
    pokemon_jugador_1 = elegir_pokemon(opcion_pokemon)
    print(f'¡Has seleccionado a {pokemon_jugador_1.nombre}!')

    if modo_juego == 1:
        pokedex.mostrar_catalogo_disponible()
        opcion_pokemon = input('Jugador 2, elija el número de su Pokémon: ')
        
        pokemon_jugador_2 = elegir_pokemon(opcion_pokemon)

        print(f'¡Has seleccionado a {pokemon_jugador_2.nombre}!')
        break
    elif modo_juego == 2:
        print('Computadora eligiendo combatiente...')
        pokemon_jugador_2 = elegir_pokemon(aleatorio(1,7))

        print(f'¡La computadora ha seleccionado a {pokemon_jugador_2.nombre}!')
        break
    else: 
        print('Modo de juego incorrecto')