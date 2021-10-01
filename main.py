from requests.models import Response
from src.logic.functions import requests


data = requests.read_json()
print(data['pokemons'])
response = {}
for pokemon in data['pokemons']:
    pkm = requests.get_pokemon(pokemon)
    location = requests.get_location(pkm.location_area_encounters)
    response[pokemon] = {

        "dados" : pkm.to_return(),
        "area" : location
    }

print(response)