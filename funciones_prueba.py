import requests
import json
import os

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
    }

# guardarJson = consultaApiPokemon(5)

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

# guardarEstructuraPokemon(guardarJson, guardarJson["nombre"])

