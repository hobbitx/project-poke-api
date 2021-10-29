from typing import List, Any


class Species:
    name: str
    url: str

    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url


class Ability:
    ability: Species
    is_hidden: bool
    slot: int

    def __init__(self, ability: Species, is_hidden: bool, slot: int) -> None:
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot


class GameIndex:
    game_index: int
    version: Species

    def __init__(self, game_index: int, version: Species) -> None:
        self.game_index = game_index
        self.version = version


class VersionDetail:
    rarity: int
    version: Species

    def __init__(self, rarity: int, version: Species) -> None:
        self.rarity = rarity
        self.version = version


class HeldItem:
    item: Species
    version_details: List[VersionDetail]

    def __init__(self, item: Species, version_details: List[VersionDetail]) -> None:
        self.item = item
        self.version_details = version_details


class Stat:
    base_stat: int
    effort: int
    stat: Species

    def __init__(self, base_stat: int, effort: int, stat: Species) -> None:
        self.base_stat = base_stat
        self.effort = effort
        self.stat = stat


class TypeElement:
    slot: int
    type: Species

    def __init__(self, slot: int, type: Species) -> None:
        self.slot = slot
        self.type = type


class Pokemon:
    abilities: List[Ability]
    base_experience: int
    forms: List[Species]
    game_indices: List[GameIndex]
    height: int
    held_items: List[HeldItem]
    id: int
    is_default: bool
    location_area_encounters: str
    name: str
    order: int
    past_types: List[Any]
    species: Species
    stats: List[Stat]
    types: List[TypeElement]
    weight: int

    def __init__(self, abilities: List[Ability], base_experience: int, forms: List[Species], game_indices: List[GameIndex], height: int, held_items: List[HeldItem], id: int, is_default: bool, location_area_encounters: str, name: str, order: int, past_types: List[Any], species: Species, stats: List[Stat], types: List[TypeElement], weight: int) -> None:
        self.abilities = abilities
        self.base_experience = base_experience
        self.forms = forms
        self.game_indices = game_indices
        self.height = height
        self.held_items = held_items
        self.id = id
        self.is_default = is_default
        self.location_area_encounters = location_area_encounters
        self.name = name
        self.order = order
        self.past_types = past_types
        self.species = species
        self.stats = stats
        self.types = types
        self.weight = weight

    def getTypes(self):
        string = []
        for type in self.types:
            string.append(str(type["type"]["name"]))
        return string
        
    def getStats(self):
        string = {}
        for stat in self.stats:
            string[str(stat["stat"]["name"])] = str(stat["base_stat"])
        return string

    def to_response(self):
        return {
            "types" : self.getTypes(),
            "size":self.weight,
            "stats": self.getStats()
            }