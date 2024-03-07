import random


def mostrar_menu_principal():
    print("MENU PRINCIPAL:")
    print("1. Iniciar juego")
    print("2. Configuración")
    print("3. Salir")


def mostrar_menu_juego():
    print("\nMODO DE JUEGO:")
    print("1. Combate 1vs1")
    print("2. Combate 2vs2")
    print("3. Combate 3vs3")
    print("4. Combate 4vs4")
    print("5. Combate 6vs6")
    print("6. Combate Aleatorio")
    print("0. Volver atrás")


def mostrar_pokemons():
    print("\n¡ELIJE TU POKÉMON!")
    for i, pokemon in enumerate(pokemons):
        print(f"{i+1}. {pokemon}")
    print("0. Volver atrás")


def mostrar_stats_pokemon(pokemon):
    stats = pokemons_stats[pokemon]
    print(f"\nSTATS DE {pokemon.upper()}:")
    for stat, value in stats.items():
        print(f"{stat}: {value}")


def menu_seleccionar_pokemon(pokemon):
    print("\n¿vas a elegir este sensual Pokémon?")
    print(f"Pokemon seleccionado: {pokemon}")
    print("1. Continuar")
    print("0. Volver atrás")

    opcion = input("Selecciona una opción: ")
    return opcion


def seleccionar_pokemon(pokemon):
    print(f"Has seleccionado a {pokemon}. ¡Prepárate para la batalla!")
    return pokemon


def combate_1vs1(pokemon_1):
    print(f"Iniciando combate 1vs1 con {pokemon_1}...")
    # Acá va el código para el combate 1vs1


def combate_2vs2(pokemon_1, pokemon_2):
    print(f"Iniciando combate 2vs2 con {pokemon_1} y {pokemon_2}...")
    # Acá va el código para el combate 2vs2


def combate_3vs3(pokemon_1, pokemon_2, pokemon_3):
    print(
        f"Iniciando combate 3vs3 con {pokemon_1}, {pokemon_2} y {pokemon_3}...")
    # Acá va el código para el combate 3vs3


def combate_4vs4(pokemon_1, pokemon_2, pokemon_3, pokemon_4):
    print(
        f"Iniciando combate 4vs4 con {pokemon_1}, {pokemon_2}, {pokemon_3} y {pokemon_4}...")
    # Acá va el código para el combate 4vs4


def combate_6vs6(pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6):
    print(
        f"Iniciando combate 6vs6 con {pokemon_1}, {pokemon_2}, {pokemon_3}, {pokemon_4}, {pokemon_5} y {pokemon_6}...")
    # Acá va el código para el combate 6vs6


def combate_aleatorio():
    print("\n¿Cuántos pokémon quieres seleccionar automáticamente?")
    print("1. 1 Pokémon (1vs1)")
    print("2. 2 Pokémons (2vs2)")
    print("3. 3 Pokémons (3vs3)")
    print("4. 4 Pokémons (4vs4)")
    print("5. 6 Pokémons (6vs6)")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cantidad_pokemons = 1
    elif opcion == "2":
        cantidad_pokemons = 2
    elif opcion == "3":
        cantidad_pokemons = 3
    elif opcion == "4":
        cantidad_pokemons = 4
    elif opcion == "5":
        cantidad_pokemons = 6
    else:
        print("Opción no válida.")
        return

    print(f"\nSeleccionando {cantidad_pokemons} pokémons automáticamente...")
    pokemons_seleccionados = random.sample(pokemons, cantidad_pokemons)
    for pokemon in pokemons_seleccionados:
        print(f"Pokemon seleccionado: {pokemon}")

    print("\n¿Estás seguro de estos Pokémon seleccionados?")
    print("1. Continuar")
    print("0. Volver atrás")

    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        if cantidad_pokemons == 1:
            combate_1vs1(*pokemons_seleccionados)
        elif cantidad_pokemons == 2:
            combate_2vs2(*pokemons_seleccionados)
        elif cantidad_pokemons == 3:
            combate_3vs3(*pokemons_seleccionados)
        elif cantidad_pokemons == 4:
            combate_4vs4(*pokemons_seleccionados)
        elif cantidad_pokemons == 6:
            combate_6vs6(*pokemons_seleccionados)
    elif opcion == "0":
        return
    else:
        print("Opción no válida.")


def iniciar_combate_1vs1():
    while True:
        print("Selecciona tu Pokémon:")
        mostrar_pokemons()
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            return "back_to_pokemon_selection"

        pokemon_elegido = int(opcion) - 1
        if 0 <= pokemon_elegido < len(pokemons):
            pokemon_1 = pokemons[pokemon_elegido]
            mostrar_stats_pokemon(pokemon_1)
            menu_seleccionar_pokemon(pokemon_1)
            opcion_menu = input("Selecciona una opción: ")

            if opcion_menu == "1":
                seleccionar_pokemon(pokemon_1)
                combate_1vs1(pokemon_1)
                break
            elif opcion_menu == "0":
                continue
            else:
                print("Opción no válida.")
        else:
            print("Pokémon no válido.")


def iniciar_combate_2vs2():
    while True:
        print("Selecciona tu primer Pokémon:")
        mostrar_pokemons()
        opcion_1 = input("Selecciona el primer Pokémon: ")

        if opcion_1 == "0":
            return "back_to_pokemon_selection"

        pokemon_elegido_1 = int(opcion_1) - 1
        if 0 <= pokemon_elegido_1 < len(pokemons):
            pokemon_1 = pokemons[pokemon_elegido_1]
            mostrar_stats_pokemon(pokemon_1)

            # Mostrar el Pokémon seleccionado
            print(f"\nHas seleccionado a {pokemon_1}.")
            print("\nSelecciona tu segundo Pokémon:")
            mostrar_pokemons()  # Mostramos de nuevo el menú para elegir el segundo Pokémon
            opcion_2 = input("Selecciona el segundo Pokémon: ")

            if opcion_2 == "0":
                continue

            pokemon_elegido_2 = int(opcion_2) - 1
            if 0 <= pokemon_elegido_2 < len(pokemons):
                pokemon_2 = pokemons[pokemon_elegido_2]
                mostrar_stats_pokemon(pokemon_2)

                menu_seleccionar_pokemon(pokemon_2)
                opcion_menu = input("Selecciona una opción: ")

                if opcion_menu == "1":
                    seleccionar_pokemon(pokemon_1)
                    seleccionar_pokemon(pokemon_2)
                    combate_2vs2(pokemon_1, pokemon_2)
                    break
                elif opcion_menu == "0":
                    continue
                else:
                    print("Opción no válida.")
            else:
                print("Segundo Pokémon no válido.")
        else:
            print("Primer Pokémon no válido.")

# Aquí debes agregar las funciones para los combates 3vs3, 4vs4 y 6vs6 de manera similar


def menu_principal():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Selecciona una opción: ")

        if opcion_principal == "1":
            iniciar_juego()
        elif opcion_principal == "2":
            configuracion()
        elif opcion_principal == "3":
            print("Saliendo del juego. ¡Hasta luego!")
            break
        else:
            print("Opción no válida")


def iniciar_juego():
    while True:
        mostrar_menu_juego()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            result = iniciar_combate_1vs1()
            if result == "back_to_mode_selection":
                continue  # Continuar al siguiente ciclo del bucle
            break  # Salir del bucle después del combate
        elif opcion == "2":
            result = iniciar_combate_2vs2()
            if result == "back_to_mode_selection":
                continue  # Continuar al siguiente ciclo del bucle
            break  # Salir del bucle después del combate
        elif opcion == "3":
            combate_3vs3()
        elif opcion == "4":
            combate_4vs4()
        elif opcion == "5":
            combate_6vs6()
        elif opcion == "6":
            combate_aleatorio()
        elif opcion == "0":
            break  # Volver atrás al menú principal
        else:
            print("Opción no válida")


def configuracion():
    print("CONFIGURACIÓN DEL JUEGO")


# Lista de pokemons y sus stats
pokemons = ["Pikachu", "Onix"]
pokemons_stats = {
    "Pikachu": {"vida": 274, "Ataque": 229, "Defensa": 196},
    "Onix": {"vida": 180, "Ataque": 85, "Defensa": 292}
}

menu_principal()
