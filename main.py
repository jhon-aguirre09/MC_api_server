from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

app = FastAPI()

app.title = "App Server"

class Person():

	def __init__(self, id, name, identification, email, direction, phone):
		self.id = id
		self.name = name
		self.identification = identification
		self.email = email
		self.direction = direction
		self.phone = phone

class PersonManager():

	def __init__(self):
		self.__people = []

	def add_person(self, new_person):
		self.__people.append(new_person)

	def get_list_people(self):
		return self.__people
		
	def get_detail_person(self, id):
		person = next((item for item in self.__people if item.id == id), None)
		if person:
			return {
				'id': person.id,
				'name': person.name,
				'identification': person.identification,
				'email': person.email,
				'direction': person.direction,
				'phone': person.phone,
			}

people = PersonManager()

@app.post('/create', tags=['Create Person'])
def person_creation(
		id: int = Body(0),
		name: str = Body(''),
		identification: int = Body(0),
		email: str = Body(''),
		direction: str = Body(''),
		phone: int = Body('')
	):
	
	person = Person(
		id, name, identification, email, direction, phone
	)
	people.add_person(person)
	people.get_detail_person(id)
	return JSONResponse(status_code=201, content=[people.get_detail_person(id)])

@app.get('/people/{pk}', tags=['Detail Person'])
def get_person(pk: int):
	return people.get_detail_person(pk)


@app.get('/people', tags=['List People'])
def get_people():
	return people.get_list_people()