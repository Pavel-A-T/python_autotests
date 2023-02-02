import requests
import json
import pytest 

trainer = "2067"
url = "https://pokemonbattle.me:5000/trainers"
name = "Jhon"

#Проверить, что запрос GET /trainers - вернёт код 200
def test_status_code():
    response = requests.get(url)
    assert response.status_code == 200


#Проверь, что в ответе приходит строчка с именем твоего тренер
def test_check_name():
    response = requests.get(url, params={
        "trainer_id":trainer
    })
    assert response.json()["trainer_name"] == name
