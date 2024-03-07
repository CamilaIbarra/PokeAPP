import requests
import json
import clases.Pokemon as Pokemon
import os

apiOk = 200

def consultaApiPokemon(id):
    try:
        nombre = str(id)
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + nombre.lower())
        if response.status_code == apiOk:
            data = response.json()
            return crearEstructuraPokemon(data)
            #return data
        else:
            return None
    except Exception as e:
        print(f"Error al obtener información del ID Pokemon {id}: {e}")
        return None

def crearEstructuraPokemon(data):
    return {
       "nombre": data["name"],
            "hp": data["stats"][0]["base_stat"],       
            "ataque": data["stats"][1]["base_stat"], 
            "defensa": data["stats"][2]["base_stat"], 
            "tipos": [tipo["type"]["name"] for tipo in data["types"]]
       
    }

def damePokemones(inicio, fin):
   
    try:
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon?limit={fin}&offset={inicio}")

        if (response.status_code == 200):
            data = response.json()
            return data

    except Exception as e:
        print(f"ERROR: {e}")

def guardarEstructuraPokemon(path, guardarJson, name):
    base_dir = 'pokemones/'+str(path)

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    file_name = name+".json"
    file_path = os.path.join(base_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, "w") as json_file:
            json.dump(guardarJson, json_file, indent=4)
        print(guardarJson)
    else:
        print(f"El pokemon "+name+" ya existe.")

    
def crearPokemon(pika):
    pokemonDev=Pokemon(pika["hp"],pika["ataque"],pika["defensa"],pika["tipos"],pika["nombre"])
    return pokemonDev
    
def usarArchivoCreado(name):
    with open("PresetPokemones/"+name+".json", "r")as file:
        poke = json.loads(file)
        return crearPokemon(crearEstructuraPokemon(poke))
    