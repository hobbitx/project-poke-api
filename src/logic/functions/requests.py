import json
from os import read
import requests
from src.models import pokemon_model as pkm_model

url_base = "https://pokeapi.co/api/v2"

def get_pokemon(name):
    r = requests.get(f"{url_base}/pokemon/{name}")
    if r.status_code != 200:
        return None
    r = r.json()
    pokemon = pkm_model.Pokemon(r['abilities'],r['base_experience'], r['forms'],r['game_indices'],r['height'],r['held_items'],r['id'],r['is_default'],r['location_area_encounters'],r['name'],r['order'],r['past_types'],r['species'],r['stats'],r['types'],r['weight'])
    return pokemon

def read_json():
    with open('inputs/example1.json','r') as f:
        list=json.load(f)
    return list

def get_location(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    r = r.json()
    location = ''
    max_chance = 0
    for obj in r:
       for ver in obj['version_details']:
           for details in ver['encounter_details']:
               chance = details['chance']
               if chance > max_chance:
                   max_chance = chance
                   location = str(obj['location_area']['name'])
    return location