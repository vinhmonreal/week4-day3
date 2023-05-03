from requests import get
from IPython.display import Image
from linkedlist import LinkedList, Node

class Pokemon():
    
    def __init__(self, name):
        self.name = name
        self.evolve_chain = LinkedList()
        self.abilities = []
        self.types = []
        self.weight = None
        self.image = None
        self.call_poke_api()
        
    def call_poke_api(self):
        response = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response.status_code == 200:
            print('Success')
            data = response.json()
            self.name = data['name']
            self.abilites = [ability_object['ability']['name'] for ability_object in data['abilities']],
            self.types = [type_object['type']['name'] for type_object in data['types']]
            self.weight = data['weight']
#            self.image = data['sprites']['front_default']
            self.image = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
            if not self.image:
                self.image = data['sprites']['front_default']
            self.species_url = data['species']['url']
            #display(Image(self.image, width = 200))
        else:
            print(f'Error status code {response.status_code}')
            
    def get_evolution_chain(self):
        response = get(self.species_url)
        if response.status_code == 200:
            data = response.json()
        evolution_chain_url = data['evolution_chain']['url']
        evolution_chain = get(evolution_chain_url)
        if evolution_chain.status_code == 200:
            return evolution_chain.json()['chain']
        
    def add_evolve_chain(self, evolution_chain):
        current_pokemon_in_chain = evolution_chain['species']['name']
        self.evolve_chain.add_node(current_pokemon_in_chain)
        if not evolution_chain['evolves_to']:
            print(f'This is the final from')
            return

        return self.add_evolve_chain(evolution_chain['evolves_to'][0])
        
my = Pokemon('eevee')
my.add_evolve_chain(my.get_evolution_chain())
print(my.evolve_chain)
print(my.evolve_chain.get_length())
