from UserPokemon import userPokemon

pokemon_name = str(input("Ingrese el nombre del pokemon que desea usar: "))
pokemon = userPokemon(pokemon_name)

if pokemon:
    # print(f"{pokemon}")
    print(f"Elegiste a {pokemon['nombre']}!")
    print("Info sobre tu pokemon:")
    print(f"Nombre: {pokemon['nombre']}")
    print(f"Altura: {pokemon['altura']}")
    print(f"Peso: {pokemon['peso']}")
else:
    print("No se encontró el pokemón ingresado.")
