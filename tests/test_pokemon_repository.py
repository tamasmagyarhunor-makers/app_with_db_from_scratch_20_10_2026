from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

def test_pokemon_repository_all(db_connection):
    db_connection.seed("seeds/pokemons_seed.sql")
    # all function
    poke_repository = PokemonRepository(db_connection)

    pokemons = poke_repository.all() 
    
    assert pokemons == [
        Pokemon(1, 'Raichu', 'electric'), 
        Pokemon(2, 'Bulbasaur', 'earth-water'), 
        Pokemon(3, 'MewTwo', 'psychio'), 
        Pokemon(4, 'Charmander', 'fire')
    ]

def test_find_pokemon(db_connection):
    db_connection.seed("seeds/pokemons_seed.sql")
    poke_repository = PokemonRepository(db_connection)

    raichu = poke_repository.find(1) 
    
    assert raichu == Pokemon(1, "Raichu", "electric")

def test_pokemon_repository_create(db_connection):
    # create function
    pokemon = Pokemon(None, 'Venusaur', 'earth-water')
    poke_repository = PokemonRepository(db_connection)

    poke_repository.create(pokemon)

    pokemons = poke_repository.all() 
    assert pokemons == [
        Pokemon(1, 'Raichu', 'electric'), 
        Pokemon(2, 'Bulbasaur', 'earth-water'), 
        Pokemon(3, 'MewTwo', 'psychio'), 
        Pokemon(4, 'Charmander', 'fire'), 
        Pokemon(5, 'Venusaur', 'earth-water')
    ]