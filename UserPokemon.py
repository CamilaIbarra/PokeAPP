from funciones_prueba import *

def userPokemon():
    pokemon_name = str(input("Ingrese el nombre del pokemon que desea usar: "))
    pokemon = consultaApiPokemon(pokemon_name)
    dir = 'user'
    guardarEstructuraPokemon(dir, pokemon, pokemon["nombre"])
    