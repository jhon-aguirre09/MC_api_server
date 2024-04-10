from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_add_person():
    response = client.post('/create', json = {
                                                    "id": 1, 
                                                    "name": "Jhon",
                                                    "identification": 10245522,
                                                    "email": "j@j.com",
                                                    "direction": "Calle Falsa 123",
                                                    "phone": 3208940782
                                                    })
    assert response.status_code == 201
    assert response.json()[0]["name"] == "Jhon"

def test_add_second_person():
    response = client.post('/create', json = {
                                                    "id": 2, 
                                                    "name": "Marcos",
                                                    "identification": 10243333,
                                                    "email": "j@j.com",
                                                    "direction": "Calle Falsa 123",
                                                    "phone": 3208940782
                                                    })
    assert response.status_code == 201
    assert response.json()[0]["name"] == "Marcos"

def test_get_person():
    response = client.get('/people/1')
    assert response.status_code == 200
    assert response.json()["name"] == "Jhon"
    
def test_get_people():
    response = client.get('/people')
    
    assert response.status_code == 200
    assert len(response.json()) == 2