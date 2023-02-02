import requests
import json


token = '9619bc8025671b17b1619158b3b7f5a3'
url = "https://pokemonbattle.me:5000"
pokemon = "/pokemons" 
poketball = "/trainers/add_pokeball" 
img = "https://papik.pro/uploads/posts/2021-12/1639264981_1-papik-pro-p-pikachu-klipart-1.png"

def print_response():
    response = requests.post(url + pokemon, headers={'trainer_token':token}, json= {
        "name":"Это мой покемон",
        "photo": img
        })
    print(json.dumps(response.json(), indent=4, ensure_ascii=False)) 
    id = response.json().get('id')   

    put =  requests.put(url + pokemon, headers={'trainer_token':token}, json= {
        "pokemon_id":id,
        "name":"NewName",
        "photo": img
        })
    print(json.dumps(put.json(), indent=4, ensure_ascii=False)) 
    
    add_poketbol = requests.post(url + poketball, headers={'trainer_token':token}, json= {
        "pokemon_id":id,
        })   
    print(json.dumps(add_poketbol.json(), indent=4, ensure_ascii=False)) 
    

print_response()

                   





