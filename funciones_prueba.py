import requests
import json
import random

apiOk = 200

def consultaApiPokemon(id):
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(id))
        if response.status_code == apiOk:
            data = response.json()
            return crearEstructuraPokemon(data)
        else:
            return None
    except Exception as e:
        print(f"Error al obtener información del ID Pokemon {id}: {e}")
        return None

def crearEstructuraPokemon(data):
    return {
        "nombre": data["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "tipos": [tipo["type"]["name"] for tipo in data["types"]],
        # Puedes agregar más campos según tus necesidades
    }

guardarJson = consultaApiPokemon(5)

def guardarEstructuraPokemon(guardarJson):
    with open("nombre_archivo.json", "w") as json_file:
        json.dump(guardarJson, json_file, indent=2)
    print(guardarJson)
guardarEstructuraPokemon(guardarJson)
#guardarEstructuraPokemon(consultaApiPokemon("pikachu"))

def randomPokemon():
    pokemonsId =range(1,150 + 1)
    randomId = random.choice(pokemonsId)
    llamarApi = consultaApiPokemon(randomId)  #obtener la información de un pokemon y tranformarlo en variable
    guardarEstructuraPokemon(llamarApi)
    #return seleccionRandom
#Link dek Import random:https://www.w3schools.com/python/ref_random_choice.asp
print(randomPokemon())