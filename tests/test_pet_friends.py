import os

from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()

# Эти тесты были в учебном модуле
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Тест на получение API-ключа"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """Тест на получение списка всех питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert  len(result['pets']) > 0

import os

def test_add_new_pet():
    """Тест на добавление нового питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo_path = os.path.join(os.path.dirname(__file__), 'images/cat.png')
    status, result = pf.add_new_pet(auth_key, "Minie", "Кот", "2", pet_photo=pet_photo_path)
    assert status == 200
    assert result['name'] == "Minie"


def test_update_pet_info():
    """Тест на обновление информации о питомце"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(pets['pets']) > 0:
        pet_id = pets['pets'][0]['id']
        status, result = pf.update_pet_info(auth_key, pet_id, "Minie", "Кот", "3")
        assert status == 200
        assert result['name'] == "Minie"


def test_delete_pet():
    """Тест на удаление питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(pets['pets']) > 0:
        pet_id = pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)
        _, pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert status == 200
        assert pet_id not in [pet['id'] for pet in pets['pets']]

# Практическое задание 24.7.2
# 1. Эти тесты к методам, которые ещё не реализованы в библиотеке
def test_create_pet_simple():
    """Тест на добавление нового питомца без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, "Ася", "Кот", "2")
    assert status == 200
    assert result['name'] == "Ася"

def test_set_photo_pet():
    """Тест на добавление фото питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(pets['pets']) > 0:
        pet_id = pets['pets'][1]['id']
        pet_photo_path = os.path.join(os.path.dirname(__file__), 'images/cat2.jpg')
        status, result = pf.set_photo_pet(auth_key, pet_id, pet_photo=pet_photo_path)
        assert status == 200
        assert 'pet_photo' in result
    else:
        raise Exception("У вас нет питомцев для добавления фото.")

# 2. 10 различных методов для данного REST API-интерфейса

def test_delete_pet_with_invalid_auth_key():
    """ 1. Тест на удаление питомца с неверным API ключом"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(pets['pets']) > 0:
        pet_id = pets['pets'][0]['id']
        invalid_auth_key = {"key": "invalid_key"}
        status, _ = pf.delete_pet(invalid_auth_key, pet_id)
        assert status == 403
    else:
        raise Exception("У вас нет питомцев для удаления.")

def test_create_pet_with_invalid_auth_key():
    """ 2. Тест на добавление нового питомца с неверным API ключом"""
    invalid_auth_key = {"key": "invalid_key"}
    status, result = pf.add_new_pet_simple(invalid_auth_key, "Барсик", "Кот", "4")
    assert status == 403

def test_create_pet_simple_invalid_data():
    """ 3. Тест на добавление нового питомца без фото с невалидными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, "", "", "-1")
    assert status == 200

def test_create_pet_simple_negative_age():
    """ 4. Тест на добавление нового питомца без фото с отрицательным возрастом"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, "Том", "Кот", "-5")
    assert status == 400

def test_delete_nonexistent_pet():
    """ 5. Тест на удаление несуществующего питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_id = "invalid_pet_id"
    status, _ = pf.delete_pet(auth_key, invalid_pet_id)
    assert status == 404

def test_update_nonexistent_pet_info():
    """ 6. Тест на обновление информации о несуществующем питомце"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_id = "invalid_pet_id"
    status, result = pf.update_pet_info(auth_key, invalid_pet_id, "Неизвестный", "Собака", "5")
    assert status == 404

def test_update_nonexistent_pet_info():
    """ 7. Тест на обновление информации о несуществующем питомце"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_id = "invalid_pet_id"
    status, result = pf.update_pet_info(auth_key, invalid_pet_id, "ААА", "Собака", "5")
    assert status == 404

def test_create_pet_simple_long_name():
    """ 8. Тест на добавление нового питомца без фото с длинным именем"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    long_name = "Барсик"*50
    status, result = pf.add_new_pet_simple(auth_key, long_name, "Кот", "2")
    assert status == 400

def test_create_pet_simple_special_char_animal_type():
    """ 9. Тест на добавление нового питомца без фото с типом животного, содержащим специальные символы"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, "Том", "Кот!!_!!", "3")
    assert status == 400

def test_get_pets_invalid_category():
    """ 10. Тест на получение списка питомцев с неверной категорией"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, "invalid_category")
    assert status == 500


















