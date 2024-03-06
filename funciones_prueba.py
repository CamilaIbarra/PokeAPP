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
            #return data
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

guardarJson = consultaApiPokemon(22)

def guardarEstructuraPokemon(guardarJson, name):
    with open(name+".json", "w") as json_file:
        json.dump(guardarJson, json_file, indent=4)
    print(guardarJson)

#guardarEstructuraPokemon(guardarJson, guardarJson["nombre"])
#guardarEstructuraPokemon(consultaApiPokemon("pikachu"))

#op1_nos manejamos con funciones | metodos

#op2_manejamos diccionario (vive en memoria, una vez q termina ya murio).

#funcion q recibe como parametro otra funcion
