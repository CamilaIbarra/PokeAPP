from funciones_prueba import *

def randomPokemon():
    pokemonsId =range(1,150 + 1)
    randomId = random.choice(pokemonsId)
    llamarApi = consultaApiPokemon(randomId)  #obtener la información de un pokemon y tranformarlo en variable
    #guardarEstructuraPokemon(llamarApi , llamarApi["nombre"])
    return llamarApi
#Link dek Import random:https://www.w3schools.com/python/ref_random_choice.asp
#print(llamarApi)

#no crear archivos json - pedir desde la API