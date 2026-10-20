from lib.pokemon import Pokemon

class PokemonRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute("SELECT * FROM pokemons")

        pokemons = []

        for poke_dict in rows:
            pokemon = Pokemon(poke_dict['id'], poke_dict['name'], poke_dict['power_type'])
            pokemons.append(pokemon)
        
        return pokemons
    
    def create(self, pokemon):
        self.connection.execute(
            "INSERT INTO pokemons(name, power_type) VALUES(%s, %s)",
            [pokemon.name, pokemon.power_type]
        )
    
    def find(self, pokemon_id):
        rows = self.connection.execute(
            "SELECT * FROM pokemons WHERE id = %s", 
            [pokemon_id]
        )

        return Pokemon(rows[0]['id'], rows[0]['name'], rows[0]['power_type'])