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
