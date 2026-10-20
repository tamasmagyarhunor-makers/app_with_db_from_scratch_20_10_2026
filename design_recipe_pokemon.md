### Problem
```
As a Pokemon lover
So that I can play with my pokemons
I want to be able to create a Pokemon with a name, and power_type

As a Pokemon lover
So that I can store my pokemons
I want to be able to store my pokemons in a database
```


### Class and functions, SQL signature/schema
```python
class Pokemon:
    # id: int, eg. 1
    # name: str, eg. Raichu
    # power_type: str, eg. electric

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

```

```python
class PokemonRepository:
    # connection: DatabaseConnection
    def __init__(self, conn):
        self.connection = conn

    def all(self):
        pass
        # Parameters: None
        # Returns: list of pokemons
        # Side effects: None*

    def create(self, pokemon):
        # Parameters: Pokemon object
        # Returns: None
        # Side effects: Stores the Pokemon in the database
        pass
    
    def find(self, pokemon_id):
        # Parameters: int, id, eg. 2
        # Returns: Pokemon
        # Side effects: None*
        pass
    
    def delete(self, pokemon_id):
        # Parameters: int, id, eg. 2
        # Returns: None
        # Side effects: Deletes the Pokemon from the DB with the pokemon_id provided
        pass
 fi
```

```sql
DROP TABLE IF EXISTS pokemons;
DROP SEQUENCE IF EXISTS pokemons_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS pokemons_id_seq;
CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    power_type VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO pokemons (name, power_type) VALUES ('Raichu', 'electric');
INSERT INTO pokemons (name, power_type) VALUES ('Bulbasaur', 'earth-water');
INSERT INTO pokemons (name, power_type) VALUES ('MewTwo', 'psychio');
INSERT INTO pokemons (name, power_type) VALUES ('Charmander', 'fire');


```

### Examples
```python
# Pokemon instantiates
pokemon = Pokemon(1, 'Raichu', 'electric')

pokemon.id #=> 1
pokemon.name #=> Raichu
pokemon.power_type #=> electric

# Pokemons prints nicely
pokemon = Pokemon(1, 'Raichu', 'electric')

str(pokemon) == "Pokemon(1, Raichu, electric)"

# Pokemons equal
pokemon = Pokemon(1, 'Raichu', 'electric')
pokemon_2 = Pokemon(1, 'Raichu', 'electric')

pokemon == pokemon #=> True

```

```python
# all function
poke_repository = PokemonRepository(connection)

poke_repository.all() #=> [Pokemon(1, Raichu, electric), Pokemon(2, Bulbasaur, earth-water), Pokemon(3, MewTwo, psychio), Pokemon(4, Charmander, fire)]

#######

# create function
pokemon = Pokemon('Venusaur', 'earth-water')
poke_repository = PokemonRepository(connection)

poke_repository.create(pokemon)

poke_repository.all() #=> [Pokemon(1, Raichu, electric), Pokemon(2, Bulbasaur, earth-water), Pokemon(3, MewTwo, psychio), Pokemon(4, Charmander, fire), Pokemon(5, Venusaur, earth-water)]
######

# find function
poke_repository = PokemonRepository(connection)

poke_repository.find(1) #=> Pokemon(1, "Raichu", "electric")


```

```SQL
SELECT * FROM pokemons;
-- {1, 'Raichu', 'electric'}
-- {2, 'Bulbasaur', 'earth-water'}
-- {3, 'MewTwo', 'psychio'}
-- {4, 'Charmander', 'fire'}
```
