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
                print('❌ Entrada inválida. Escribí 1 o 2.')
        except ValueError: 
            print('❌ Ups esa opción ni es un número. Intenta de nuevo')
    return modo_juego

def mostrar_menu_acciones():
    print('¿Qué acción deseas realizar?')
    print('1. Atacar (Costo: 15 EP)')
    print('2. Defender (Costo: 5 EP)')
    print('3. Descansar (Restaura: 20 EP)')

# Devuelve la accón del pokemon - Jugador
def accion_jugador(jugador):
    energia = jugador.pokemon.energia_actual

    if energia == 0:
        print('⚠️ Tu energia es insuficiente para alguna acción. Descanso forzado')
        return 3

    mostrar_menu_acciones()

    while True:
        try:
            opcion = int(input('Elegí una opción: '))

            if opcion == 1 and energia < 15:
                print('❌ Energía insuficiente. Intenta nuevamente')
                continue

            if opcion == 2 and energia < 5:
                print('⚠️ Tu energia es insuficiente para alguna acción. Descanso forzado')
                return 3

            if opcion not in (1,2,3):
                print('❌ El número ni es una opción. Intente de nuevo')
                continue

            return opcion

        except ValueError:
            print('❌ Ups eso ni es un número. Intente nuevamente')


# Acción del pokemon - Computadora
# Retorna la acción que realizara
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

def mostrar_turno(jugador):
    print(f'\nTURNO DE {jugador.pokemon.nombre.upper()}', end=' ')
    print('(Computadora)' if jugador.es_cpu else '')

def manejar_estado(pokemon):
    if pokemon.estado == 'Paralizado':
        print('\n¡Estás paralizado! Turno perdido')
        pokemon.estado = 'Normal'
        return False  
    return True

def obtener_accion(jugador):
    if jugador.es_cpu:
        return accion_computadora(jugador)
    return accion_jugador(jugador)

def ejecutar_accion(accion, jugador, oponente):
    pokemon = jugador.pokemon

    match accion:
        case 1:
            pokemon.atacar(oponente.pokemon)
        case 2:
            pokemon.defender()
        case 3:
            pokemon.descansar()

    if pokemon.estado == 'Defensa':
        pokemon.estado = 'Normal'

def accion_pokemon(jugador, oponente):
    mostrar_turno(jugador)

    pokemon = jugador.pokemon

    if not manejar_estado(pokemon):
        return

    print(f'{pokemon.obtener_estado()}\n')

    accion = obtener_accion(jugador)

    print('')
    ejecutar_accion(accion, jugador, oponente)


def obtener_ganador(jugador1, jugador2):
    p1 = jugador1.pokemon
    p2 = jugador2.pokemon

    if p1.hp_actual <= 0 and p2.hp_actual <= 0:
        return 'Empate'
    elif p1.hp_actual <= 0:
        return p2.nombre
    elif p2.hp_actual <= 0:
        return p1.nombre
    
    return None

# --------- PRINCIPAL ---------

while True:
    modo_juego = menu_principal()

    jugador_1 = Jugador(False)
    jugador_1.pokemon = FabricaPokemon.crear_pokemon(1, jugador_1)
    excepcion = FabricaPokemon.get_pokemon_id(jugador_1.pokemon)

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
        
        ganador = obtener_ganador(jugador_1, jugador_2)

        if ganador == None:
            continue
        elif ganador == 'empate':
            print("\n¡Empate épico! Ambos Pokémon cayeron")
            break
        else:
            if ganador == jugador_1.pokemon.nombre:
                perdedor = jugador_2.pokemon.nombre
            else:
                perdedor = jugador_1.pokemon.nombre

            print(f'\n¡{perdedor} ha sido derrotado en combate! 😵')
            print(f'\n¡Felicidades {ganador} ha ganado 🏆🥇!')
            break