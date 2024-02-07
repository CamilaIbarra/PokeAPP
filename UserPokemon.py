import requests

def userPokemon(pokemon_name):
    try:
        name = pokemon_name.lower()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        if response.status_code == 200:
            data = response.json()
            pokemon = {
                "nombre": data["name"],
                "altura": data["height"],
                "peso": data["weight"]
            }
            return pokemon
    except Exception as e:
        pass
