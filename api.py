import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    # Эти методы были в учебном модуле
    def get_api_key(self, email, password):
        """Метод делает запрос к APi сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключом пользователя, найденного по указанным email и password"""

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к APi сервера и возвращает статус запроса и результат в формате
        JSON со списком найденных питомцев, совпадающих с фильтром. На данный момент фильтр может
        иметь либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к APi сервера и возвращает статус запроса и результат в формате
        JSON со списком найденных питомцев, совпадающих с фильтром. На данный момент фильтр может
        иметь либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: object, name: object, animal_type: object, age: object, pet_photo: object) -> object:
        """Метод отправляет данные о новом питомце на сервер и возвращает статус запроса и
        результат в формате JSON"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        file = {'pet_photo': open(pet_photo, 'rb')}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key, pet_id, name, animal_type, age):
        """Метод обновляет информацию о питомце по указанному ID и возвращает статус запроса
        и результат в формате JSON"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.put(self.base_url + f'api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key, pet_id):
        """Метод удаляет питомца по указанному ID и возвращает статус запроса и результат
        в формате JSON"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    # Практическое задание 24.7.2
    # 1. Эти методы, которые ещё не реализованы в библиотеке

    def add_new_pet_simple(self, auth_key: object, name: object, animal_type: object, age: object) -> object:
        """Метод отправляет данные о новом питомце без фото на сервер и возвращает статус запроса и
        результат в формате JSON"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def set_photo_pet(self, auth_key, pet_id, pet_photo):
        """Метод добавляет фото питомцу по указанному ID и возвращает статус запроса и результат
        в формате JSON"""

        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': open(pet_photo, 'rb')}

        res = requests.post(self.base_url + f'api/pets/set_photo/{pet_id}', headers=headers, files=file)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


