from jugador import Jugador, FabricaPokemon
from random import randint as aleatorio


# -------- MENÚ PRINCIPAL --------
def menu_principal():
    # Mostrar título del juego
    print('='*50)
    print(f'{"SIMULADOR DE BATALLAS POKÉMON (POO)":^50}')
    print('='*50)

    print('Seleccione el Modo de Juego:')
    print('1. Jugador vs Jugador')
    print('2. Jugador vs Computadora')

    while True:
        try:
            # Leer modo de juego
            modo_juego = int(input('Elegí una opción (1 o 2): '))

            # Validar opción
            if modo_juego in (1, 2):
                break
            else:
                print('❌ Entrada inválida. Escribí 1 o 2.')

        except ValueError:
            print('❌ Debes ingresar un número válido')

    return modo_juego


def mostrar_menu_acciones():
    # Mostrar acciones disponibles del turno
    print('¿Qué acción deseas realizar?')
    print('1. Atacar (Costo: 15 EP)')
    print('2. Defender (Costo: 5 EP)')
    print('3. Descansar (Restaura: 20 EP)')


# -------- ACCIONES DEL JUGADOR --------
def accion_jugador(jugador):
    pokemon = jugador.pokemon
    energia = pokemon.energia_actual

    # Si no hay energía, fuerza descanso
    if energia == 0:
        print('⚠️ Energía insuficiente. Descanso forzado')
        return 3

    mostrar_menu_acciones()

    while True:
        try:
            # Elegir acción
            opcion = int(input('Elegí una opción: '))

            # Validar energía para atacar
            if opcion == 1 and energia < 15:
                print('❌ Energía insuficiente')
                continue

            # Validar energía para defender
            if opcion == 2 and energia < 5:
                print('⚠️ Energía insuficiente. Descanso forzado')
                return 3

            # Validar opción
            if opcion not in (1, 2, 3):
                print('❌ Opción inválida')
                continue

            return opcion

        except ValueError:
            print('❌ Ingresa un número válido')


# -------- ACCIONES DE LA CPU --------
def accion_computadora(jugador):
    pokemon = jugador.pokemon

    energia = pokemon.energia_actual
    energia_max = pokemon.energia_maxima
    vida = pokemon.hp_actual

    # Estrategia según estado del Pokémon
    if vida <= 15:
        return 1 if aleatorio(1, 100) <= 70 else 2

    elif energia == energia_max:
        return 1  # ataque agresivo

    elif energia <= 5:
        return 3  # descansar

    elif energia < 15:
        return aleatorio(1, 2)

    else:
        # comportamiento balanceado
        probabilidad = aleatorio(1, 100)
        if probabilidad <= 60:
            return 1
        elif probabilidad <= 85:
            return 2
        else:
            return 3


# -------- CONTROL DE TURNO --------
def mostrar_turno(jugador):
    # Mostrar jugador activo
    print(f'\nTURNO DE {jugador.pokemon.nombre.upper()}', end=' ')
    print('(CPU)' if jugador.es_cpu else '')


def manejar_estado(pokemon):
    # Si está paralizado, pierde turno
    if pokemon.estado == 'Paralizado':
        print('\n¡Paralizado! Pierde el turno')
        pokemon.estado = 'Normal'
        return False
    return True


def obtener_accion(jugador):
    # Obtener acción según tipo de jugador
    if jugador.es_cpu:
        return accion_computadora(jugador)
    return accion_jugador(jugador)


def ejecutar_accion(accion, jugador, oponente):
    pokemon = jugador.pokemon

    # Ejecutar acción seleccionada
    match accion:
        case 1:
            pokemon.atacar(oponente.pokemon)
        case 2:
            pokemon.defender()
        case 3:
            pokemon.descansar()

    # Reset estado defensa después de usarlo
    if pokemon.estado == 'Defensa':
        pokemon.estado = 'Normal'


def accion_pokemon(jugador, oponente):
    # Ejecutar turno completo
    mostrar_turno(jugador)

    pokemon = jugador.pokemon

    if not manejar_estado(pokemon):
        return

    print(pokemon.obtener_estado(), '\n')

    accion = obtener_accion(jugador)
    ejecutar_accion(accion, jugador, oponente)


# -------- CONDICIÓN DE VICTORIA --------
def obtener_ganador(jugador1, jugador2):
    p1 = jugador1.pokemon
    p2 = jugador2.pokemon

    # Ambos derrotados
    if p1.hp_actual <= 0 and p2.hp_actual <= 0:
        return 'Empate'

    # Solo jugador 1 pierde
    elif p1.hp_actual <= 0:
        return p2.nombre

    # Solo jugador 2 pierde
    elif p2.hp_actual <= 0:
        return p1.nombre

    return None


# -------- JUEGO PRINCIPAL --------
while True:
    modo_juego = menu_principal()

    # Crear jugador 1
    jugador_1 = Jugador(False)
    jugador_1.pokemon = FabricaPokemon.crear_pokemon(1, jugador_1)

    # Evitar repetir Pokémon
    excepcion = FabricaPokemon.get_pokemon_id(jugador_1.pokemon)

    # Crear jugador 2 según modo
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
    print(f'{pokemon_1.nombre} ({pokemon_1.tipo}) vs {pokemon_2.nombre} ({pokemon_2.tipo})')
    print('-' * 30)

    turno = True

    # Loop de combate
    while True:
        if turno:
            accion_pokemon(jugador_1, jugador_2)
            turno = False
        else:
            accion_pokemon(jugador_2, jugador_1)
            turno = True

        ganador = obtener_ganador(jugador_1, jugador_2)

        # Si no hay ganador, sigue el combate
        if ganador is None:
            continue

        # Empate
        if ganador == 'Empate':
            print("\n¡Empate épico! Ambos Pokémon cayeron")
            break

        # Hay ganador
        if ganador == jugador_1.pokemon.nombre:
            perdedor = jugador_2.pokemon.nombre
        else:
            perdedor = jugador_1.pokemon.nombre

        print(f'\n¡{perdedor} fue derrotado 😵!')
        print(f'¡{ganador} gana el combate 🏆!')
        break