import requests
import json

inicio_pokemon = 1
fin_pokemon = 150

for pokemon_id in range(inicio_pokemon, fin_pokemon + 1):
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/pokemon_id")

        if response.status_code == 200:
            data = response.json()

            nombre_archivo = f"{data['name']}_info.json"
            pokemon_info = {
            "nombre": data["name"],
            "altura": data["height"],
            "peso": data["weight"],
            "tipos": [tipo["type"]["name"] for tipo in data["types"]],
            # Puedes agregar más campos según tus necesidades
        }
            # Guardar los datos específicos en un archivo JSON
        with open(nombre_archivo, 'w') as json_file:
            json.dump(pokemon_info, json_file, indent=2)

    except Exception as e:
        pass