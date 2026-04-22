from jugador import Jugador, FabricaPokemon
from random import randint as aleatorio

# -----------
# Menú principal, modo de Juego
def menu_principal():
    print('='*50)
    print(f'{"SIMULADOR DE BATALLAS POKÉMON (POO)":^50}')
    print('='*50)
    print('Seleccione el Modo de Juego:')
    print('1. Jugador vs Jugador')
    print('2. Jugador vs Computadora')

    while True:
        try:
            modo_juego = int(input('Elegí una opción (1 o 2): '))
            if modo_juego in (1,2):
                break
            else:
                print('[ERROR] Entrada inválida. Escribí 1 o 2.')
        except ValueError: 
            print('[ERROR] Ups esa opción ni es un número. Intenta de nuevo')
    return modo_juego


# Menu de acción del pokemon
def accion_jugador(jugador):
    print('¿Qué acción deseas realizar?')
    print('1. Atacar (Costo: 15 EP)')
    print('2. Defender (Costo: 5 EP)')
    print('3. Descansar (Restaura: 20 EP)')

    enregia_pokemon = jugador.pokemon.energia_actual

    while True:
        if enregia_pokemon <= 0:
            accion_jugador = 3
            print(f'[ALERTA] {jugador.pokemon.nombre} descansará para recuperar energía')
            break

        try:
            accion_jugador = int(input('Elegí una opción: '))

            if accion_jugador in (1,2,3):
                if accion_jugador == 1 and enregia_pokemon < 15:
                    print('[ERROR] Tu energía es muy baja para atacar')
                else:
                    break
            else:
                print('[ERROR] Entrada inválida. Intente nuevamente.')

        except ValueError:
            print('[ERROR] Ups esa opción ni es un número. Intente nuevamente.')

    return accion_jugador


def accion_computadora(jugador):
    pokemon = jugador.pokemon

    energia = pokemon.energia_actual
    energia_max = pokemon.energia_maxima
    vida = pokemon.hp_actual

    if vida <= 15:
        probabilidad = aleatorio(1, 100)
        if probabilidad <= 70:
            return 1 # atacar
        else:
            return 2 # defender

    elif energia == energia_max:
        return 1 # atacar

    elif energia <= 5:
        return 3 # descansar

    elif energia < 15:
        return aleatorio(1, 2)

    else:
        probabilidad = aleatorio(1, 100)
        if probabilidad <= 60:
            return 1 # atacar
        elif probabilidad <= 85:
            return 2 # defender
        else:
            return 3 # descansar


def accion_pokemon(jugador, oponente):
    print(f'\nTURNO DE {jugador.pokemon.nombre.upper()}', end=' ')

    if jugador.es_cpu:
        print('(Computadora)')
    else:
        print('')

    if not jugador.pokemon.estado == 'Paralizado':
        print(f'{jugador.pokemon.obtener_estado()}\n')

        if not jugador.es_cpu:
            accion = accion_jugador(jugador)
        else:
            accion = accion_computadora(jugador)

        print('')

        match accion:
            case 1:
                jugador.pokemon.atacar(oponente.pokemon)
            case 2:
                jugador.pokemon.defender()
            case 3:
                jugador.pokemon.descansar()

        if jugador.pokemon.estado == 'Defender':
            jugador.pokemon.estado = 'Normal'

    else:
        print('\n¡Estás paralizado! Turno perdido')
        jugador.pokemon.estado = 'Normal'


# --------- PRINCIPAL ---------

while True:
    modo_juego = menu_principal()

    jugador_1 = Jugador(False)
    jugador_1.pokemon = FabricaPokemon.crear_pokemon(1, jugador_1)
    excepcion = FabricaPokemon.obtener_opcion(jugador_1.pokemon)

    match modo_juego:
        case 1:
            jugador_2 = Jugador(False)
        case 2:
            jugador_2 = Jugador(True)
        case _:
            break
    
    jugador_2.pokemon = FabricaPokemon.crear_pokemon(2, jugador_2, excepcion)

    pokemon_1 = jugador_1.pokemon
    pokemon_2 = jugador_2.pokemon

    print('¡COMIENZA LA BATALLA!')
    print(f'\n{pokemon_1.nombre} ({pokemon_1.tipo}) vs {pokemon_2.nombre} ({pokemon_2.tipo})')
    print('-' * 30)

    turno = True

    while True:
        if turno:
            accion_pokemon(jugador_1, jugador_2)
            turno = False
        else:
            accion_pokemon(jugador_2, jugador_1)
            turno = True

        if jugador_1.pokemon.hp_actual <= 0 and jugador_2.pokemon.hp_actual <= 0:
            print("\n¡Empate épico! Ambos Pokémon cayeron")
            break

        elif jugador_1.pokemon.hp_actual <= 0:
            print(f'\n¡{jugador_2.pokemon.nombre} ha sido derrotado en combate!')
            print(f'\n¡Felicidades {jugador_2.pokemon.nombre} ha ganado!')
            break

        elif jugador_2.pokemon.hp_actual <= 0:
            print(f'\n¡{jugador_1.pokemon.nombre} ha sido derrotado en combate!')
            print(f'\n¡Felicidades {jugador_1.pokemon.nombre} ha ganado!')
            break