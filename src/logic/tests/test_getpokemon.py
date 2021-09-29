import unittest
from ..functions import requests

class TestGetPokemon(unittest.TestCase):
    def test_get_pokemon(self):
        name = "butterfree"
        pokemon = requests.get_pokemon(name)
        self.assertEqual(name, pokemon.name)

    def test_error_get_pokemon(self):
        name = "batata"
        pokemon = requests.get_pokemon(name)
        self.assertEqual(pokemon,None)

if __name__ == '__main__':
    unittest.main()