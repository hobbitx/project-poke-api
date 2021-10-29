from src.logic.functions import requests
import json

f = open('inputs/example.json')
data = json.load(f)
response = {}
for pokemon in data['pokemons']:
    response[pokemon] = requests.get_pokemon(pokemon).to_response()

print(json.dumps(response, indent=4, sort_keys=True))