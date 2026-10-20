from lib.pokemon import Pokemon

def test_pokemon_instantiates():
# Pokemon instantiates
    pokemon = Pokemon(1, 'Raichu', 'electric')

    assert pokemon.id == 1
    assert pokemon.name == 'Raichu'
    assert pokemon.power_type == 'electric'

def test_pokemon_prints_nicely():
    # Pokemons prints nicely
    pokemon = Pokemon(1, 'Raichu', 'electric')

    assert str(pokemon) == "Pokemon(1, Raichu, electric)"

def test_two_pokemons_with_same_attribute_are_equal():
    # Pokemons equal
    pokemon = Pokemon(1, 'Raichu', 'electric')
    pokemon_2 = Pokemon(1, 'Raichu', 'electric')

    assert pokemon == pokemon_2
